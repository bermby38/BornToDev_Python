dict1 = {'Name':'James','Age':18}
dict2 = {'UserName':'Admin','Password':'1234'}
dict3 = dict1|dict2
print(dict1)
print(dict1['Name'],dict1['Age'],dict2['UserName'],dict2['Password'])
dict1['Lastname'] = 'Kotlin'
print(dict1)
dict1.clear()
print(dict1)
dict1['Name'] = 'Boy'
print(dict1)
print(dict3)