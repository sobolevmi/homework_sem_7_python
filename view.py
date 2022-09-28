def view_file():
    """Функция по выводу информации, содержащейся в справочнике, в консоль"""
    print("Данные, имеющиеся в телефонном справочнике:\n")
    with open("telephone_book.txt", "r") as file:
        for line in file:
            print(str(line))