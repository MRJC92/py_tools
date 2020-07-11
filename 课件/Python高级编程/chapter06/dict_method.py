a = {"bobby1":{"company":"imooc"},
     "bobby2": {"company": "imooc2"}
     }
#clear
#a.clear()
# pass
#a=dict()
# #copy, 返回浅拷贝
# new_dict = a.copy()
# new_dict["bobby1"]["company"] = "imooc3"

#深拷贝
import copy
new_dict = copy.deepcopy(a)
new_dict["bobby1"]["company"] = "imooc3"

#formkeys 将可迭代对象转为dict
new_list = ["bobby1", "bobby2"]

new_dict = dict.fromkeys(new_list, {"company":"imooc"})

new_dict.update((("bobby","imooc"),))
new_dict.update(booby6="imooc1")
#如果有就返回值，没有就返回空
value = new_dict.get("bobby9",{})

default_value= new_dict.setdefault("bobby9","imooc")



pass
