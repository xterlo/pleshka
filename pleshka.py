# -*- coding: utf-8 -*-
from openpyxl import load_workbook
import requests
print("Download...")
check = requests.get("https://mpt.ru/priyemnaya-komissiya/09.02.07%20бюджет%209%20кл..xlsx")
f = open("1.xlsx",'wb')
f.write(check.content)
f.close
print("Opening file...")
wb = load_workbook('1.xlsx')
numb=6
name=''
while not name == "Шорин Евгений Максимович":
    name = wb.active['C'+str(numb)].value
    ball = wb.active['D'+str(numb)].value
    print(str(numb-5)+') '+name+" ["+str(ball)+"]")
    numb+=1
input()
