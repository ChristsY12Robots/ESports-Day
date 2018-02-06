# work in progress.

import datetime
#print (datetime.datetime.now())

"""
Nathaniel Huesler: 03/12/2017
Update -- Nathaniel Huesler: 04/12/2017
    Finished off methods for reading from a csv file with all the rules implemented.
Update -- Nathaniel Huesler: 08/12/2017
    Added "read" and "write" classes. The "CSV_File_Read" class only contains read methods. The CSV_File_Write class contains read and write methods.
    Both "CSV_File_Read" and "CSV_File_Write" inherit from "CSV_File"
Update -- Nathaniel Huesler: 30/01/2018
    Fixed some bugs.
         -Writing to a file using the "CSV_File_Write" class no longer prints an error when the filename does not exists. Instead, a new file is created.
         - small fixes
Update -- Nathaniel Huesler: 06/02/2018
    -CSV_File class "open_file" method has been changed to "open_file_". methods named "open_file" in inherited classes overwited base class "open_file" method.
        There seems to be no way to explicitly call base class method from the base class. super() does not work as the base class has not super().
    - Leaving arguments "filename" and "perms" when using methods, such as "open_file" and "create_file", when left as "None" or as an empty string will use the last used
        perms and file dirrectory.
    - Having the "filename" not as "None" or "" will overwite the file dirrectory of the class.
    - Opening a file will implicity extract the data and store each element in a list with the correct type.
    
    
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

To read csv files, use the "CSV_File_Read()" class with the file dirrectory.
Giving the file dirrectory will only open the file. To extract the data, use the "CSV_File.extract()" method. After doing this, the "CSV_File.data" attribute will contain the
extracted data.

To edit csv files, use the "CSV_File_Write()" class. This contains additional methods that allow you to edit csv files. Use the "CSV_File_Write.add_record()" to append a new
record to csv data. Use "CSV_File_Write.write_record()" to overwrite a record. To save the file, use "CSV_File_Write.save()". 
"""




from os import path


class CSV_File():
    def __init__(self , filename , perms):
        self.file_dir = filename # a string to store the file dirrectory and name.
        self.perms = perms
        self.raw = "" # the data directly copied from a csv file.
        self.data = [] # this will hold the individual elements of the csv file.

        if (filename == None):
            self.file_dir = ""
        if (self.file_dir != ""):
            self.open_file_(self.file_dir , self.perms)# ---------

    def open_file_(self , filename , perms):
        if (filename != None and filename != ""):
            self.file_dir = filename
        if (perms != None and filename != ""):
            self.perms = perms
            
        if (path.isfile(self.file_dir) == False and self.perms == "r"): # check if the file exists
            print ("Error -- CSV_File::open: File '{0}' does not exist".format(self.file_dir))
            return
        self.raw = ""
        with open(self.file_dir , self.perms) as file:
            for line in file:
                self.raw += line
        file.close()
        self.extract()

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
                try:
                    result.append(int(temp))
                except ValueError:
                    result.append(temp)
                temp = ""
            elif (string_data[index] == "["):# list clause.
                temp_string = string_data[index+1 : self.skip_list(string_data , index)] # make a substing from the start to the end of the csv list.
                result.append(self.extract_loop(temp_string , 0 , False)) # call extract_loop as if the substring is a new csv file and append the result to "result"
                index = self.next_element(string_data , index) # skip over the list and move on.
            elif (string_data[index] == "{"): # skip clause.
                temp_string = string_data[index+1:self.skip(string_data , index)] # assign a tempory string to content of the skip.
                result.append(temp_string) # append the temp string to the result.
                index = self.next_element(string_data , index) # skip to the next element.
            else:
                temp += string_data[index] # append to temp
            index += 1 # move to next charater.
        if (temp != ""): # make sure that there are no elements left behind.
            try:
                result.append(int(temp))
            except:
                result.append(temp)
        return (result)

    def remove_spaces(self , string_data): # removes spaces from string data and returns the result. skips over skip clauses.
        index = 0
        temp = 0
        result = ""
        while (index < len(string_data)): # iterate through string.
            if (string_data[index] == " "): # if there is a space, then pass.
                pass
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

    def print_meta(self):
        print ("dir: {0}\nperms: {1}\n".format(self.file_dir , self.perms) , end="")


class CSV_File_Read(CSV_File):
    def __init__(self , filename):
        super().__init__(filename , "r+")

    def open_file(self , filename):
        self.perms = "r"
        self.file_dir = filename
        super().open_file_()

    def get_data(self , index): # returns the data at a given index.
        if (index >= len(self.data) or index < 0):
            if (index == 0):
                return
            print ("Error -- CSV_File_Read::get_data: index out of range\n\trecord count = {0}\n\tindex = {1}".format(len(self.data) , index))
            return
        return (self.data[index])

class CSV_File_Write(CSV_File):
    def __init__(self , filename):
        super().__init__(filename , "w+")

    def open_file(self , filename):
        super().open_file_(filename , "w+")

    def create_file(self , filename , suffix , current):
        if (current == True):
            self.file_dir = path.dirname(path.abspath(__file__)) + "\\" + filename + "." + suffix
        else:
            self.file_dir = filename + "." + suffix
        
        tempory_file = open(self.file_dir , "w+")
        tempory_file.close()

        super().open_file_(self.file_dir , "w+")
        super().extract()

    def add_record(self , data_in): # adds a record, no checking involved.
        if (data_in == None):
            return
        self.data.append(data_in)

    def write_record(self , data_in , index): # over-writes a record.
        if (data_in == None):
            return 
        if (index >= len(self.data) or index < 0):
            if (index == 0):
                return
            print ("Error -- CSV_File_Write::write:: Index out of range.\n\tdata size = {0}\n\t index = {1}".format(len(data_in) , index))
            return
        self.data[index] = data_in

    def write_field(self , data_in , record , element):
        if (data_in == None):
            return
        
    def save(self , filename):
        if (filename != "" and filename != None):
            self.file_dir = filename
        
        with open(self.file_dir , "w+") as file:
            self.raw = ""
            for record in self.data:
                self.raw += self.compress(record) + "\n"
            file.write(self.raw)
        
    def compress(self , record):
        result = ""
        for field in record:
            if (isinstance(field , list) == True):
                result = result + ("[" + self.compress(field) + "]")
            elif (isinstance(field , str) == True):
                result += "{" + field + "}"
            else:
                result += str(field)
            result += ","
        if (result[len(result)-1] == ","):
            result = result[0:len(result)-1]
        return (result)


"""file_data = CSV_File_Write(None)
file_data.create_file("dummy_file" , "txt")
file_data.open_file("data_2.txt")
file_data.add_record(["hello thete , gfdf"])
file_data.save("data_3.txt" , "a")

file_data.print_data()



#file_data.save("data_3.txt" , "a")
#print ("-------------------------------")
#file_data.print_data()"""

