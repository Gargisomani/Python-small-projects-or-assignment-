try:
    file=open("sample.txt","r+")
    file.write("This is a sample text file.\nIt contains multiple lines.")
    file.close()
    file=open("sample.txt","r+")
    reading=file.read()
    print(reading)
    file.close()
except FileNotFoundError:
    print("Error: The File 'sample.txt' was not found.")

