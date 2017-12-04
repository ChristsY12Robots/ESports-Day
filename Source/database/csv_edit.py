# work in progress.

import datetime
print (datetime.datetime.now())

"""
Nathaniel Huesler: 03/12/2017

Use this file to access and edit csv files. There are some simple rules.

(1):data are seperated with commas.

    elelemt_1 , element_2 , element_3 , ...

(2):Anything enclosed in curly brackets ({...}) is considered as string data. This is called a skip clause. The program will ignore content inside a skip clause.
This is allows you to store data that would otherwise currupt a csv file. For example:

    "value_1 , 4#gt-,h2 , some name" -> [value_1 , 4#gt- , h2 , somename]

Here "some name" becomes "somename" and "4#gt-,h2" becomes [4#gt- , h2].
Notice that the program will ignore spaces.
A skip clause will fix the problem.

    value_1 , {4#gt-,h2} , {some name} -> [value1 , 4#gt-,h2 , some name]

    
(3)Using square brackets allows you to make a list. When extracting data from a csv file, the program will store a 'csv' list in into 'pyhton' list. This results with an
embedded list. For example:

This is a csv file:
    "some_data , [list_el_0 , list_el_1 , {hello world}] , more"
    
And this is what the program will produce:
    [some_data , [list_el_0 , list_el_1 , hello world] , more] <-- list within list.


To edit csv files, use the CSV_File() class with the file dirrectory.
Giving the file dirrectory will only open the file. To extract the data, use the CSV_File.extract() method.

"""




from os import path


class CSV_File():
    def __init__(self , filename):
        self.file_dir = filename # a string to store the file dirrectory and name.
        self.raw = "" # the data directly copied from a csv file.
        self.data = [] # this will hold the individual elements of the csv file.

        self.open(filename)

    def open(self , filename):
        if (path.isfile(filename) == False): # check if the file exists
            print ("Error -- CSV_File.open: File '{0}' does not exist".format(filename))
            return
        
        file = open(filename)
        for letters in file: # go though the file and copy it's content into "self.raw"
            self.raw += letters

        self.file_dir = filename

    def extract(self): # extracts the data from a csv file into a list.
        temp = ""
        index = 0

        while (index < len(self.raw)):
            if (self.raw[index] == ","): # commna, new element.
                self.data.append(temp)
                temp = ""
            elif (self.raw[index] == "{"): # skip clause
                pass
            elif (self.raw[index] == "["):# list clause
                pass
            elif (self.raw[index] == " "): # pass over spaces
                pass
            else:
                temp += self.raw[index] # append to temp.
            index += 1 # move to next charater.


    def next_element(self , index): # returns the index of the next element in a csv file from "index"
        for i in range(index , len(self.raw) , 1):
            if (self.raw[i] == "{"):
                i = self.skip(i)
            if (self.raw[i] == ","):
                return (i)
        return (len(self.raw))

    def skip(self , index): # returns the index of the end of a skip clause.
        pass

    
    def print_raw(self): # prints the raw data from the file.
        line = ""
        for letter in self.raw: # safe printing. This will print the raw data in chunks.
            if (letter == "\n"):
               print (line)
               line = ""
            else:
                line += letter
        print (line)
        
    def print_data(self): # prints the extracted data.
        print (self.data)


file_data = CSV_File("file dirrectory")
file_data.print_raw()
file_data.extract()
file_data.print_data()
