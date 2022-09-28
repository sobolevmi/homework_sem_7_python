def export_data_from_file():
    """Функция по экспорту информации, содержащейся в телефонном справочнике, в другой файл"""
    with open("telephone_book.txt", "r") as a_file:
        with open("export_telephone_book.txt", "a") as b_file:
            for line in a_file:
                b_file.write(line)
            a_file.close()
            b_file.close()
    print("Ваши данные успешно экспортированы!")
