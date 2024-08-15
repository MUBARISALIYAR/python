# # single line string 

# a='mubaris'
# print(a)

# # multiple line string
# a='''mubaris
# hisham
# muhsin'''
# print(a)

# # \n and \t 

# a='mubaris\naliyar'
# b='mubxz\t mubxz'
# print(a)
# print(b)


#                         # Index 

# a='python'
# print(a[2])

# # print type of a variable 

# a='mubz'
# print(type(a))

# # to print elements of a string from starting position 

# a="mubaris"
# print(a[0:4])     #prints elements from index[0]-index[3]
#         # or 
# print(a[:4])


# # to print elements of a string upto last positon 

# b='muhsin'
# print(b[3:6])    #prints elemts from index[3] to last index
#     # or 
# print(b[3:])

# # slicing           syntax = print(a[strt_index:last_index:step])

# c='hisham'
# print(a[::2])  #prints the elements from index 0 then index[lastindex+2] upto last

# d='shaukath'
# print(d[::-1])  #reverses the string



# # to check wheter a string is palindrome 

# a=input('enter the string=')
# print("reversed=",a[::-1])
# print(a==a[::-1])

# OR

# if(a==a[::-1]):
    # print('string is palindrome')
# else:
    # print("not a palindrome")
    

# capitalize

a="welcOMe ALl"
print(a.capitalize())
print(a.upper())
print(a.lower())
print(a.isupper())
print(a.islower())

# centralize ,count ,start, end ,find

a='mubaris'
print(a.center(20))

print(a.count('b'))

print(a.endswith('a'))

print(a.startswith('m'))

print(a.find('a'))
print(a.find('z'))

#remove blank space

a="          mubaris       "
print(a)
print(a.strip())
print(a.lstrip())
print(a.rstrip())

# check whether string is digit 

a="10004"
print(a.isdigit())



# table

print("{:<10}{:<8}{:<8}".format("name","age","mark"))
print("{:<10}{:<8}{:<8}".format("","",""))
print("{:<10}{:<8}{:<8}".format("mubz","22","50"))
print("{:<10}{:<8}{:<8}".format("mubxz","20","50"))