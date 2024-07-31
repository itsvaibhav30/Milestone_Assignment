from file_operations import read_file, write_file, append_file

file_path = 'hello.txt'

write_file(file_path, 'Hello, World!')

print("Read from file:", read_file(file_path))

# Append data to the file
append_file(file_path, '\nThis is an appended line.')

# Read data again to see the appended content
print("Read from file after appending:", read_file(file_path))
