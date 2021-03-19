meat = ['beef', 'pork', 'chiken']
for x in meat[:]:
    if(x == 'pork'):
        meat.remove(x)
    else:
        print(x)