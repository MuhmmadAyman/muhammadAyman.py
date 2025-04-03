try:
    with open("sample.txt","r") as f:
        line1=f.readline()
        line2=f.readline()
        print("reading file:")
        print("first line:",line1)
        print("second line:",line2)
except FileNotFoundError:
    print("file was not found")
except Exception as e:
    print(e)




