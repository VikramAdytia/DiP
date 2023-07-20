def generate_salary_dict(names_list, salaries_list, bonuses_list):
    yield {name: salary * (1 + float(bonus.strip('%')) / 100) for name, salary, bonus in zip(names_list, salaries_list, bonuses_list)}

names = ["Louie", "Dewey", "Huey"]
salaries = [10000, 15000, 20000]
bonuses = ["10.25%", "15.15%", "20.2%"]

salary_dict = generate_salary_dict(names, salaries, bonuses)
print(*salary_dict)