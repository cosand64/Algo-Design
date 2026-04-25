import json


def write_data_to_json_file(data, filename):
    '''Write the data contained in data to the file whose name 
    is finlename. Make sure to check and catch errors.'''

    try:
        with open (filename, 'wt') as filehandle:
            # json_data = json.dumps(data)
            # filehandle.write(json_data)
            json.dump(data, filehandle)


    except (FileExistsError, FileNotFoundError):
        print('File not found dummy')

def read_data_to_json_file(filename):
    '''Write the data contained in data to the file whose name 
    is finlename. Make sure to check and catch errors.'''

    try:
        with open (filename, 'rt') as filehandle:
            # json_data = filehandle.read()
            # dictionary_data = json.loads(json_data)
            dictionary_data = json.load(filehandle)

            return dictionary_data

    except (FileExistsError, FileNotFoundError):
        print('File not found dummy')

def calculate_debt(data):
    pass

def main():
    print('hey')
    my_friends = {
        'Name' : ['bob', 'betty', 'jeannie'],
        'phone numbers' : [208123, 123456, 676767],
        'Addresses' : ['address one', 'address two', 'address three'],
        'owe me': [123, 456, 789]
    }

    filename = 'myfriends.json'
    
    write_data_to_json_file(my_friends, filename)

    my_friends_data = read_data_to_json_file(filename)
    print(my_friends_data['Name'])

main()