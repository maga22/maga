filename1 = input('Введите название копируемого файла: ')
filename2 = input('Введите куда скопировать файл: ')

if filename2 != '':
    file2 = open(filename2,'w')

file1 = open(filename1,'r')
file2 = open('copied_' + filename1,'w')



file2.write( file1.read() )

file1.close()
file2.close()

print('Успешно скопировано')
