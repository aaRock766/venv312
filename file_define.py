"""
定義文件相關的類
"""
import json

from data_define import Record


class FileReader:
    def read_data(self) -> list[Record]:
        pass


class TextFileReader(FileReader):
    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8-sig")
        record_list = []
        for line in f.readlines():
            line = line.strip("\n")
            # print(line)
            data_list = line.split(",")
            # print(data_list)
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)
        f.close()
        return record_list


class JsonFileReader(FileReader):

    def __init__(self, path):
        self.path = path

    def read_data(self) ->list[Record]:
        f = open(self.path, "r", encoding="UTF-8-sig")
        record_list = []

        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["date"], data_dict["order_id"], int(data_dict["money"]), data_dict["province"])
            record_list.append(record)


        f.close()
        return record_list


if __name__ == '__main__':
    text_file_reader = TextFileReader("image_006.txt")
    json_file_reader = JsonFileReader("image_007.txt")
    list1 = text_file_reader.read_data()
    list2 = json_file_reader.read_data()
    for l in list1:
        print(l)
