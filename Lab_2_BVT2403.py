#Лебедева БВТ2403
#Лабораторная работа №2: Функции в Python и базовые алгоритмы

#Задача 1
def greet(name):
    return "Привет, " + name + "!"


print(greet("Лиза"))


def square(number):
    return number**2


print(square(4))


def max_of_two(x, y):
    return max(x, y)


print(max_of_two(-12345678, 123456))


#Задание 2
def describe_person(name, age=30):
    m = str(name) + ': ' + str(age)
    return m


print(describe_person("Петя"))
print(describe_person("Стёпа", 18))


#Задание 3
def is_prime(n):
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            return False
    return True


print(is_prime(7414))
print(is_prime(113))
