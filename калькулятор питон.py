заново = 'T'
while заново == 'T':
    import math
    firstnumber_num = float (input("Введите число"))# первая переменная
    operation = input ("Введите операцию") # операция
    secondnumber = float (input("Введите число")) # вторая переменная
    син = math.sin
    кос = math.cos
    таг = math.tan
    корень = (firstnumber_num ** 0.5 )
    факториал = math.factorial 
    if operation == '+': # если операции будет присвоина плюс
        print (firstnumber_num + secondnumber) # вывести сложение переменных
    elif    operation == '-': # если операции будет присвоина минус
        print (firstnumber_num - secondnumber) # вывести вычитание переменных
    elif operation == "*": # если операции будет присвоина умножение
        print (firstnumber_num * secondnumber) # вывести умножение переменных
    elif operation == '/': # если операции будет присвоина деление
            if secondnumber != 0:
                print (firstnumber_num / secondnumber) # вывести деление переменных
            else:
                print("Деление на 0 невозможно!")
    elif operation  == '': 
        print (firstnumber_num   (secondnumber)) # вывести возведение в степень переменных
    elif operation == '%': 
        print (firstnumber_num % secondnumber)
    elif  operation == "синус" :
        print (math.sin (firstnumber_num))
    elif operation == 'косинус':
        print (math.cos(firstnumber_num))
    elif operation == 'таг':
        print (math.tan (firstnumber_num))
    elif operation == 'корень':
        print (firstnumber_num ** 0.5)
    elif operation == "факториал":
        print (math.factorial (firstnumber_num ))
    else: 
        print ("Ошибка")
    занова = input("Введите 'T' чтобы начать заново")
