#A simple library that prettify data

from prettytable import PrettyTable

#Creating your table
table = PrettyTable()

#Creating field names
table.field_names = ['Name', 'Age', 'Address']

#Function that adds data to the table
def add_record(name,age,address):
    table.add_row([name, age, address])

#Align function either right,left or center
def align_table(position):
    table.align = position
    
#Sort Function
def sort_table(sort_by):
    table.sortby = sort_by

#Html form function
def html_form():
    return table.get_html_string()

#Print table function
def print_table():
    print(table)
    
