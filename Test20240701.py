# -*- coding:utf-8 -*-
stu_score_dic={
    "王力宏":{
        "語文":77,
        "數學":66,
        "英文":33
    }, "周杰倫":{
        "語文":88,
        "數學":86,
        "英文":55
    }, "林俊傑":{
        "語文": 99,
        "數學": 96,
        "英文": 66
    }
}

print(f"可是訊息{stu_score_dic}")
r = stu_score_dic["王力宏"]["語文"]
print(r)

stu_score_dic["吳中石"]:33
print(stu_score_dic)

stu_score_dic={
    "王力宏":77,
    "周杰倫":88
    "林俊傑":12}
stu_score_dic.clear()
print(stu_score_dic)