set1={23,45,5,90,34}
set2={83,45,87,98,90}
set1.add(78)
set2.remove(90)
print(set1)
print(set2)
#print(set1&set2)
print(set1.intersection(set2))
#print(set1|set2)
print(set1.union(set2))
print(set2.issubset(set1))
print(set2.issuperset(set1))
#print(set1-set2)
print(set1.difference(set2))