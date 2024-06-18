import itertools
s = input()
s1 = list(s)
li = itertools.permutations(s1) 
for i in list(li): 
    print("".join(i))