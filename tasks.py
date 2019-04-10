import math

def sectionBegin():
    print("\n\n\tСборник Begin")
    print("Доступно 13 из 40 программ")
    print("0 - выход из раздела")
    print("Введите номер программы: ", end="")
    choose = int(input())
    while ((choose<0)or(choose>13)):
        print("\nВы ввели неверное число!\nВыход в гл. меню - 0\nПовторите попытку: ", end="")
        choose = int(input())
    if (choose == 1):
        print("\n\nВведите сторону квадрата a:", end="")
        num = int(input())
        print("P=4*a =", num*4, end="\n")
        sectionBegin()
    elif (choose == 2):
        print("\n\nВведите сторону квадрата a:", end="")
        num = int(input())
        print("S=a^2 =", num**2, end="\n")
        sectionBegin()
    elif (choose == 3):
        print("\n\nВведите стороны прямоугольника a и b")
        print("a:", end="")
        numA = int(input())
        print("b:", end="")
        numB = int(input())
        print("S=a*b =", numA*numB, " P=2*(a+b) =", 2*(numA+numB), end="\n")
        sectionBegin()
    elif (choose == 4):
        print("\n\nВведите диаметр окружности d:", end="")
        num = float(input())
        print("L=Pi*d =", math.pi*num, end="\n")
        sectionBegin()
    elif (choose == 5):
        print("\n\nВведите длину ребра куба a:", end="")
        num = int(input())
        print("V=a^3 =", num**3, "S=6*a^2 =",6*(num**2), end="\n")
        sectionBegin()
    elif (choose == 6):
        print("\n\nВведите длину ребер a,b,c")
        print("a:", end="")
        numA = int(input())
        print("b:", end="")
        numB = int(input())
        print("c:", end="")
        numC = int(input())
        print("S=2(ab+bc+ac) =", 2*((numA*numB)+(numB*numC)+(numA+numC)), end="\n")
        sectionBegin()
    elif (choose == 7):
        print("\n\nВведите радиус окружности R:", end="")
        num = float(input())
        print("L=2*Pi*R =", 2*math.pi*num, " S=Pi*R^2 =", math.pi*(num**2), end="\n")
        sectionBegin()
    elif (choose == 8):
        print("\n\nВведите a и b")
        print("a:", end="")
        numA = int(input())
        print("b:", end="")
        numB = int(input())
        print("Среднее арифм. =", (numA+numB)/2, end="\n")
        sectionBegin()
    elif (choose == 9):
        print("\n\nВведите 2 неотрицательных числа a и b")
        print("a: ", end="")
        numA = float(input())
        print("b: ", end="")
        numB = float(input())
        print("Корень из a*b =", math.sqrt(numA*numB), end="\n")
        sectionBegin()
    elif (choose == 10):
        print("\n\nВведите 2 не нулевых числа a,b")
        print("a: ", end="")
        numA = int(input())
        print("b: ", end="")
        numB = int(input())
        print("Сумма =", numA+numB, ", разность =", numA-numB, ", произведение =", numA*numB, ", частное их квадратов =", (numA**2)/(numB**2), end="\n")
        sectionBegin()
    elif (choose == 11):
        print("\n\nВведите 2 не нулевых числа a,b")
        print("a: ", end="")
        numA = int(input())
        print("b: ", end="")
        numB = int(input())
        print("Сумма =", numA+numB, ", разность =", numA-numB, ", произведение =", numA*numB, ", частное их модулей =", abs(numA)/abs(numB), end="\n")
        sectionBegin()
    elif (choose == 12):
        print("\n\nВведите катеты прямугольного треугольника")
        print("a: ", end="")
        numA = float(input())
        print("b: ", end="")
        numB = float(input())
        print("c=кв.корень из a^2+b^2 =", math.sqrt((numA**2)+(numB**2)), ", P=a+b+c =", numA+numB+(math.sqrt((numA**2)+(numB**2))), end="\n")
        sectionBegin()
    elif (choose == 13):
        print()
        sectionBegin()
    elif (choose == 0):
        print("\n\tВыход в гл. меню\n")
        mainChoose()

