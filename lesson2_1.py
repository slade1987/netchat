import os, re, csv

def get_data():
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]

    for root, dirs, files in os.walk(os.path.abspath("pars")):
        for filename in files:
            f = open(os.path.abspath("pars") + "\\" + filename, 'r')
            for line in f:
                if re.search('Изготовитель системы', line):
                    os_prod_list.append(line.split()[2])
                elif re.search('Название ОС', line):
                    os_name_list.append(line.split()[2])
                elif re.search('Код продукта', line):
                    os_code_list.append(line.split()[2])
                elif re.search('Тип системы', line):
                    os_type_list.append(line.split()[2])

    for i in range(len(os_type_list)):
        row_data = []
        row_data.append(os_prod_list[i])
        row_data.append(os_name_list[i])
        row_data.append(os_code_list[i])
        row_data.append(os_type_list[i])
        main_data.append(row_data)

    return main_data


def write_to_csv(file_name: str):
    main_date = get_data()
    myfile = open(file_name, 'w', newline='')

    with myfile:
        writer = csv.writer(myfile, delimiter=';')
        for row in main_date:
            writer.writerow(row)
