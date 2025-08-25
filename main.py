import sqlite3
from tkinter import messagebox

class RegistrationSystem:
    def __init__(self):
        self.conn = sqlite3.connect('students.db')
        self.c = self.conn.cursor()
        self.create_table()
    
    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS students(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     name TEXT NOT NULL,
                     email TEXT NOT NULL,
                     phone TEXT NOT NULL,
                     sex TEXT NOT NULL,
                     birthday TEXT NOT NULL,
                     address TEXT NOT NULL,
                     course TEXT NOT NULL,
                     picture TEXT NOT NULL)''')

    def register_student(self, students):
        self.c.execute("INSERT INTO students(name, email, phone, sex, birthday, address, course, picture) VALUES (?,?,?,?,?,?,?,?)", (students['name'], students['email'], students['phone'], students['sex'], students['birthday'], students['address'], students['course'], students['picture']))
        self.conn.commit()

        messagebox.showinfo("Successo", "Estudante registrado com sucesso!")

    def view_all_students(self):
        self.c.execute("SELECT * FROM students")
        data = self.c.fetchall()
        return data

    def search_student(self, id):
        self.c.execute("SELECT * FROM students WHERE id=?", (id,))
        data = self.c.fetchone()
        return data

    def update_student(self, update_data):
        query = "UPDATE students SET name=?, email=?, phone=?, sex=?, birthday=?, address=?, course=?, picture=? WHERE id=?"
        self.c.execute(query, update_data)
        self.conn.commit()
        messagebox.showinfo("Sucesso", f"Dados do estudante ID:{update_data[8]} foram atualizados!")
    
    def delete_student(self, id):
        self.c.execute("DELETE FROM students WHERE id=?", (id,))
        self.conn.commit()
        messagebox.showinfo("Sucesso", f"Estudante ID:{id} foi deletado com sucesso!")

# instancia de registros
registration_system = RegistrationSystem()

# teste informacoes
# estudante = {
#     'name': 'Helena Pinto',
#     'email': 'helena.pinto@example.com',
#     'phone': '12345678',
#     'sex': 'F',
#     'birthday': '07/09/2003',
#     'address': 'Cariacica, ES',
#     'course': 'Jornalismo',
#     'picture': 'image2.png'
# }
# registration_system.register_student(estudante)

# # ver todos os estudantes
# all_students = registration_system.view_all_students() 

# # pesquisar aluno
# aluno = registration_system.search_student(3)

# # atualizar aluno
# estudante = ( 'Helena Pinto', 'helena.pinto@example.com', '22225555', 'F', '07/09/2003', 'Angola, Luanda', 'Jornalismo', 'image2.png', 2)
# aluno = registration_system.update_student(estudante)

#deletar aluno
#registration_system.delete_student(6)