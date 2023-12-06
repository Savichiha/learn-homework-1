"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user():
    """
    Замените pass на ваш код
    """
while True:
    hello_user = input('Как дела? ')
    if hello_user == 'Хорошо':
        print('Ну и славно!')
        break
    else:
        print(hello_user)
print('Пока!')

    
if __name__ == "__main__":
    hello_user()
