# main.py
import re
import pathlib
import os
from loguru import logger
from parser.file_scanner import FileScanner
from parser.file_reader import FileReader
from custom_openai.api_request import OpenAIModel
import modos.unittesting as modo
from dotenv import load_dotenv


def main():
    """
    Some hardcoded config
    @TODO move to config file
    """
    # load env
    load_dotenv()
    input_folder = os.getenv("INPUT_FOLDER")
    extension = os.getenv("VALID_EXTENSION")
    model_name = os.getenv("MODEL_NAME")
    api_key = os.getenv("API_KEY")
    output_test_folder = os.getenv("OUTPUT_TEST_FOLDER")

    # @TODO move to config file
    exclude_folders = [".venv", "build"]

    # get files
    scanner = FileScanner(input_folder, extension, exclude_folders)
    files = scanner.scan()

    # parse files
    files_list = FileReader(files).read_files()
    for filepath in files_list:
        # get filename
        filename = re.search(r"(\w+\.\w+$)", filepath).group(1)

        # check if code contains any method o class, if not continue
        if not re.search(r"(def|class)", files_list.get(filepath)):
            continue

        # if the only method if def main(): continue
        if re.search(r"(def main\(\):)", files_list.get(filepath)):
            continue

        # generate prompt
        prompt = ""
        prompt += f"filename: {filename}\n"
        prompt += f"code: {files_list.get(filepath)}"

        # save if not exists
        output_path = f"{output_test_folder}/test_{filename}"
        if not pathlib.Path(output_path).is_file():
            modelo = OpenAIModel(model_name, modo._SYSTEM_PROMPT, api_key)
            test_code = modelo.generate_response(prompt)

            # check if output folder exists
            if not pathlib.Path(output_test_folder).is_dir():
                logger.info(f"Creating output folder at {output_test_folder}")
                os.mkdir(output_test_folder)

            with open(output_path, "w") as fo:
                # get the code from codeblock
                if test_code.find("```") != -1:
                    test_code = FileScanner.get_code_from_codeblock(test_code)

                # save
                if len(test_code) == 0:
                    logger.critical(f"File {output_path} is empty")
                    continue

                fo.write(test_code)
                logger.success(f"File {output_path} created")
        else:
            logger.warning(f"File {output_path} already exists")


if __name__ == "__main__":
    main()
