try:
    with open("myfile.txt") as f:
        data = f.read()
    print(data)
except Exception as err:
    print("couldnt get the file skipping to next task ")
    
print("some other important task that must happen")