alist = [1,2,3,4,5,6,7,8]
print(alist)
print(alist[::2])
print(alist[::-1])
print(alist[0])
alist[1]= 100
print(alist)

print(alist.append(30))
print(alist)

print(alist.extend([80,89]))
print(alist)

print(alist.insert(0,30))
print(alist)

alist.sort()
print(alist)
alist.reverse()
print(alist)
alist.pop(0)
print(alist)
alist.remove(89)
print(alist)
atup =(1,2,3,4,5,6)
print(atup[0])
atup.count(1)


book = {'chap1':10,'char2':20}
print(book.keys())
print(book.values())
print(book.items())
print(book['chap1'])
print(book.get('chap3'))
book.pop("chap1")
print(book)
book.update({"cpa3":20})
print(book)

for val in range(1,5):
    print(val)
for char in "vaibhav":
    print(char)
for key in book.keys():
    print(key)
for value in book.values():
    print(value)
for key,value in book.items():
    print(key,value)
aset={1,2,3,4,5,6,7,8}
for val in aset:
    print(val)
    
    
