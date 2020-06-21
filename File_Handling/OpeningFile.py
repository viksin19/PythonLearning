File_Read = open(
    '/Users/VikramSingh/Pictures/PythonLearning/File_Handling/File.txt', 'r')

# output : /Users/VikramSingh/Pictures/PythonLearning/File_Handling/File.txt
print(File_Read.name)
print(File_Read.mode)    # output : r     -- read , w -- write
File_Read.close()        # closing file
print(File_Read.closed)  # output : True


#
#
###  using with 

with open('/Users/VikramSingh/Pictures/PythonLearning/File_Handling/File.txt','r') as file_read:
    File_Content = file_read.read()  # Whole content will be loaded
    print(File_Content)    # Content of the file will be in output
                           # Here file is closing.
print(file_read.closed)    # output : True
print(File_Content)

## Reading in different way

with open('/Users/VikramSingh/Pictures/PythonLearning/File_Handling/File.txt','r') as fileRead:
    File_Content_2 = fileRead.readline()   #It will read one line at a time.
    print(File_Content_2)      #It will output First Line
    print(fileRead.readline()) #It will output second line    and same way so on.....

    File_Content_List = fileRead.readlines() #It will read all the lines in the file in the list.
    print(File_Content_List)    #It will output List of lines from third Line.

with open('/Users/VikramSingh/Pictures/PythonLearning/File_Handling/File.txt','r') as fileRead:
    File_Content_List = fileRead.readlines()
    print(File_Content_List)   #output : ['Hello this is temporary file.\n', 'I am Vikram Singh.\n', 'I am Learning file-handling in Python.\n', "Let's see I am able to do it or not."]
    

