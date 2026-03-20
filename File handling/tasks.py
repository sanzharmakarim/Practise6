import shutil
import os

#task1
with open("text.txt", "w") as f:
   f.write("Hello, my name is Maulenali!")

with open("text.txt") as f:
    print(f.read())

#task2
with open("text.txt", "r") as f:
    print(f.read())

#task3
with open("text.txt", "a") as f:
    f.write(" My hobby is playing video games. ")
with open("text.txt") as f:
    print(f.read())

#task4
shutil.copy("text.txt", "text_2.txt")
with open("text_2.txt", "a", encoding="utf-8") as f:
    f.write(" And i like reading books!")
with open("text_2.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

#task5
if os.path.exists("text_2.txt"):
    os.remove("text_2.txt")
else:
    print("The file does not exist")