def sectionInteger():
    print("\n\nСборник Integer")
    print("Доступно 1 из 30 программ")
    print("0 - выход из раздела")
    print("Введите номер программы: ", end="")
    choose = int(input())
    while ((choose<0)or(choose>1)):
        print("\nВы ввели неверное число!\nВыход в гл. меню - 0\nПовторите попытку: ", end="")
        choose = int(input())
    if (choose == 1):
        print("\n\nВведите расстояние L в сантиметрах")
        print("L:", end="")
        num = int(input())
        print("В метрах: ", num/100, end="\n")
        sectionInteger()
    elif (choose == 0):
        print("\n\tВыход в гл. меню\n")
        mainChoose()

def sectionBoolean():
    print("\n\nСборник Boolean")
    print("Доступно 9 из 40 программ")
    print("0 - выход из раздела")
    print("Введите номер программы: ", end="")
    choose = int(input())
    while ((choose<0)or(choose>9)):
        print("\nВы ввели неверное число!\nВыход в гл. меню - 0\nПовторите попытку: ", end="")
        choose = int(input())
    if (choose == 1):
        print("\n\nДано число:", end="")
        num = int(input())
        print("Проверить, явл. число положительным?")
        if (num>0):
            print("Является!", end="\n")
        else:
            print("Число отрицательное!", end="\n")
        sectionBoolean()
    elif (choose == 2):
        print("\n\nДано число:", end="")
        num = int(input())
        print("Проверить, явл. число нечетным?")
        if ((num%2)==1):
            print("Число нечетное!", end="\n")
        else:
            print("Число четное!", end="\n")
        sectionBoolean()
    elif (choose == 3):
        print("\n\nДано число:", end="")
        num = int(input())
        print("Проверить, явл. число четным?")
        if ((num%2)==0):
            print("Число четное!", end="\n")
        else:
            print("Число нечетное!", end="\n")
        sectionBoolean()
    elif (choose == 4):
        print("\n\nВведите целые числа A и B")
        print("A:", end="")
        numA = int(input())
        print("B:", end="")
        numB = int(input())
        print("Справедливы неравенства A>2 и B<=3 ?")
        if ((numA>2)and(numB<=3)):
            print("Все верно!", end="\n")
        else:
            print("Числа не подходят!", end="\n")
        sectionBoolean()
    elif (choose == 5):
        print("\n\nВведите целые числа A и B")
        print("A:", end="")
        numA = int(input())
        print("B:", end="")
        numB = int(input())
        print("Справедливы неравенства A>=0 и B<=-2 ?")
        if ((numA>=0)and(numB<=-2)):
            print("Все верно!", end="\n")
        else:
            print("Числа не подходят!", end="\n")
        sectionBoolean()
    elif (choose == 6):
        print("\n\nВведите целые числа A,B,C")
        print("A:", end="")
        numA = int(input())
        print("B:", end="")
        numB = int(input())
        print("C:", end="")
        numC = int(input())
        print("Справедливо неравенство A<B<C ?")
        if ((numA<numB)and(numB<numC)and(numA<numC)):
            print("Все верно!", end="\n")
        else:
            print("Числа не подходят!", end="\n")
        sectionBoolean()
    elif (choose == 7):
        print("\n\nВведите целые числа A,B,C")
        print("A:", end="")
        numA = int(input())
        print("B:", end="")
        numB = int(input())
        print("C:", end="")
        numC = int(input())
        print("Число B находится между числами A и C ?")
        if (((numA<numB)and(numB<numC)and(numA<numC))or((numA>numB)and(numB>numC)and(numA>numC))):
            print("Все верно!", end="\n")
        else:
            print("Числа не подходят!", end="\n")
        sectionBoolean()
    elif (choose == 8):
        print("\n\nДаны 2 целых числа A,B")
        print("A:", end="")
        numA = int(input())
        print("B:", end="")
        numB = int(input())
        print("Истенно ли высказывание - A и B нечетное?")
        if (((numA%2)==1)and((numB%2)==1)):
            print("Оба числа нечетные!", end="\n")
        else:
            print("Хотя бы одно число четное.", end="\n")
        sectionBoolean()
    elif (choose == 9):
        print("\n\nДаны 2 целых числа A,B")
        print("A:", end="")
        numA = int(input())
        print("B:", end="")
        numB = int(input())
        print("Истенно ли высказывание - хотя бы из чисел A и B нечетное?")
        if (((numA%2)==1)or((numB%2)==1)):
            print("Хотя бы одно число нечетное!", end="\n")
        else:
            print("Все числа четные!", end="\n")
        sectionBoolean()
    elif (choose == 0):
        print("\n\tВыход в гл. меню\n")
        mainChoose()

