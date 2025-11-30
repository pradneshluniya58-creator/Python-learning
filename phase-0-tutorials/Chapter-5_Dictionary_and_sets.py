#Dictionary example and a few common functions
oxford = {
    "key" : "something",
    "gift" : "something willingly given to someone to appreciate",
    "this" : "A keyword in C++",
    "mylist"  : [3,5,78,85],
}
# print(oxford)

# print(oxford["this"])

# print(oxford.items())
# for a,b in oxford.items():     #using the for loop
#     print(a,":",b)             #using the for loop

# print(oxford.keys()) #prints just the keys
# for a in oxford.keys():         #using the for loop
#     print(a)                    #using the for loop

# oxford.update({"key" : "nothing","youtube" : "A video sharing platform"}) #updates the dictionary
# for a,b in oxford.items():     
#     print(a,":",b)             

# Sets dosen't contain duplicate items i.e it contains unique values  

myset = {4 ,5,6 ,7}
# print(myset.pop()) # Removes first element from the set and returns it 
# print(len(myset))  # Prints the length of the set
# myset.add(45) #add to the set if not already present
# myset.add(4) #nothing will happen as set already has 4
# myset.add("4") # will add "4" as string and integer are different
# myset.remove(4) # Removes an element from the set , gives error if the element not in set
# myset.clear() #empties the set 
# set works like set in mathematics i.e it has union , intersection , + and - , i will not write all those functions here so just check those functions at docs.python.org , it also has superset and subset functions etc etc
print(myset)