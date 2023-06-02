from tkinter import *
nuatgeral = 0
nuc = 0
# Funções 
def atendimentogeral():
    root2 = Toplevel(root)
    root2.title("Atendimento Geral")
    root2.geometry("300x300")
    root2.resizable(False,False)
    root2.configure(background="black")
    text = Label(root2, text='Atendimento Geral', font=("Ariel", "15",'bold'),
                 fg="white", bg="black")
    text.place(relx=0.2, rely=0.05)
    textClick = Label(root2, text=0, font=("Ariel", "70"), fg="red", bg="black")
    textClick.place(relx=0.35,rely=0.2)
    global nuatgeral
    nuatgeral += 1
    if nuatgeral == 100:
        nuatgeral = 0
    textClick.config(text=nuatgeral)
    root2.after(3000, lambda: root2.destroy()) # Fechar a Janela de Forma automática
def cobranca():
    root3 = Toplevel(root)
    root3.title("Cobrança")
    root3.geometry("300x300")
    root3.resizable(False, False)
    root3.configure(background="black")
    text = Label(root3, text='Cobrança', font=("Ariel", "15", 'bold'),
                 fg="white", bg="black")
    text.place(relx=0.4, rely=0.05)
    textClick = Label(root3, text=0, font=("Ariel", "70"),
                      fg="red", bg="black")
    textClick.place(relx=0.45, rely=0.2)
    global nuc
    nuc += 1
    if nuc == 100:
        nuc = 0
    textClick.config(text=nuc)
    root3.after(3000, lambda: root3.destroy())  # Fechar a Janela de Forma automática depois de 3 segundos
root = Tk()
root.title("Tirar Senha")
root.geometry("250x200")
root.configure(background="black")
root.resizable(False,False)
at = Button(root, text="Atendimento Geral",command=atendimentogeral) # Butão de Atendimento
at.place(relx=0.25,rely=0.15)
cob = Button(root, text="Cobrança", command=cobranca) # Butão de Cobrança
cob.place(relx=0.4,rely=0.45)
root.mainloop()