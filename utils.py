import json 
import os 


DATA_FILE = 'data/students.json'

def load_students():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE,'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_students(students):
    with open(DATA_FILE,'w') as f:
        json.dump(students,f,indent=4)
