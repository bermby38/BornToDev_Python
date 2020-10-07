""""
tuple1 = ("a","b","c","d")
tuple2 = ("d","e")
tuple3 = tuple1+tuple2
print(tuple3[2])
print("a" in tuple3)
print("H" in tuple3)
for i in tuple3:
    print(i)

"""

tuple4 = (1,2,3,5,5,500)
print(max(tuple4))
print(tuple(tuple4))
print(tuple4.index(5))
