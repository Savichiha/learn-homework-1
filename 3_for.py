"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
stock = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

for phone in stock:
    phone_name = phone["product"]
    summ_sold =sum(phone['items_sold'])
    print(f'Всего продано: {phone_name}: {summ_sold}')

for phone_avg in stock:
    phone_name = phone_avg["product"]
    avg_sold_phone = sum(phone_avg['items_sold']) / len(phone_avg['items_sold'])
    print(f'Средняя кол-во продаж: {phone_name}: {avg_sold_phone}')

all_ph = 0
for all_phones in stock:
    summ_sold =sum(phone['items_sold'])
    all_ph += summ_sold
print(f'Всего продано ед.: {all_ph}')

for sold_avg in stock:
    phone_name = sold_avg["product"]
    sold_avg_phone = sum(sold_avg['items_sold']) / len(sold_avg['items_sold'])
print(f'Средее количество продаж: {sold_avg_phone}')
    
if __name__ == "__main__":
    main()
