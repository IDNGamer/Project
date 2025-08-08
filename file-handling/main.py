try:
    file = open('file-handling/mynote.txt', 'x')
except:
    print('File Exist')

file = open('file-handling/mynote.txt', 'r')
print(file.read())

file = open('file-handling/note.txt', 'w')
file.write('The quick brown fox jumps over the lazy dog.')

file=open('file-handling/note.txt', 'a')
file.write('1234567890')
file.close