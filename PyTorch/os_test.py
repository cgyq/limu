names = ['joker','joe','nacy','timi']
filename= 'names.txt'
name ='\n'.join(names)
with open(filename,'w') as f:
    f.write(name)