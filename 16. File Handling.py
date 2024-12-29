print("File Handling:\n 1. Temporary Storage - list,tuple, dict created by PVM, which will delee once program terminate. \n 2. Permanent Storage - Files, DB, Big Data, Cloud.\n Syntax for file  I/O: \n  f = open(file_name, mode). The default mode if not provided is, 'r'. It is highly recommedn to close teh file f .close() after oper., since it will delete the res., consumed\n . There are 2 types of files: \n 1) Text File - .txt \n 2) Binary Files - Video,audio,pdf, jar files, any files except text files. \n There are 7 mode operations available for text adn binary files.\n FOr text files - r,w,a,r+,w+,a+,x \n For Bianry Files - rb,wb,ab,r+b,w+b,a+b,xb (just add b (binary) behind)  \n 1) 'r': \n Read: It reads the file, if sepecified filename was not present,return erro. FIle poitner potinign the first char of the file.f = open('abc.txt', 'r')  \n 2)'w': \n Write: If no exisitn filename presen,t enw fiel will eb created. It will oeverride the existing file content \n 3)'a'\n Append:  You will append to the exisitng data. \n 4)'r+'\n Read and Write: It will read and then write, so existing information will not be erased.  \n 5)'w+'\n  Write and Read: It will write and then read, so existing information will be overriden.  \n 6)'a+'\n  Append and Read: It will Append and then read, so existing information will not be overriden.\n 7) 'x': \n Exclusive Mode: f = open('abc.txt', 'x') It exactly write operations, but there shoudl not be existing filename, only new file need to be created and written. IF existing, it leads to FileExistign Error \n Various properties of File Object are name, mode, closed, readable(), writable()")



print(r" If u tried f = open('C:\Users\HP\Downloads\College\asd.txt'), it throws error, since the backslashes in the file path are being interpreted as escape characters, and shows compile-time errors, taht caan;t be shows in try-catch blcoks tatemtns, as it's an compile time error.  Even here, if i used simple print('string') instead of using raw string or \\, it would treated \ as escape character, eleadign to error. In Python, backslashes (\) are used for escape sequences like \n for newline or \t for tab. Solution: There are a few ways to correctly handle the file path to avoid this error:" "\n" r"1) Raw String: \n Prefix the string with r to treat backslashes as literal characters. f = open(r' C:\Users\HP\Downloads\College\asd.txt')" "\n" "2) Double Backslashes: \n" r"Use double backslashes (\\) to escape the backslashes. f = open('C:\\Users\\HP\\Downloads\\College\\asd.txt')" "\n 3) Forward Slashes: \n" r"Use forward slashes (/) instead of backslashes. This works on all platforms. f = open('C:/Users/HP/Downloads/College/asd.txt')")





f = open(r"C:\Users\HP\Downloads\College\asd.txt")
##default mode: read
print("Name of the file: ",f.name)
print("Mode of the file: ",f.mode)
print("Is the file readable: ",f.readable())
print("Is the file writable: ",f.writable())
print("Is the file closed?: ",f.closed)
f.close()
print("Is the file closed?: ",f.closed)


f = open(r"C:\Users\HP\Downloads\College\asd.txt",'w')
print("Write operations: ")
file_name = "vishal.txt"
f = open("C:\\Users\\HP\\Downloads\\College\\" + file_name,'w')
string =  "vishal"
list_of_lines = ['a','b','c','d','e']
f.write(string) 
f.writelines(list_of_lines)
print("Whatever u wite, by defualt, it gets printed on the same line. To print in the nxeet line, u should use escape character" r"\n")

print("Reading operations: ")
print("Enter file name: ")
name = input()
f = open(r"C:\Users\HP\Downloads\College\\" + name, 'r+')
print(r"If you place a backslash directly before the closing quote, Python expects an escape sequence or a valid character to follow. Since it doesn't form a valid sequence, Python throws a SyntaxError: unterminated string literal because it assumes the string isn't finished. So, use f = open(r'C:\Users\HP\Downloads\College\" + name) or open(r'C:\\Users\\HP\\Downloads\\College\\' + name) or f = open(r'C:\Users\HP\Downloads\College' + '\\' + name)")

print(r"If you place a backslash directly before the closing quote, Python expects an escape sequence or a valid character to follow. Since it doesn't form a valid sequence, Python throws a SyntaxError: unterminated string literal because it assumes the string isn't finished. So, use f = open(r'C:\Users\HP\Downloads\College\\' + name) or open(r'C:\\Users\\HP\\Downloads\\College\\' + name) or f = open(r'C:\Users\HP\Downloads\College' + '\\' + name)")

print("Read total data from the file: ",f.read())
print("Read 5 characters from the file: ",f.read(3))
print("Read only 1 line: ",f.readline())
print("Read all lines into a list: ",f.readlines())
print("\n")
print("It won't print anything since, after reading the entire data using f.read(), the pointer would have moved to the end of the file, we need to re-assign the pointer to the starting of the file, to read the sepcific contents.SO,it didnt pritn anything here. FIles indexse are 0-based liek strings, and When you read from a file in Python, the file pointer moves to the position immediately after the last character that was read. the file pointer position returned by f.tell() is 1-based after the last written/added character. The pointer position shown by f.tell() is the next byte position for subsequent read or write operations. It doesn't reflect the position of the last byte written but rather the position just after it.")
print("Current file pointer position: ", f.tell())
f.seek(0)
print("Current file pointer position: ", f.tell())
print("Read 3 characters from the file: ",f.read(3))
print("Current file pointer position: ", f.tell())
f.write("\n")
f.write("Kumar")
print("Current file pointer position after adding escape character and Kumar, escape character also counts in chracter counting: ", f.tell())
f.seek(0)
print("Read 3 characters from the file: ",f.read(3))
print("Current file pointer position: ", f.tell())
print("Read only 1 line: ",f.readline())
print("Read only 1 line: ",f.readline())
print("The reaons why we got an extra space,why printing,is by default escape character is included,after readline operation. So, the escapec haracter ,we also  incldeud in the text file, leads to another extra empty line in between in consequent readline operations")
print("Current file pointer position: ", f.tell())
f.seek(0)
print("Current file pointer position: ", f.tell())
all_lines = f.readlines()
print("Read all lines into a list: ",all_lines)
print("Using loops")
for i in all_lines:
    print(i,end = " ")



print("Instead of explicitelty, writing out f.close() at last, to free up the res., we can use 'with' statemne, that woudl automtically, closes the file,after execution of the bloc is completed")
with open("C:/Users/HP/Downloads/College/kumar.txt",'w') as f2:
    print("I am going to copy, all contents of vishal.txt to kumar.txt",f2.write(f.read()))
    print("Do the kumar is closed within the block?",f2.writable())

try:
    print("Do the kumar is closed outsude the block?", f2.writable())
except:
    print("Closed, cannot access it")


