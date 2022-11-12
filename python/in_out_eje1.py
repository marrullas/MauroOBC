f = open('elfile.txt','w')

f.write("Curso python\n")
f.write("OpenBootCamp\n")

f.close()

f = open('elfile.txt','r')

datos = f.readlines()
for linea in datos :
    print (linea)

f.close()



