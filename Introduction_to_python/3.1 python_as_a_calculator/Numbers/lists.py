squares=[1,4,9,16,25]
print(squares)
a=squares[0]  # indexing returns the item

print(a)

#lists also support operations like concatenation
a=squares+[36,49,64,81,100]
print(a)
cubes=[1,8,27,65,125] #something's wrong here
cubes[3]=64 #replace the wrong values
print(cubes)

#you can also add new items at the end of the list,by using the list.append() method
cubes.append(12)
print(cubes)

#it is possible to lists (create lists contains other lists)
a=['a','b','c']
n=[1,2,3]
x=[a,n]
print(x)
print(x[0])
print(x[0][1])
