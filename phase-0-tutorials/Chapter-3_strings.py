# The string functions are
#len(name)
# name.endswith("")
# name.startswith("")
# name.count("")
# name.capitalize()
# name.find("")
# name.replace("old word","new word")
# chain replace example 
a = input("Enter the name : ")
b = input("Enter the date : ")
c = '''dear name,
You are selected
date
'''
print(c.replace("name",a).replace('date',b))