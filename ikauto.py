#!/usr/bin/python
# -*- coding: utf8 -*-

import requests

from Tkinter import *

class Layout:
	def __init__(self, master=None):
		self.primeiroContainer = Frame(master)
		self.primeiroContainer["pady"] = 20
		self.primeiroContainer.pack()
		
		self.segundoContainer = Frame(master)
		self.segundoContainer["padx"] = 20
		self.segundoContainer.pack()

		self.terceiroContainer = Frame(master)
		self.terceiroContainer["padx"] = 20
		self.terceiroContainer.pack()

		self.quartoContainer = Frame(master)
		self.quartoContainer["pady"] = 20
		self.quartoContainer.pack()

		self.top = Label(self.primeiroContainer, text="Ikauto")
		self.top["font"] = ("Tahoma", "20", "bold")
		self.top.pack()

		self.nomeLabel = Label(self.segundoContainer,text="Nome:")
		self.nomeLabel.pack(side=LEFT)

		self.nome = Entry(self.segundoContainer)
		self.nome["width"] = 25
		self.nome.pack(side=LEFT)

		self.senhaLabel = Label(self.terceiroContainer,text="Senha:")
		self.senhaLabel.pack(side=LEFT)

		self.senha = Entry(self.terceiroContainer)
		self.senha["width"] = 25
		self.senha["show"] = '*'
		self.senha.pack(side=LEFT)

		self.autenticar = Button(self.quartoContainer)
		self.autenticar["text"] = "Login"
		self.autenticar["command"] = self.login
		self.autenticar.pack()

		self.msg = Label(self.quartoContainer,text="")
		self.msg.pack()


	def login(self):
		user = self.nome.get()
		passw = self.senha.get()
		dados = {'name': user, 'password': passw}
		headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
		r = requests.post("http://s37-br.ikariam.gameforge.com/index.php?action=loginAvatar&function=login", data=dados, headers=headers)
		texto = r.text

		def recursos():
			tmp1 = texto.split('<td id="js_GlobalMenu_wood_Total" class="rightText">')
			nome1 = tmp1[1].strip()
			total1 = nome1.split('</td>')
			tf = "Madeira:"+total1[0]
			
			tmp2 = texto.split('<td id="js_GlobalMenu_wine_Total" class="rightText">')
			nome2 = tmp2[1].strip()
			total2 = nome2.split('</td>')
			tf2 = "Vinho:"+total2[0]
			
			tmp3 = texto.split('<td id="js_GlobalMenu_marble_Total" class="rightText">')
			nome3 = tmp3[1].strip()
			total3 = nome3.split('</td>')
			tf3 = "Marmore:"+total3[0]
			
			tmp4 = texto.split('<td id="js_GlobalMenu_crystal_Total" class="rightText">')
			nome4 = tmp4[1].strip()
			total4 = nome4.split('</td>')
			tf4 = "Cristal:"+total4[0]
			
			tmp5 = texto.split('<td id="js_GlobalMenu_sulfur_Total" class="rightText">')
			nome5 = tmp5[1].strip()
			total5 = nome5.split('</td>')
			tf5 = "Enxofre:"+total5[0]
			self.msg["text"] = tf+'\n'+tf2+'\n'+tf3+'\n'+tf4+'\n'+tf5
		recursos()

root = Tk()
Layout(root)
root.mainloop()
