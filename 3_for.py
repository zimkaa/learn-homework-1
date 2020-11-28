"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    school = [{'school_class': '4a', 'scores': [3,4,4,5,2]},
        {'school_class': '5a', 'scores': [3,4,2,3,2]},
        {'school_class': '6a', 'scores': [3,5,5,5,2]},
        {'school_class': '7a', 'c': [4,4,4,5,3]}]
    
    all_average_score = 0
    for score_class in school:
        all_mark = 0
        for score in score_class["scores"]:
            all_mark += score
        average_score = all_mark/len(score_class['scores'])
        print(f"Средний балл по {score_class['school_class']} классу = {average_score}")
        all_average_score += average_score

    # дописать 
    for mark in school:
        all_average_score += mark[scores]


    print(f"Средний балл по всей школе = {all_average_score/(len(school))}")

    
if __name__ == "__main__":
    main()
