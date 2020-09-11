import os

os.chdir('D:\Home\practice\python\headfirstpython\chapter12')
with open('buzzers.csv') as raw_data:
    print(raw_data.read())