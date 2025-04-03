n=input("Enter the content u want to write in a file:")

with open("sample.txt","w") as f:
        f.write(n+"\n")
        print("data succesfuilly written to the file")


while True:
   appending=input("enter the content u want to append:")
   if appending.lower()=="exit":
       break
 
   with open("sample.txt","a") as f:
  
       f.write(appending+"\n")
       print("data succesfully appended")

with open("sample.txt") as f :
    m=f.read()
           
print("final content of file:")
print(m)