# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида «10.25%».
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

name_list = ['Иван', 'Петр', 'Николай']
salary_list = [30000, 45000, 60000]
bonus_list = ['10.5%', '13.2%', '17%']

def create_bonus_list(name: str, salary: int, bonus: str) -> dict[str, float]:
    return {item[0]: item[1] / 100 * float(item[2][:-1]) for item in zip(name, salary, bonus)}

print(create_bonus_list(name_list, salary_list, bonus_list))