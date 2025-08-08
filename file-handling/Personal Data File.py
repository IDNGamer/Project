try:
    file = open('file-handling/personaldata.txt', 'x')
except:
    print('File Exist')

file = open('file-handling/personaldata.txt', 'r')
print(file.read())

file=open('file-handling/personaldata.txt', 'a')
file.write('\n Favourite Virus: Jigsaw Ransomware')
file.close