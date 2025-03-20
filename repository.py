import json 
import os 

FILE_PATH = r'C:\Users\cesar\OneDrive\Python\proyect_spences\db_expences.json'

def get_data() -> list:
    if not os.path.exists(FILE_PATH):
        print("El archivo no existe. Se creará uno nuevo con una tarea inicial.")
        new_task = input("Ingrese la descripción de la tarea: ")
        new_data = [{"id": 1, "description": new_task, "status": "pendiente"}]
        
        with open(FILE_PATH, 'w', encoding='utf-8') as file:
            json.dump(new_data, file, indent=4)
        
        return new_data
    
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Error al leer el archivo JSON. Se creará una nueva lista.")
        new_task = input("Ingrese la descripción de la tarea: ")
        new_data = [{"id": 1, "description": new_task, "status": "pendiente"}]
        
        with open(FILE_PATH, 'w', encoding='utf-8') as file:
            json.dump(new_data, file, indent=4)
        
        return new_data
    
    