"""
與文件有關的類定義
"""
from data_define import Record
class FileReader:

    def read_data(self) ->list[Record]:
        pass


class TextFileReader(FileReader):
    def __init__(self, path):
        self.path = path

    def read_data(self) ->list[Record]:
        f=open(self.path, 'r', encoding='utf-8')
        for line in f.readlines():


