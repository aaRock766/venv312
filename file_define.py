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

    def read_data(self): -> list[Record]312
