"""
定義文件相關的類
"""
from data_define import Record


class FileReader:
    def read_data(self) -> list[Record]:
        pass


class TextFileReader(FileReader):
    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")
        for line in f.readlines():
            line = line.strip("\n")
            data_list = line.split(",")
            print(data_list)


if __name__ == '__main__':
    text_file_reader = TextFileReader("Image_006.txt")
    text_file_reader.read_data()