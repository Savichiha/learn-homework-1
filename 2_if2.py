"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
a = input('Введите первую строку: ')
b = input('Введите вторую строку: ')

def proverka (a, b):
    if not isinstance(a, str) or not isinstance(b, str):
        return "0"
    if len(a) == len(b):
        return "1"
    if len(a) > len(b):
        return "2"
    if len(a) != len(b) and b == u'learn':
        return "3"
    else:
        return "4"
  
print(proverka (a, b))
    
if __name__ == "__main__":
    main()
