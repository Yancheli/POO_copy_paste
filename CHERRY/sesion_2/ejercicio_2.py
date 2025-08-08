subject = {
    "POO I": 'h12',
    "BASE DE DATOS": 'p18',
    "SISTEMAS OPERATIVOS": 'r96',
    "COMPILADORES": 'y85',
}

print("¿Que asignatura quieres consultar?")
      
user_Subj = str(input())

if user_Subj in subject:
    print(f"La asignatura {user_Subj} tiene el  código {subject[user_Subj]}")