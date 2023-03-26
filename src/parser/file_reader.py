class FileReader:
    def __init__(self, file_list):
        self.file_list = file_list

    def read_files(self):
        file_contents = {}
        for file_path in self.file_list:
            with open(file_path, "r") as file:
                file_contents[file_path] = file.read()
        return file_contents