def sectionIF():
    print("\n\nСборник IF")
    print("Доступно 0 из 30 программ")
    print("0 - выход из раздела")
    print("Введите номер программы: ", end="")
    choose = int(input())
    while ((choose<0)or(choose>=1)):
        print("\nВы ввели неверное число!\nВыход в гл. меню - 0\nПовторите попытку: ", end="")
        choose = int(input())
    if (choose == 1):
        print("\n\n")
        
        sectionIF()
    elif (choose == 0):
        print("\n\tВыход в гл. меню\n")
        mainChoose()

def sectionCase():
    print("\n\nСборник Case")
    print("Доступно 0 из 20 программ")
    print("0 - выход из раздела")
    print("Введите номер программы: ", end="")
    choose = int(input())
    while ((choose<0)or(choose>=1)):
        print("\nВы ввели неверное число!\nВыход в гл. меню - 0\nПовторите попытку: ", end="")
        choose = int(input())
    if (choose == 1):
        print("\n\n")
        
        sectionCase()
    elif (choose == 0):
        print("\n\tВыход в гл. меню\n")
        mainChoose()

def sectionFor():
    print("\n\nСборник For")
    print("Доступно 0 из 40 программ")
    print("0 - выход из раздела")
    print("Введите номер программы: ", end="")
    choose = int(input())
    while ((choose<0)or(choose>=1)):
        print("\nВы ввели неверное число!\nВыход в гл. меню - 0\nПовторите попытку: ", end="")
        choose = int(input())
    if (choose == 1):
        print("\n\n")
        
        sectionFor()
    elif (choose == 0):
        print("\n\tВыход в гл. меню\n")
        mainChoose()

def sectionWhile():
    print("\n\nСборник While")
    print("Доступно 0 из 30 программ")
    print("0 - выход из раздела")
    print("Введите номер программы: ", end="")
    choose = int(input())
    while ((choose<0)or(choose>=1)):
        print("\nВы ввели неверное число!\nВыход в гл. меню - 0\nПовторите попытку: ", end="")
        choose = int(input())
    if (choose == 1):
        print("\n\n")
        
        sectionWhile()
    elif (choose == 0):
        print("\n\tВыход в гл. меню\n")
        mainChoose()

def mainChoose():
    print("\tСборник программ")
    print("Доступен ? разделов, 0 - выход")
    print("1 - Begin")
    print("2 - Integer")
    print("3 - Boolean")
    print("4 - IF")
    print("5 - Case")
    print("6 - For")
    print("7 - While")
    print("Введите номер раздела: ", end="")
    selectMain = int(input())
    while ((selectMain<0)or(selectMain>=8)):
        print("Вы ввели неверное число!\nПовторите попытку: ", end="")
        selectMain = int(input())
    if (selectMain == 1):
        sectionBegin()
    elif (selectMain == 2):
        sectionInteger()
    elif (selectMain == 3):
        sectionBoolean()
    elif (selectMain == 4):
        sectionIF()
    elif (selectMain == 5):
        sectionCase()
    elif (selectMain == 6):
        sectionFor()
    elif (selectMain == 7):
        sectionWhile()
    elif (selectMain == 0):
        print("\nВыход из программы!")

# Общее кол-во готовых задач - 22 из 230
def perReady():
    numCompletTask = 22
    totalTask = 230
    perCompleteTask = (numCompletTask * 100)/totalTask
    print("\n\t Program ready at\n\t",perCompleteTask, "%\n")

perReady()
mainChoose()