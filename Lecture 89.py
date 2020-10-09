import json
print("1".center(20,"-"))

example1 =  '{ "name":"John", "age":30, "city":"New York"}'
print(type(example1))
print(example1)

jason1 = json.loads(example1)
print(type(jason1))
print(jason1["name"])

print("2".center(20,"-"))

example2 = '["a","b","c"]'
print(type(example2))
print(example2)

jason2 = json.loads(example2)
print(type(jason2))
print(jason2)

print("3".center(20,"-"))

example3 = '["c","d",1]'
print(type(example3[2]))
print(example3[2])

jason3 = json.loads(example3)
print(type(jason3))
print(jason3)
jason3 = json.dump()

jason3.dumps(["apple", "bananas"])
print(jason3)




def readjson():
    # some JSON:
    x =  '{ "name":"John", "age":30, "city":"New York"}'

    # parse x:
    y = json.loads(x)

    # the result is a Python dictionary:
    print(y["age"])

def convertjson():
    print(json.dumps({"name": "John", "age": 30}))
    print(json.dumps(["apple", "bananas"]))
    print(json.dumps(("apple", "bananas")))
    print(json.dumps("hello"))
    print(json.dumps(42))
    print(json.dumps(31.76))
    print(json.dumps(True))
    print(json.dumps(False))
    print(json.dumps(None))

#readjson()
#convertjson()