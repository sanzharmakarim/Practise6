import os
import shutil

#task1
os.makedirs("project/test1/answers", exist_ok=True)
os.makedirs("project/test1/questions", exist_ok=True)
print("Directory created successfully")

#task2
path = "project"
items = os.listdir(path)
for item in items:
    print(item)

#task3
folder = "project"
for root, dirs, files in os.walk(folder):
    for file in files:
        if file.endswith(".txt"):
            print(os.path.join(root, file))

#task4
source = "project/data/raw/data1.txt"
destination = "project/data/processed/data1.txt"
shutil.move(source, destination)
shutil.copy(source, destination)
