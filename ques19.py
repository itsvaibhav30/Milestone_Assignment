def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

from collections import Counter
import re
from file_operations import read_file

# Read the content of the file
file_path = 'paragraph.txt'
paragraph = read_file(file_path)

words=paragraph.split()
count=Counter(words)

sorted_count=dict(sorted(count.items()))
print(sorted_count)