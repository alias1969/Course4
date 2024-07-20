import src.utils as utils

def main():
    """ Запуск программы """

    user_input = input("Здравствуйте!\n"
                       "Вы хотите считать вакансии в файл? [yes/no]\n").lower().strip()

    # Пользователь выбрал получить файл с данными с сайта
    if user_input == "yes":
        utils.data_sampling()

        type_file = input("Выберите формат файла: [json/txt/csv]").lower().strip()

        if type_file == 'json':
            utils.data_sampling()

        elif type_file == 'txt':
            print('К сожалению, работа с файлами в формате TXT еще не реализован')

        elif type_file == 'csv':
            print('К сожалению, работа с файлами в формате CSV еще не реализован')
        else:
            print('Выбран неизвестный формат файла')

    elif:
        user_input = input("Вы хотите отчистить файл [yes/no]?\n")
        #
        if user_input == "yes":
            file = FileWorkerJson(FILE_VACANCIES)
            file.del_data()
            print("Данные удалены!")

    return



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
