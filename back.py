import pandas as pd
from datetime import date
import os

path = "C:\\Users\\shubh\\Desktop\\app\\"
filename = str(date.today()) + ".csv"
cols = ['Product_name', 'Price', 'Stock', 'Category']

print(path)


def check_file():
    try:
        f=open(path+filename, 'r')
    except FileNotFoundError:
        print('No files exists, creating file by name: '+filename)
        print('Please insert some records to begin with')
        file = open(filename,'w')
        file.write('Product_name,Price,Stock,Category\n')
        file.close()
        
        msg='No files exists, creating file by name: '+filename+'\nPlease insert some records to begin with'
        return msg
    
    
    
def get_file(name=""):
    try:
        f=open(path+filename, 'r')
        lines = f.readlines()
        f.close()
        if len(name) == 0:
            print(lines)
            return lines
        for l in lines:
            line=l.split(',')
            if line[0] == name:
                return line
   
        return "No results found!"

    except FileNotFoundError:
        print('No files exists, creating file by name: '+filename)
        print('Please insert some records to begin with')
        
        file = open(filename,'w')
        file.write('Product_name,Price,Stock,Category')
        file.close()
        
        

def insert(name, stock, category="No Entry", price="No Entry"):
    check_file()
    if len(category) == 0:
        category="No Entry"
    if len(price) == 0:
        price="No Entry"
        
    if isinstance(get_file(name), list):
        print('Product exists, try updating product details instead: ',get_file(name))

    if stock.isnumeric():
        file = open(filename,'a')
        s = name + "," + str(price) + "," + str(stock) + "," + category+',\n'
        print(s)
        file.write(s)
        file.close()
        return s
    else:
        print("Stock should be a valid number!")
        return "Stock should be a valid number!"

      
      
def update_selected(name):
    pass


