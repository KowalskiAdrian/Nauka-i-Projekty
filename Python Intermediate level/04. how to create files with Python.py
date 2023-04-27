with open('writting_files.txt', 'w') as file: # 'w' write
    file.write("Hello from Venus!")

with open('writting_files.txt', 'a') as file: # append
    file.write("Hello from Earth!")

with open('writting_files.txt', 'a') as file: # append
    file.write("\nA second line")   # \n new line
    file.write("\n\tA tabbed line")  # \t tabbed line