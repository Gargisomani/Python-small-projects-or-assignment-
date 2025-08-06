text=input("Type in the text: ")
try:
    file=open("output.txt","w")
    file.write(text)
    file.close()
    print("Data successfully written to 'output.txt'.")
    text2=input("Enter additional text to append: ")
    file=open("output.txt","a")
    file.write("\n"+text2)
    file.close()
    print("Data successfully appended.")
    file=open("output.txt","r")
    reading=file.read()
    print("Final content of output.txt:\n",reading)
    file.close()
except FileNotFoundError:
    print("Error: The File 'output.txt' was not found.")


