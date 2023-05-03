i = int(input())
while i != 0:
    if i < 0:
        print("Встретилось отрицательное число", i)
        break
    i = int(input())
else:
    print("Не найдено отрицательных чисел")    
    