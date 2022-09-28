import import_data
import export_data
import view

choice_menu = " "
while choice_menu != "4":
    choice_menu = str(input("Телефонный справочник\n"
                        "Если вы хотите добавить контакт, нажмите 1\n"
                        "Если вы хотите просмотреть содержимое справочника, нажмите 2\n"
                        "Если вы хотите экспортировать данные из справочника, нажмите 3\n"
                        "Если вы хотите завершить работу программы, нажмите 4\n"))
    if choice_menu == "1":
        import_data.add_data_to_file()
        print(choice_menu)
    if choice_menu == "2":
        view.view_file()
        print(choice_menu)
    if choice_menu == "3":
        export_data.export_data_from_file()
        print(choice_menu)
    if choice_menu == "4":
        break