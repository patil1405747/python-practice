#creating dict
dict={"name":"gayatri", "id":1,"marks":90, "city":"pune"}
print(dict)

#methods of dictionary
#copy()
dic=dict.copy()
print(dic)

#fromkeys()
dic=dict.fromkeys("name")
print(dic)

#keys()
dic=dict.keys()
print(dic)

#get
dic=dict.get("name")
print(dic)

#values()
dic=dict.values()
print(dic)

#items()
dic=dict.items()
print(dic)

#update()
dic=dict.update({"name":"ram","id":2})
print(dic)

#pop()
dic=dict.pop("city")
print(dic)

#popitem()
dic=dict.popitem()
print(dic)

#clear()
dic=dict.clear()
print(dic)

#setdefault
dict={"name":"muttu","age":18,"city":"sankeshwar"}
age=dict.setdefault("sister","gayatri")
print(age)
print(dict)

#itearing a dictionary
for i,j,in dict.items():
    print(i,j)



