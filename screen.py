from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

from PIL import ImageTk, Image

from tkcalendar import Calendar, DateEntry
from datetime import date

#importando main
from main import *

co0 = "#2e2d2b"  # preto
co1 = "#feffff"  # branco   
co2 = "#e5e5e5"  # cinza
co3 = "#00a095"  # verde
co4 = "#403d3d"   # letra
co6 = "#003452"   # azul
co7 = "#ef5350"   # vermelha

co6 = "#146C94"   # azul
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde

screen = Tk()
screen.title("")
screen.geometry("810x535")
screen.configure(background=co1)
screen.resizable(width=False, height=False)

style = Style(screen)
style.theme_use("clam")

frame_logo = Frame(screen, width=850, height=52, bg=co6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW, columnspan=5)

frame_buttons = Frame(screen, width=100, height=200, bg=co1, relief=RAISED)
frame_buttons.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_details = Frame(screen, width=800, height=100, bg=co1, relief=SOLID)
frame_details.grid(row=1, column=1, pady=1, padx=10, sticky=NSEW)

frame_table = Frame(screen, width=800, height=100, bg=co1, relief=SOLID)
frame_table.grid(row=3, column=0, pady=0, padx=10, sticky=NSEW, columnspan=5)

#frame_logo ------------------------------------------
global imagem, imagem_string, l_imagem

app_lg = Image.open("icons/logo.png")
app_lg = app_lg.resize((50,50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text="  Sistema de Registro Estudantil", width=850, compound=LEFT, anchor=NW, font=('Verdana 15'), bg=co6, fg=co1)
app_logo.place(x=5, y=0)

imagem = Image.open("icons/hat.png")
imagem = imagem.resize((130,130))
imagem = ImageTk.PhotoImage(imagem)
l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
l_imagem.place(x=390, y=10)
#----------------------------------------------------
#funções CRUD
#adicionar
def add():
    global imagem, imagem_string, l_imagem
    name = e_name.get()
    email = e_email.get()
    phone = e_phone.get()
    sex = c_sex.get()
    birth_date = birthday.get()
    address = e_address.get()
    course = c_course.get()
    picture = imagem_string

    data = [name, email, phone, sex, birth_date, address, course, picture]

    for i in data:
        if i == '':
            messagebox.showerror("Erro", "Por favor, preencha todos os campos!")
            return
    
    registration_system.register_student({
        'name': name,
        'email': email,
        'phone': phone,
        'sex': sex,
        'birthday': birth_date,
        'address': address,
        'course': course,
        'picture': picture
    })

    # limpando campos
    e_name.delete(0, END)
    e_email.delete(0, END)
    e_phone.delete(0, END)
    c_sex.set('')
    birthday.set_date(date.today())
    e_address.delete(0, END)
    c_course.set('')

    show_students()

#procurar
def search():
    global imagem, imagem_string, l_imagem

    id_student = int(e_search.get())
    data = registration_system.search_student(id_student)

    e_name.delete(0, END)
    e_email.delete(0, END)
    e_phone.delete(0, END)
    c_sex.set('')
    birthday.set_date(date.today())
    e_address.delete(0, END)
    c_course.set('')

    e_name.insert(END, data[1])
    e_email.insert(END, data[2])
    e_phone.insert(END, data[3])
    c_sex.set(data[4])
    birthday.set_date(data[5])
    e_address.insert(END, data[6])
    c_course.set(data[7])
    
    imagem = data[8]
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((130,130))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=390, y=10)

#atualizar
def update():
    global imagem, imagem_string, l_imagem
    id_student = int(e_search.get())

    name = e_name.get()
    email = e_email.get()
    phone = e_phone.get()
    sex = c_sex.get()
    birth_date = birthday.get()
    address = e_address.get()
    course = c_course.get()
    picture = imagem_string

    data = [name, email, phone, sex, birth_date, address, course, picture]

    for i in data:
        if i == '':
            messagebox.showerror("Erro", "Por favor, preencha todos os campos!")
            return

    update_data = [name, email, phone, sex, birth_date, address, course, picture, id_student]

    registration_system.update_student(update_data)

    # limpando campos
    e_name.delete(0, END)
    e_email.delete(0, END)
    e_phone.delete(0, END)
    c_sex.set('')
    birthday.set_date(date.today())
    e_address.delete(0, END)
    c_course.set('')

    imagem = Image.open("icons/hat.png")
    imagem = imagem.resize((130,130))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem.configure(image=imagem)
    l_imagem.image = imagem

    show_students()

#deletar
def delete():
    global imagem, imagem_string, l_imagem
    id_student = int(e_search.get())

    registration_system.delete_student(id_student)

    # limpando campos
    e_name.delete(0, END)
    e_email.delete(0, END)
    e_phone.delete(0, END)
    c_sex.set('')
    birthday.set_date(date.today())
    e_address.delete(0, END)
    c_course.set('')

    e_search.delete(0,END)

    imagem = Image.open("icons/hat.png")
    imagem = imagem.resize((130,130))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem.configure(image=imagem)
    l_imagem.image = imagem

    show_students()


#campos de entrada -----------------------------------

