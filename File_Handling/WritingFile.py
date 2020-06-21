# Writing in same file. It will override same file.
with open('/Users/VikramSingh/Pictures/PythonLearning/File_Handling/File.txt','w') as writeInFile:
    writeInFile.write('Hello this is temporary file.\nI am Vikram Singh.\nI am Learning file-handling in Python.\nLet\'s see I am able to do it or not.Hey I am Trying to write in Same File.\n')

# Writing in different File
with open('/Users/VikramSingh/Pictures/PythonLearning/File_Handling/NewFile.txt','w') as newFile:
    newFile.writelines('Hello!, I am writing in new file.\nLet\'s see it will work or not.')
    newFile.writelines('\nHello!, I am writing second line in new file.\nLet\'s see it will work or not.') # In this we can write different Lines.
    newFile.write('\nBoom! It\'s working.')   # It will write single line

# Now we will read from two files and write in another file
with open('/Users/VikramSingh/Pictures/PythonLearning/File_Handling/NewFromTwoFile.txt','w') as mergeFile:
    with open('/Users/VikramSingh/Pictures/PythonLearning/File_Handling/File.txt','r') as firstFile:
        fileContent = firstFile.readlines();
        for line in fileContent:
            mergeFile.write(line);

    mergeFile.write('\n\nHey above content is from First File.')  
    with open('/Users/VikramSingh/Pictures/PythonLearning/File_Handling/NewFile.txt','r') as secondFile:
        fileContent = secondFile.readlines()
        for line in fileContent:
            mergeFile.write(line)
    mergeFile.write('\n\nHey! We created new file from two file')    



