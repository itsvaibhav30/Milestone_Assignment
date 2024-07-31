from file_operations import write_file

employees=[
    {"name":"Vaibhav","age":22,"role":"Data Scientist"},
    {"name":"Apurv","age":22,"role":"Full Stack Dev"},
    {"name":"Raj","age":21,"role":"Frontend Dev"}
]

employee_details = "\n".join([f"Name: {emp['name']}, Age: {emp['age']}, Role: {emp['role']}" for emp in employees])

filename="employee.txt"
write_file(filename,employee_details)