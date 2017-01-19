#!/usr/bin/python
# -*- coding: utf8 -*-

import requests
import urllib
user = raw_input("Usuário: ")
passw = raw_input("Senha: ")

dados = {'name': user, 'password': passw}

r = requests.post("http://s37-br.ikariam.gameforge.com/index.php?action=loginAvatar&function=login", data=dados)
texto = r.text

def recursos():
	tmp1 = texto.split('<td id="js_GlobalMenu_wood_Total" class="rightText">')
	nome1 = tmp1[1].strip()
	total1 = nome1.split('</td>')
	print "Madeira: ",total1[0]
	tmp2 = texto.split('<td id="js_GlobalMenu_wine_Total" class="rightText">')
	nome2 = tmp2[1].strip()
	total2 = nome2.split('</td>')
	print "Vinho: ",total2[0]
	tmp3 = texto.split('<td id="js_GlobalMenu_marble_Total" class="rightText">')
	nome3 = tmp3[1].strip()
	total3 = nome3.split('</td>')
	print "Mármore: ",total3[0]
	tmp4 = texto.split('<td id="js_GlobalMenu_crystal_Total" class="rightText">')
	nome4 = tmp4[1].strip()
	total4 = nome4.split('</td>')
	print "Cristal: ",total4[0]
	tmp5 = texto.split('<td id="js_GlobalMenu_sulfur_Total" class="rightText">')
	nome5 = tmp5[1].strip()
	total5 = nome5.split('</td>')
	print "Enxofre: ",total5[0]

recursos()