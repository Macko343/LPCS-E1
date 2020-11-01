import re
import os
from bs4 import BeautifulSoup as BS
import requests


A_Nombres = []
areas = []
M_Nombres = ['01 Enero','02 Febrero','03 Marzo','04 Abril','05 Mayo','06 Junio','07 Julio','08 Agosto','09 Septiembre','10 Octubre','11 Noviembre','12 Diciembre']
meses = ['01','02','03','04','05','06','07','08','09','10','11','12']
Datos = {}

def getA_Nombres():
    r = requests.get('http://transparencia.uanl.mx/remuneraciones_mensuales/bxd.php?pag_act=1&id_area_form=1102&mya_det=082020')
    regExArea = r'[0-9]{4}\s&nbsp;\s[A-Z+\;\-\#\.\"\s0-9+ÁÉÍÓÚ]+'
    area_v = set(re.findall(regExArea, r.text))
    for i in area_v:
        i = i.replace("&nbsp;","")
        A_Nombres.append(i)
    A_Nombres.sort()
    #print(i)
    #print(r.text)

def getAreas():
    regExArN = r'[0-9]{4}'
    areas_v = set(re.findall(regExArN, str(A_Nombres)))
    for i in areas_v:
        areas.append(i)
        #print(i)

def getUrl():
    urlD = []
    for area in A_Nombres:
        print('   '+area)
    c = True
    while c==True:
        areaE = input('Ingresa el área que desea visualizar: ')
        for i in areas:
            if i == areaE:
                c = False
    urlD.append(areaE)
    for mes in M_Nombres:
        print('   '+mes)
    c = True
    while c==True:
        mesE = input('Ingresa el mes que desea visualizar, en formato "mm": ')
        for i in meses:
            if i == mesE:
                c = False
    urlD.append(mesE)
    year = input('Ingresa el año que desea visualizar (2019 o 2020): ')            
    while year!='2019' and year!='2020':
        year = input('Ingresa el año que desea visualizar (2019 o 2020): ')
    urlD.append(year)
    print('\n\nObteniendo datos...\n')
    return urlD

def getData(urlD):
    con = True
    i = 1
    while con==True:
        info = []
        url = 'http://transparencia.uanl.mx/remuneraciones_mensuales/bxd.php?pag_act='+str(i)+'&id_area_form='+urlD[0]+'&mya_det='+urlD[1]+urlD[2]
        r = requests.get(url)
        regExArea = r'[0-9]{4}\s&nbsp;\s[A-Z+\-+\#\.\"\s0-9+ÁÉÍÓÚ]+'
        sopa = BS(r.content, 'html.parser')
        pagina = f"page.html"
        path = os.getcwd()
        with open(path+"\\"+pagina, 'w+') as txt:
            txt.writelines(f"{sopa.encode('utf-8')}")
            txt.close()
        with open(path+"\\"+pagina, 'r+') as txt:
            for line in txt.readlines():
                temp = str(line.replace("b'","")[:-1])
                infor = re.compile(r'No genera Personal')
                info.append(infor.findall(temp))
            txt.close()
        #print(info[0])
        #print(r.text)
        if info[0]==['No genera Personal']:
            if i==1:
                print('No hay datos del área y fecha proporcionada')
            con = False
        else:
            regExData = r'<td>[A-Z+\sÑÁÉÍÓÚ]+<\/td>[\r\n\t]*<td\salign=\"right\">\$\s[0-9\,\.]+'
            datos = set(re.findall(regExData, r.text))
            info = []
            for j in datos:
                j = j.replace("<td>","")
                j = j.replace('</td>\r\n\t<td align="right">',":")
                info.append(j)
            info.sort()
            for j in info:
                Datos[j.split(':')[0]] = j.split(':')[1]
            i = i + 1
    for x,y in Datos.items():
        print(x, ':', y)
  
   
getA_Nombres()
getAreas()
#urlD = ['1207','08','2020']
getData(getUrl())