l_name =Label(frame_details, text="Nome:", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_name.place(x=4, y=10)
e_name = Entry(frame_details, width=30, justify='left', relief=SOLID)
e_name.place(x=7, y=40)

l_email =Label(frame_details, text="Email:", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_email.place(x=4, y=70)
e_email = Entry(frame_details, width=30, justify='left', relief=SOLID)
e_email.place(x=7, y=100)

l_phone =Label(frame_details, text="Telefone:", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_phone.place(x=4, y=130)
e_phone = Entry(frame_details, width=15, justify='left', relief=SOLID)
e_phone.place(x=7, y=160)

l_sex =Label(frame_details, text="Gênero:", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_sex.place(x=127, y=130)
c_sex = ttk.Combobox(frame_details, width=7, font=('Ivy 8 bold'), justify='center')
c_sex['values'] = ('Masculino', 'Feminino')
c_sex.place(x=130, y=160)

l_birthday =Label(frame_details, text="Data de Nascimento:", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_birthday.place(x=229, y=10)
birthday = DateEntry(frame_details, width=18, justify='center', background='darkblue',foreground='white', borderwidth=2, year=2023)
birthday.place(x=224, y=40)

l_address =Label(frame_details, text="Endereço:", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_address.place(x=220, y=70)
e_address = Entry(frame_details, width=20, justify='left', relief=SOLID)
e_address.place(x=224, y=100)

cursos = ["Administração","Direito","Medicina","Enfermagem","Psicologia","Engenharia Civil","Engenharia da Computação","Engenharia Elétrica","Ciência da Computação","Sistemas de Informação","Análise e Desenvolvimento de Sistemas","Arquitetura e Urbanismo","Design Gráfico","Educação Física","Pedagogia","Biomedicina","Farmácia","Jornalismo","Publicidade e Propaganda","Contabilidade"]

l_course =Label(frame_details, text="Curso:", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_course.place(x=220, y=130)
c_course = ttk.Combobox(frame_details, width=20, font=('Ivy 8'))
c_course['values'] = cursos
c_course.place(x=224, y=160)

# escolher a imagem ---------------------------

def choose_image():
    global imagem, imagem_string, l_imagem

    imagem = fd.askopenfilename()
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((130,130))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=390, y=10)

    button_load['text']= 'Trocar foto '

button_load = Button(frame_details, command=choose_image, text='Carregar foto'.upper(), width=20, compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0)
button_load.place(x=390, y=160)

# tabela de alunos ----------------------------------

def show_students():

    list_header = ['ID', 'Nome', 'Email', 'Telefone', 'Gênero', 'Data de Nascimento', 'Endereço', 'Curso']
    df_list = registration_system.view_all_students()

    tab_student = ttk.Treeview(frame_table, selectmode="extended", columns=list_header, show='headings')

    vsb = ttk.Scrollbar(frame_table, orient="vertical", command=tab_student.yview)
    hsb = ttk.Scrollbar(frame_table, orient="horizontal", command=tab_student.xview)

    tab_student.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tab_student.grid(column=0, row=1, sticky='nsew')
    vsb.grid(column=1, row=1, sticky='ns')
    hsb.grid(column=0, row=2, sticky='ew')
    frame_table.grid_rowconfigure(0, weight=12)

    hd = ["nw", "nw", "nw", "center", "center", "center", "center", "center", "center"]
    h=[40,150,150,70,70,120,100,100]
    n=0

    for col in list_header:
        tab_student.heading(col, text=col.title(), anchor=NW)
        tab_student.column(col, width=h[n], anchor=hd[n])

        n+=1
    for item in df_list:
        tab_student.insert('', 'end', values=item)

#procurar aluno --------------------------------------

frame_search = Frame(frame_buttons, width=40, height=50, bg=co1, relief=RAISED)
frame_search.grid(row=0, column=0, pady=10, padx=10, sticky=NSEW)
l_name =Label(frame_search, text="Procurar aluno [ID]", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_name.grid(row=0, column=0, pady=10, padx=0, sticky=NSEW)
e_search = Entry(frame_search, width=5, justify=CENTER, relief=SOLID, font=('Ivy 10'))
e_search.grid(row=1, column=0, pady=10, padx=0, sticky=NSEW)
button_search = Button(frame_search, command=search, text='Procurar', width=9, anchor=CENTER, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0)
button_search.grid(row=1, column=1, pady=10, padx=0, sticky=NSEW)

# botoes adicionar / atualizar / deletar --------------------------

app_add_image = Image.open("icons/add.png")
app_add_image = app_add_image.resize((25,25))
app_add_image = ImageTk.PhotoImage(app_add_image)
button_add_img = Button(frame_buttons, command=add, image=app_add_image, relief=GROOVE, text=' Adicionar', width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
button_add_img.grid(row=1, column=0, pady=5, padx=10, sticky=NSEW)

app_update_image = Image.open("icons/update.png")
app_update_image = app_update_image.resize((25,25))
app_update_image = ImageTk.PhotoImage(app_update_image)
button_update_img = Button(frame_buttons, command=update, image=app_update_image, relief=GROOVE, text=' Atualizar', width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
button_update_img.grid(row=2, column=0, pady=5, padx=10, sticky=NSEW)

app_delete_image = Image.open("icons/remove.png")
app_delete_image = app_delete_image.resize((25,25))
app_delete_image = ImageTk.PhotoImage(app_delete_image)
button_delete_img = Button(frame_buttons, command=delete, image=app_delete_image, relief=GROOVE, text=' Deletar', width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
button_delete_img.grid(row=3, column=0, pady=5, padx=10, sticky=NSEW)

#-----------------------------------------------------------------------

l_line = Label(frame_buttons, relief=GROOVE, width=1, height=104, anchor=NW, font=('Ivy 1'), bg=co0, fg=co0)
l_line.place(x=197, y=15)


show_students()
screen.mainloop()