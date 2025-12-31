try:
    file=open("C:\Python_Assignments\Assignment_4\sample.txt","r")
    line1=file.readline()
    line2=file.readline()

    print("Line1:",line1.strip())
    print("Line2:",line2.strip())
    file.close()

except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
