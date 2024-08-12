mylist =['aaaaaa','bbbbbb', 'python']
r=mylist.index('python')
print(r)


mylist[0]='cccccc'
print(mylist)

mylist.insert(1,'best')
print(mylist)

mylist.append('iuyyy')
print(mylist)
mylist.extend(['ddd','iuyyy'])
print(mylist)


del mylist[0]
print(mylist)
mylist.pop(2)
print(mylist)
mylist.append('best')
# mylist.remove('best1')
print(mylist)
mylist.remove('best')
print(mylist)