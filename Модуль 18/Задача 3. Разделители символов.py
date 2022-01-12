text = input("Введите шаблон поздравления, в шаблоне можно использовать конструкцию {name} и {age}: ")
name_list = input("Список людей через запятую: ").split(",")
age_list = input("Возраст людей через пробел: ").split()

people = [
            " ".join([name_list[i_man], str(age_list[i_man])])
          for i_man in range(len(name_list))]

people_str = ", ".join(people)
print('\nИменинники:', people_str)
