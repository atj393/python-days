""" myfile = open("files/fruits.txt")

print(myfile.read())

myfile.close()

with open("files/fruits.txt") as myfile2:
    content = myfile2.read()
    print(content)


with open("files/vegetable.txt","w") as myfile3:
    myfile3.write("Tomato\nOnion\nCarrot\n")
    myfile3.write("Garlic")


with open("files/vegetable2.txt","a+") as myfile3:
    myfile3.write("\nGarlic")
    myfile3.seek(0)
    print(myfile3.read())
 """

with open("files/vegetable2.txt", "a+") as myfile:
    myfile.seek(0)
    content = myfile.read()
    myfile.seek(0)
    myfile.write(content)
    myfile.write(content)