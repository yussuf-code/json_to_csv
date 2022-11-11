import json


def json_to_csv(json_file_name, csv_file_name):

    # getting json data in a list
    with open(json_file_name, "r") as json_file:
        data_list = json.load(json_file)

    # getting the headers from the data list
    headers_list = list(data_list[0].keys())
    csv_data = ','.join(headers_list)

    # getting the data from the data list
    for item in data_list:
        new_data_list = list(item.values())
        new_data_list_str = [str(x) for x in new_data_list]
        new_data_joined = '\n' + ','.join(new_data_list_str)
        csv_data += new_data_joined

    # creating the csv file
    with open(csv_file_name, 'w') as csv_file:
        csv_file.write(csv_data)