# # #def eto functsiya, cluchevoe slovo
# # #def greeting():
# #     # print("privet")
    
# # #greeting()

# # #def hello(name):
# #     print (name, "hello")
    
# # #name = input("name: ")  
# # hello(name)      

# # def findsum(a, b):
# #     return a + b
# # x = int(input(("zhaz:"))) 
# # y = int(input("zhaz:"))
# # print (findsum(x, y)) 

# # # subtraction     
# # def subtraction(a, b):
# #     return a - b
# # x = int(input(("zhaz:"))) 
# # y = int(input("zhaz:"))
# # # print (subtraction(x, y))                                         

# #is_even

# y = int(input())
# def is_even(y):
#     if y % 2 == 1:
#         print ("chislo nechetnoe")
#     else:
#         print ("chislo chetnoe")

# is_even(y)

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# j = [a*2, b*2, c*2, d*2]    
# def double_list(
    
# ):
#     print (j)
    
# double_list ()

def double_list():
    num = input().split()
    doubled = [int(i) * 2 for i in num]
    print(doubled)
    
double_list()