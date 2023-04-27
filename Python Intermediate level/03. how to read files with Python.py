# with open('filename', 'r') as file:
#     print(file.read())


with open('readme.txt', 'r') as file:  # 'r' read
    print(file.read())

with open('readme.txt', 'r') as file:  # 'r' read
    content = file.read()
    
print("The content is", content)