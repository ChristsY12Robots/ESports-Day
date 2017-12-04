# work in progress.

import datetime
print (datetime.datetime.now())

"""
Nathaniel Huesler: 03/12/2017
Update -- Nathaniel Huesler: 04/12/2017
    Finished off methods for reading from a csv file with all the rules implemented.
    
    
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

(4) A new line will create a new record.
To edit csv files, use the CSV_File() class with the file dirrectory.
Giving the file dirrectory will only open the file. To extract the data, use the CSV_File.extract() method. After doing this, the CSV_File.data attribute will contain the
extracted data.
"""




from os import path


class CSV_File():
    def __init__(self , filename):
        self.file_dir = filename # a string to store the file dirrectory and name.
        self.raw = "" # the data directly copied from a csv file.
        self.data = [] # this will hold the individual elements of the csv file.

        self.open_file(filename)

    def open_file(self , filename):
        if (path.isfile(filename) == False): # check if the file exists
            print ("Error -- CSV_File.open: File '{0}' does not exist".format(filename))
            return
        
        file = open(filename)
        for letters in file: # go though the file and copy it's content into "self.raw"
            self.raw += letters
        self.file_dir = filename

    def extract(self): # starter method. this will call the CSV_file.extract_loop() method.
        line = "" # this will temporarily hold one line of the csv file. 
        for letter in self.raw:
            if (letter == "\n"): # if the program hits the end of the line
                self.data.append(self.extract_loop(line , 0 , True)) # create a new record.
                line = ""
            else:
                line += letter # append to line.
        if (line != ""):
            self.data.append(self.extract_loop(line , 0 , True)) # make sure that there are no records left behind.
                
    def extract_loop(self , string_data , index , reduce): # extracts the data from a csv file into a list. parameter "reduce" will determine if spaces are removed.
        temp = ""
        temp_string = ""
        index = 0 # set index to zero. index is a parameter just in case we need to start from a different position.
        result = [] # this is the returning data structure.
        if (reduce == True):
            string_data = self.remove_spaces(string_data)
            
        while (index < len(string_data)):
            if (string_data[index] == ","): # commna, new element.
                result.append(temp)
                temp = ""
            elif (string_data[index] == "["):# list clause.
                temp_string = string_data[index+1 : self.skip_list(string_data , index)] # make a substing from the start to the end of the csv list.
                result.append(self.extract_loop(temp_string , 0 , False)) # call extract_loop as if the substring is a new csv file and append the result to "result"
                index = self.next_element(string_data , index) # skip over the list and move onn.
            else:
                temp += string_data[index] # append to temp
            index += 1 # move to next charater.
        if (temp != ""): # make sure that there are no elements left behind.
            result.append(temp)
        return (result)

    def remove_spaces(self , string_data): # removes spaces from string data and returns the result. skips over skip clauses.
        index = 0
        temp = 0
        result = ""
        while (index < len(string_data)): # iterate through string.
            if (string_data[index] == " "): # if there is a space, then pass.
                pass
            elif (string_data[index] == "{"): # skip over skip clause.
                temp = self.skip(string_data , index)
                result += string_data[index+1:temp]
                index = temp
                if (index >= len(string_data)): # this is needed to prevent a potential error.
                    return (result)
            else:
                result += string_data[index] # append to result.
            index += 1
        return (result)

    def next_element(self , string_data , index): # returns the index of the next element in a csv file from "index".
        # this method will skip over any clauses to keep in scope.
        while (index < len(string_data)): # iterate.
            if (string_data[index] == "{"):
                index = self.skip(string_data , index)
            elif (string_data[index] == "["):
                index = self.skip_list(string_data , index)
            elif (string_data[index] == ","): # if there is a comma, then return the current index - "i".
                return (index)
            index += 1
        return (len(string_data)-1) # index to end of string.

    def skip(self , string_data , index): # returns the index of the end of a skip clause.
        #bracket_level is a variable to store the current bracket indent. For exmple:
        #   1{2{3}4}5
        # these are bracket_levels at the numbers(number:bracket_level): 1:0 , 2:1 , 3:2 , 4:1 , 5:0
        bracket_level = 0
        for i in range(index , len(string_data) , 1):
            if (string_data[i] == "{"): # increament one to the bracket level if there is an open bracket
                bracket_level += 1
            elif (string_data[i] == "}"): # decreament one from the bracket level if there is a closed bracket
                bracket_level -= 1
            if (bracket_level == 0): # bracket_level being zero indicates that the current index is outside the original brackets.
                return (i)
        return (len(string_data)-1)

    def skip_list(self , string_data , index): # this method is the same as CSV_File.skip, however sqaure brackets are used instead.
        bracket_level = 0
        for i in range(index , len(string_data) , 1):
            if (string_data[i] == "["):
                bracket_level += 1
            elif (string_data[i] == "]"):
                bracket_level -= 1
            if (bracket_level == 0):
                return (i)
        return (len(string_data))
    
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
        for record in self.data:
            print (record)


file_data = CSV_File("Z:\\A level\\Robots\\Source_Code\\Database\\data.txt")
file_data.extract()
print ("-------------------------------")
file_data.print_data()
print ("-------------------------------")
file_data.print_raw()
