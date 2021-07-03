# list
print ('========LIST==========')
# telugu, hindi, english, maths, science, social.
marks = [69,68,90,58,30,20]
print(type(marks))
print (marks)
members = ["shiva ", "rama ", "krishna"]
print (members)
print ('second name is :',members[-1])
marks[4]=99
print (marks)
# concatination on the list.
print (marks + members)
print ( members*3)
members.append('nutalapati')
print (members)
members.extend(['ravi','sravan'])
print (members)
members.insert(1,"nota")
print (members)
# adding multiple friends using the slicing .
members[1:1]=["a","b","c"]
print(members)
del members[1]
print(members)
del marks[1:3]
print (marks)
print (members.pop(1))




