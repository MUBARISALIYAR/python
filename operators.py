                                        # ARITHMETIC OPERATORS

# addition

print(10+5)
print('mubz'+'mubz')

# substraction

print(10-5)

# multiplicaton

print(10*5)
print('mubz '*3)

# division 
 
print(10/3)

# floor division

print(10//3)

# exponential

print(10**2)

# modulus

print(10%3)

                                            # ASSIGNMENT OPERATORS


# EQUAL To 

a=10
print(a)

# plus equal to   A=A+5

a=10
a+=5
print(a)

# minus equal to   A=A-5

a=10
a-=5
print(a)

# star equal to   A=A*5

a=10
a*=5
print(a)

# slash equal to   A=A/5

a=10
a/=5
print(a)

# modulus equal to   A=A%5

a=10
a%=3
print(a)

                                            # COMPARISON OPERATORS

# eqaul to 

print(10==10)
print('apple'=='apple')


# not equalto 

print(10!=10)

# greater than 

print(10>5)

# less than 
 
print(10<5)

# less than or equal to 

print(10<=15)

# greater than or equal to 

print(10>=10)

                                                # LOGICAL OPERATORS 

# and

print(10==10 and 10<=9)   

            # true     true  = true 
            # false    true  = false
            # true     false = false 
            # false    false = false                                        


# or 

print(10==10 or 10<=9)

            # true     true  = true 
            # false    true  = true 
            # true     false = true 
            # false    false = false  
            
# not 

print(not(10==10))

            # true  = false
            # false = true                                     
                           

                                                # MEMBERSHIP OPERATORS

# in 

a='mubaris'
b='h'
print( b in a)
print('h' in b)

# not in 

a=[1,2,3]
b=[[1,2,3],[4,5,6,7]]
print(b not in a)
print(a not in b)


                                                # IDENTITY OPERATORS (compares the id of memory location )

# IS 

a=10
b=10
print(id(a))
print(id(b))
print(a is b)

a=[1,2]
b=[1,2]
print(id(a))
print(id(b))
print(a is b)


# is not

a=10
b=10
print(id(a))
print(id(b))
print(a is not b)

a=[1,2]
b=[1,2]
print(id(a))
print(id(b))
print(a is not b)
