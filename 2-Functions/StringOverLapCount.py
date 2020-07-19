
def count_substring(string, subString):
    count = 0
    i =0 
    while i < len(string): #Number of time overLapping subString is present in given String
        pos = string.find(subString)
        if pos != -1:
            i = pos +1
            count+=1
        else:
            break
    print("Count of subString :: ",count)        

if __name__ == '__main__':
    print("********** Enter your string **********")
    string = input()
    print("********** Enter the subString **********")
    subString = input()
    count_substring(string,subString)
    


   
    