# still working on this file. This is a prototype.comments will be added.

"""
This is a simple program to create database tables. 
Each table has parameters which are used to define fields(name , address). 
The program will do some checks. For example; checking to see if a record has matching fields with a 
table or checking if a record already exists using a primary key.

The program at the moment, can not read or write to files.

"""

class Field_Profile():
    def __init__(self , name , data_type , options):
        if (self.check_initparms(name , data_type , options)):
            print ("Error -- Could not create field profile\n\tdatatype = %s\n\toptions = " % data_type , options , end = "")
        self.name = name
        self.data_type = data_type
        self.options = options

    def check_initparms(self , name , data_type , options):
        if (isinstance(options , list) == False):
            return (True)
        if (isinstance(name , str) == False):
            return (True)
        for i in range(0 , len(options) , 1):
            if (type_str(options[i]) != data_type):
                return (True)
        return (False)

    def print_profile(self):
        print ("{0} , {1} , ".format(self.name , self.data_type) , self.options , end = "")

class ID_Field(Field_Profile):
    def __init__(self):
        super().__init__("ID" , type_str(0) , [])
        
class Name_Field(Field_Profile):
    def __init__(self):
        super().__init__("name" , type_str("") , [])

class Form_Field(Field_Profile):
    def __init__(self):
        super().__init__("form" , type_str("") , ["red" , "blue" , "green" , "yellow"])

class Email_Field(Field_Profile):
    def __init__(self):
        super().__init__("email" , type_str("") , [])

class Password_Field(Field_Profile):
    def __init__(self):
        super().__init__("password" , type_str("") , [])

class Score_Field(Field_Profile):
    def __init__(self):
        super().__init__("score" , type_str(0) , [])





class Table_Parameters():
    def __init__(self , parms):
        if (self.check_initparms(parms) == True):
            print ("Error -- arguments in 'Parm' class constructor are invalid\n\tparms = " , parms , end = "")
        self.parms = parms

    def check_initparms(self , parms):
        if (isinstance(parms , list) == False):
            return (True)
        for i in range(0 , len(parms) , 1): # check all the elements in parameters.
            if (isinstance(parms[i] , Field_Profile) == False):
                return (True)
        return (False)
    
    def print_field_profiles(self):
        for i in range(0 , len(self.parms) , 1):
            self.parms[i].print_profile()
            print ()

    def format_check(self , data , index):
        if (index >= len(self.parms)):
            print ("Error -- Table_Parameters.format_check: index out of range for parameters.\n\tindex = {0}\n\tparameter count"
                   .format(index , len(self.parms)))
            return (True)
        if (self.parms[index].data_type != type_str(data)):
            return (True)
        return (False)

    def option_check(self , data , index):
        if (index >= len(self.parms)):
            print ("Error -- Table_Parameters.option_check: index out of range for parameters.\n\tindex = {0}\n\tparameter count"
                   .format(index , len(self.parms)))
            return (True)
        if (len(self.parms[index].options) == 0):
            return (False)
        for i in range(0 , len(self.parms[index].options) , 1):
            if (data == self.parms[index].options[i]):
                return (False)
        return (True)

class User_Parameters(Table_Parameters):
    def __init__(self):
        super().__init__([ID_Field() , Name_Field() , Form_Field() , Score_Field() , Password_Field() , Email_Field()])
        


class Record():
    def __init__(self , data):
        if (self.check_initparms(data)):
            print ("Error -- Arguments for class 'Record' are invalid\n\tdata = " , data , end = "")
        self.data = data

    def check_initparms(self , data):
        if (isinstance(data , list) == False):
            return (True)
        return (False)

    def print_data(self):
        for i in range(0 , len(self.data) , 1):
            print (self.data[i] , " , " , end = "")
        print ()


class Table():
    def __init__(self , parameters , name):
        if (self.check_initparms(parameters , name)):
            print ("Error -- Arguments in 'Table' class are invalid\n\tparameters = " , parameters , "\n\tname = " , name , "\n" , end = "")
        self.parms = parameters
        self.name = name
        self.data = []

    def check_initparms(self , parameters , name):
        if (isinstance(parameters , Table_Parameters) == False or isinstance(name , str) == False): # check parameters and name
            return (True)
        return (False)

    def add_record(self , record , copy_field):
        if (isinstance(record , Record) == False):
            print ("Error -- Table.add_record: invalid record to add to table{0}\n\trecord = ".format(self.name) , record , end = "")
            return
        if (self.verify_record_parms(record) == True):
            return
        if (self.redundancy_check(record , copy_field) == True):
            return
        self.data.append(record)

    def verify_record_parms(self , record):
        checks = [self.length_check , self.format_check , self.option_check]
        for func in checks:
            if (func(record) == True):
                print ("Returing true")
                return (True)
        return (False)

    def length_check(self , record):
        if (len(record.data) != len(self.parms.parms)):
            print ("Error -- Either too little or too much data in record\n\trecord data = " , record.data)
            return (True)
        return (False)
        
    def format_check(self , record):
        for i in range(0 , len(record.data) , 1):
            if (self.parms.format_check(record.data[i] , i) == True):
                print ("Error - record field is an invalid data type\n\tfield_name = {0}\n\tfield type = {1}\n\tdata = {2}\n\tdata type = {3}"
                       .format(self.parms.parms[i].name , self.parms.parms[i].data_type , record.data[i] , type_str(record.data[i])))
                return (True)
        return (False)
    
    def option_check(self , record):
        for i in range(0 , len(record.data) , 1):
            if (self.parms.option_check(record.data[i] , i) == True):
                print ("Error -- data in record has no option to be '{0}'".format(record.data[i]))
                return (True)
        return (False)

    def redundancy_check(self , record , copy_field):
        if (copy_field >= len(self.parms.parms) or copy_field >= len(record.data)):
            print ("Error -- Table.redundancy_check: copy field out of range\n")
            return (True)
        records = self.find_record(copy_field , record.data[copy_field])
        if (len(records) > 0):
            print ("Error -- Table.redundancy_check: record already exists\n\trequested record:\n\t" , end = "")
            record.print_data()
            print ("\trecord in database\n\t:" , end = "")
            for i in records:
                i.print_data()
            return (True)
        return (False)
            

    def find_record(self , field , value):
        if (field >= len(self.parms.parms)):
            print ("Error -- Table.find_record: field out of range\n\tfield = " , field)
            return ([])
        if (self.parms.format_check(value , field)):
            print ("Error -- Table.find_record: value type is incorrect\n\tvalue type = " , type_str(value))
            return ([])
        
        records = []
        for i in range(0 , len(self.data) , 1):
            print ("finding --- " , self.data[i].data[field] , value)
            if (self.data[i].data[field] == value):
                records.append(self.data[i])
        return (records)
    
    def print_parms(self):
        self.parms.print_field_profiles()

    def print_records(self):
        for i in range(0 , len(self.data) , 1):
            self.data[i].print_data()

def type_str(data):
    types = [str , list , int , float]
    types_str = ("str" , "list" , "int" , "float")
    for i in range(0 , len(types) , 1):
        if (type(data) == types[i]):
            return (types_str[i])
    return ("")

table = Table(User_Parameters() , "player_table")
profile = Field_Profile("name" , "str" , ["true" , "false"])
table.print_parms()
table.add_record(Record([1 , "Jermaine" , "blue" , 200 , "originalpassword123" , "Jermain.pot@rasta.com"]) , 0)
table.add_record(Record([2 , "Jermaine2" , "red" , 200 , "originalpassword1234" , "Jermain.pot@rasta2.com"]) , 0)
print ("--------")
table.print_records()
