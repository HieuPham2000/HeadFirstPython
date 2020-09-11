import os
import csv

os.chdir('D:\Home\practice\python\headfirstpython\chapter12')
with open('buzzers.csv') as data:
    for line in csv.reader(data):
        print(line)