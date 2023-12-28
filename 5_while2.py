"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""
questions_and_answers = {}

def ask_user(answers_dict):
questions_and_answers = {'Как дела?': 'Хорошо!',
     'Что делаешь?': 'Читаю',
     'Что читаешь?': 'Виктор Пелевин'}

def ask_user(answers_dict):
    while True:
        question = input('Введите ваш вопрос: ')
        print(question)
        if question in answers_dict:
            print(answers_dict.get(question))
            break
        else:
            print('Я не знаю ответ на этот вопрос')

if __name__ == "__main__":
    ask_user(questions_and_answers)

    pass
    
if __name__ == "__main__":
    ask_user(questions_and_answers)
