
import json

student ={
    "name": "Jui",
    "age": 23,
    "Department": "Computer Science"
}

json_string = json.dumps(student)

print(json_string)