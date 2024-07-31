# file_operations.py

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def write_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write(data)

def append_file(file_path, data):
    with open(file_path, 'a') as file:
        file.write(data)
