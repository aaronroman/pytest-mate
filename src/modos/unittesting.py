import re


def GEN_SYSTEM_PROMPT():
    modo = """You MUST write unittesting code in python.
              I will provide you with the filename and the code.
              In your response, you MUST return only the test code withing codeblock.
              Add comments to the code, don't forget to import the modules you need.
              """
    return re.sub(r"\s+", " ", modo)


_SYSTEM_PROMPT = GEN_SYSTEM_PROMPT()
