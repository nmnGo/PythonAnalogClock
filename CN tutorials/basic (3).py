var1= 24
# print(var1) gives 24 as output
var2 ="25"
# print(var2) gives 25 as output
# print(int(var2)+var1) prints 49 since int(var2 takes int valu from str)
var3="hello1"
# print(var3) prints hello1
# print(int(var3)) gives error since in string there are alphabets it is not a numerical value

print(var3+" "+var2) #" " adds space in bw string
# print(var3+var1)gives error since int + str is nothing
print(type(var3)) #tells the type of variable used