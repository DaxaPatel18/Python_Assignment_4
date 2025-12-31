text=input("Enter text to write to the file:")

with open("C:\Python_Assignments\Assignment_4\output.txt","wt") as fh:
    fh.write(text)
print("Data successfully written to 'output.txt'.")

append=input("Enter additional text to append:")
with open("C:\Python_Assignments\Assignment_4\output.txt","at") as fh:
    fh.write("\n" + append)
print("Data successfully appended.")

print("Final content of 'output.txt':")
with open("C:\Python_Assignments\Assignment_4\output.txt","rt") as fh:
        line1=fh.readline().strip()
        line2=fh.readline().strip()

print(line1)
print(line2)
