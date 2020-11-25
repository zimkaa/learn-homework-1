"""

Домашнее задание №1

Исключения: приведение типов

* Перепишите функцию discounted(price, discount, max_discount=20)
  из урока про функции так, чтобы она перехватывала исключения,
  когда переданы некорректные аргументы.
* Первые два нужно приводить к вещественному числу при помощи float(),
  а третий - к целому при помощи int() и перехватывать исключения
  ValueError и TypeError, если приведение типов не сработало.
    
"""

def discounted(price, discount, max_discount=20):
    """
    Замените pass на ваш код
    """
    try:
        price = abs(float(price))
    except (TypeError, ValueError):
        return "Передано не корректное значение price"
    try:
        discount = abs(float(discount))
    except (TypeError, ValueError):
        return "Передано не корректное значение discount"
    try:
        max_discount = abs(int(max_discount))
    except (TypeError, ValueError):
        return "Передано не корректное значение max_discount"
    if max_discount > 99:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount:
        return price
    else:
        return price - (price * discount / 100)


if __name__ == "__main__":
    print(discounted(100, 2))
    print(discounted(100, "3"))
    print(discounted("100", "4.5"))
    print(discounted("five", 5))
    print(discounted("сто", "десять"))
    print(discounted(100.0, 5, "10"))

    print("Мои условия")
    print(discounted(100.0, "five", "10"))
    print(discounted(100.0, 5, "10.7"))
    print(discounted(100.0, 5, "five"))
