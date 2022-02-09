from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import left, width
from Itens import Itens
from Banco import BancoItens

# Função para esconder os widgets
def hide_button(widget):
    widget.pack_forget()

#Função para mostrar os widgets
def show_button(widget):
    widget.pack()

class Organizador:

    def __init__(self, master=None):
        self.container = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17",
                          "18", "19", "20"]

        self.container[0] = Frame(master)
        self.container[0]["pady"] = 10
        self.container[0].pack()
        self.container[1] = Frame(master)
        self.container[1]["padx"] = 20
        self.container[1]["pady"] = 5
        self.container[1].pack()
        self.container[2] = Frame(master)
        self.container[2]["padx"] = 20
        self.container[2]["pady"] = 8
        self.container[2].pack()
        self.container[3] = Frame(master)
        self.container[3]["padx"] = 20
        self.container[3]["pady"] = 5
        self.container[3].pack()
        self.container[4] = Frame(master)
        self.container[4]["padx"] = 20
        self.container[4]["pady"] = 5
        self.container[4].pack()

        #self.sla = ["Residencial", "Comercial", "Personalizado"]

        self.nome = Label(self.container[1], text="Clique abaixo para criar uma nova configuração")
        self.nome.pack()

        self.nome = Label(self.container[0], text="SISTEMA DE GERENCIAMENTO")
        self.nome.pack()

        self.botao = Button(self.container[2], text="Novo", width=10, command=lambda: self.novaconf())
        self.botao.pack(side=TOP)

    '''Após o botão "Novo" ser apertado, essa função irá criar widgets para o usuário interagir
    e criar o botão com o nome que o usuário escolher,sendo possível criar vários botões(listas) 
    para uma melhor organização dos itens'''

    def novaconf(self):
        hide_button(self.botao)
        self.entrada = Entry(self.container[1])
        self.entrada.place(x=0, y=80, width=200, height=20)
        self.entrada.pack(side=BOTTOM)

        self.save = Button(self.container[2], text="Salvar")
        self.save.bind("<ButtonRelease>", self.salva_config)
        self.save.pack(side=BOTTOM)

    '''inicialmente a função vai checar se o usuario digitou alguma palavra, senão digita ele dá um aviso
        e retornar à função anterior. Caso tenha digitado, ele irá criar o botão normalmente'''
    def salva_config(self, event1):
        if not self.entrada.get():
            hide_button(self.entrada)
            hide_button(self.save)
            self.lb_aviso = Label(self.container[3], text="Digite uma palavra", fg="Red")
            self.lb_aviso.pack(side=LEFT)
            self.botão_retorno = Button(self.container[3], text=("Retornar"))
            self.botão_retorno.bind("<Button-1>", self.novaconf_Hidden)
            self.botão_retorno.pack(side=LEFT)
        else:
            self.arquivo()
            hide_button(self.entrada)
            hide_button(self.save)
            show_button(self.botao)
            self.conf = Button(self.container[4], text=self.entrada.get())
            self.conf.bind("<Button-1>", self.confg)
            self.conf.pack(side=TOP)

    # função necessária para esconder os botões de aviso da condição anterior e retornar
    # à função "novaconf()"
    def novaconf_Hidden(self, event2):
        hide_button(self.lb_aviso)
        hide_button(self.botão_retorno)
        self.novaconf()

    # Cria um arquivo txt que irá guardar as informações (incompleto)
    def arquivo(self):
        with open("{}.txt".format(self.entrada.get()), "a") as arquivo:
            arquivo.write("Configuração: {} ".format(self.entrada.get()))


    ''' Após criar um botão com as funções anteriores, essa função irá abrir uma nova janela
        onde de fato vamos adicionar os itens'''
    def confg(self, event3):
        janela2 = Tk()
        janela2.title("Itens")
        janela2.geometry("700x650")
        janela2.minsize(585,400)

        self.container[5] = Frame(janela2)
        self.container[5]["padx"] = 20
        self.container[5]["pady"] = 5
        self.container[5].pack()
        self.container[6] = Frame(janela2)
        self.container[6]["padx"] = 20
        self.container[6]["pady"] = 5
        self.container[6].pack()
        self.container[7] = Frame(janela2)
        self.container[7]["padx"] = 20
        self.container[7]["pady"] = 5
        self.container[7].pack()
        self.container[8] = Frame(janela2)
        self.container[8]["padx"] = 20
        self.container[8]["pady"] = 5
        self.container[8].pack()
        self.container[9] = Frame(janela2)
        self.container[9]["padx"] = 20
        self.container[9]["pady"] = 5
        self.container[9].pack()
        self.container[10] = Frame(janela2)
        self.container[10]["padx"] = 20
        self.container[10]["pady"] = 5
        self.container[10].pack()
        self.container[11] = Frame(janela2)
        self.container[11]["padx"] = 20
        self.container[11]["pady"] = 5
        self.container[11].pack()

        self.quadro = LabelFrame(self.container[5], text = "Lista de Itens", borderwidth = 10, height=10)
        self.quadro.pack(fill="both", expand="no", padx=10,pady=10)
        self.quadro3 = LabelFrame(self.container[5], text = "Opções", borderwidth = 5, height=10)
        self.quadro3.pack(fill="both", expand="yes", padx=10,pady=10)

        self.grade = ttk.Treeview(self.quadro,
                                  columns=('id', 'produto', 'quantidade', 'especificação', 'valor', 'limite'),
                                  show='headings')
        self.grade.column('id', minwidth=0, width=50)
        self.grade.column('quantidade', minwidth=0, width=100)
        self.grade.column('produto', minwidth=0, width=120)
        self.grade.column('valor', minwidth=0, width=80)
        self.grade.column('especificação', minwidth=0, width=100)
        self.grade.column('limite', minwidth=0, width=150)
        self.grade.heading('id', text="ID")
        self.grade.heading('quantidade', text="Quantidade")
        self.grade.heading('produto', text="Produto")
        self.grade.heading('valor', text="Preço")
        self.grade.heading('especificação', text="Categoria")
        self.grade.heading('limite', text="Limite Mínimo")
        self.grade.pack()

        
        self.botao_falta = Button(self.quadro3, text="Itens Faltando",
                           command=lambda: self.itens_faltando())
        self.botao_falta.pack(side=RIGHT)

        self.botao_mod = Button(self.quadro3, text="Modifique",
                           command=lambda: self.modificar())
        self.botao_mod.pack(side=RIGHT)

        self.dele = Button(self.quadro3, text="Delete",
                           command=lambda: [self.deletar()])
        self.dele.pack(side=RIGHT)

        self.inserir2 = Button(self.quadro3, text="Insira",
                               command=lambda: [hide_button(self.quadro3),hide_button(self.botao_mod),hide_button(self.botao_falta),hide_button(self.inserir2), hide_button(self.dele),
                                                self.inserir()])
        self.inserir2.pack(side=RIGHT)

    
        #Laço para inserir ao treeview os itens do banco ao abrir a janela2
        tabelaBanco = Itens.populaItens()
        for i in tabelaBanco:
            self.grade.insert("", "end", value=i)

        janela2.mainloop()

    def inserir(self):
        self.quadro2 = LabelFrame(self.container[6], text = "Insira seu Item")
        self.quadro2.pack(fill="both", expand="yes", padx=10,pady=10)

        self.lbl = Label(self.quadro2, text="Insira o nome do item")
        self.lbl.pack(side=TOP)
        self.item = Entry(self.quadro2)
        self.item.pack(side=TOP)

        self.lbl2 = Label(self.quadro2, text="Insira a quantidade")
        self.lbl2.pack(side=TOP)
        self.itemQuant = Spinbox(self.quadro2, from_=0, to=999, wrap=True)
        self.itemQuant.pack(side=TOP)

        self.lbl3 = Label(self.quadro2, text="Insira a categoria")
        self.lbl3.pack(side=TOP)
        self.itemCategoria = Entry(self.quadro2)
        self.itemCategoria.pack(side=TOP)

        self.lbl4 = Label(self.quadro2, text="Insira o preço")
        self.lbl4.pack(side=TOP)
        self.itemPreco = Entry(self.quadro2)
        self.itemPreco.pack(side=TOP)

        self.lbl5 = Label(self.quadro2, text="Insira limite")
        self.lbl5.pack(side=TOP)
        self.itemLimite = Entry(self.quadro2)
        self.itemLimite.pack(side=TOP)

        self.inserir1 = Button(self.quadro2, text="Inserir",
                               command=lambda: [show_button(self.quadro3),show_button(self.botao_falta),show_button(self.botao_mod),show_button(self.dele),show_button(self.inserir2),
                                                hide_button(self.quadro2),self.arquivo1(), self.lbl.pack_forget(), self.lbl2.pack_forget(),
                                                self.lbl3.pack_forget(), self.lbl4.pack_forget(),
                                                self.lbl5.pack_forget(), self.item.pack_forget(),
                                                self.itemQuant.pack_forget(), self.itemCategoria.pack_forget(),
                                                self.itemPreco.pack_forget(), self.itemLimite.pack_forget(),
                                                hide_button(self.inserir1),
                                                self.novalista()])
        self.inserir1.pack(side=TOP)

    def arquivo1(self):
        with open("{}.txt".format(self.entrada.get()), "a") as arquivo:
            arquivo.write("\n" + self.itemQuant.get() + " unidade(s)")
            arquivo.write(" || " + self.item.get())
            arquivo.write(" ||  R$ " + self.itemPreco.get())
            arquivo.write(" || " + " Categoria: " + self.itemCategoria.get())
            arquivo.write(" || " + " Limite: " + self.itemLimite.get() + "\n")

    def novalista(self):
        Itens.insertItem(self.item.get(), self.itemQuant.get(), self.itemCategoria.get(), self.itemPreco.get(), self.itemLimite.get())
        self.grade.delete(*self.grade.get_children())
        tabelaBanco = Itens.populaItens()
        for i in tabelaBanco:
            self.grade.insert("", "end", value=i)
        if self.itemQuant.get() == self.itemLimite.get():
            messagebox.showinfo("AVISO!!!!!", "Seu limite foi atingido, repor estoque imediatamente!!!!")
        elif self.itemQuant.get() < self.itemLimite.get():
            messagebox.showinfo("AVISO!!!!!", "Sua quantidade está crítica, repor estoque imediatamente!!!!")


    def deletar(self):
        idselecionado = -1
        selecionado = self.grade.selection()[0]
        valores = self.grade.item(selecionado, "values")
        idselecionado = valores[0]
        Itens.deleteItem(idselecionado)
        self.grade.delete(selecionado)
    
    def modificar():
        pass


    def itens_faltando(self):
        janela3 = Tk()
        janela3.title("Itens Faltando")
        janela3.geometry("650x650")
        janela3.minsize(585, 400)

        self.container[12] = Frame(janela3)
        self.container[12]["padx"] = 20
        self.container[12]["pady"] = 5
        self.container[12].pack()
        self.container[13] = Frame(janela3)
        self.container[13]["padx"] = 20
        self.container[13]["pady"] = 5
        self.container[13].pack()

        self.lb_titulo_janela3 = Label(self.container[12], text="Itens em Falta/Vendidos", font=('Arial', '10', 'bold'))
        self.lb_titulo_janela3.pack(side=TOP)

        self.grade2 = ttk.Treeview(self.container[13],
                                  columns=('id', 'produto', 'quantidade', 'especificação', 'valor', 'limite'),
                                  show='headings')
        self.grade2.column('id', minwidth=0, width=50)
        self.grade2.column('quantidade', minwidth=0, width=100)
        self.grade2.column('produto', minwidth=0, width=120)
        self.grade2.column('valor', minwidth=0, width=80)
        self.grade2.column('especificação', minwidth=0, width=100)
        self.grade2.column('limite', minwidth=0, width=150)
        self.grade2.heading('id', text="ID")
        self.grade2.heading('quantidade', text="Quantidade")
        self.grade2.heading('produto', text="Produto")
        self.grade2.heading('valor', text="Preço")
        self.grade2.heading('especificação', text="Categoria")
        self.grade2.heading('limite', text="Limite Mínimo")
        self.grade2.pack()




        janela3.mainloop()


root = Tk()
root.title("Aplicativo de organizações")
root.geometry("400x400")
Organizador(root)
root.mainloop()
