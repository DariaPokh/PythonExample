path = input("Введите путь к файлу: ")

if not path.endswith(".txt"):
    print("Ошибка: неверное расширение файла.")
elif not path.startswith("C:/"):
    print("Ошибка: неверно указан диск.")
else:
    print("Путь к файлу: ", path)
    print("На каком диске должен лежать файл:", path[0])
    print("Требуемое расширение файла:", path[-4:])
    print("Путь корректен!")

