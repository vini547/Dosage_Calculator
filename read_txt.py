file = open('passosgit.txt', 'r')
f = file.readlines()
print("Arquivo: ",file.mode ,", lido com sucesso!")

newList = []
for line in f:
    newList.append(line[:-1])

print(newList)