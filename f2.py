"""
num=input() #read input
print(num)
print(type(num))#checking the type of variable
"""

"""
num=int(input()) #read input
val=float(input())
print(type(num),type(val))#checking the type of variable
res=num+val
print(res)
print(type(res))
"""

"""
num=input() #read input

print(type(num))#checking the type of variable
res=num1+10 # TypeError: can only cancatenate str (not 'int') to str
print(res)
"""

"""
#to overcome the above problem we use explicit conversion

num=input() #read input
print(type(num))#checking the type of variable
res=int(num1) + 10 # works and gives output : 20
print(res)
"""

# Converting integer to float, String and Boolean

num = -10
print(float(num))
print(str(num))
print(bool(num))

flt=12.45
print(int(flt))
print(str(flt))
print(bool(flt))

Str="Hihello"
#print(float(Str)) #ValueError: could not convert string to float: 'Hihello'
#print(int(Str)) #ValueError: invalid literal for int() with base 10: 'Hihello'
print(bool(Str))
print(tuple(Str))
print(set(Str))
print(list(Str))

List=[1,2,3,4,2,3]
print(tuple(List))
print(set(List))
print(str(List))

tup=(1,2,3,4,5)
print(list(tup))
print(set(tup))
print(str(tup))

Set={1,3,2,4,5}
print(tuple(Set))
print(list(Set))
print(str(Set))


