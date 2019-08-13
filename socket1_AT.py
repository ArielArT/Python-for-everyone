import socket


while (True):
    adres = input("Podaj stronke:")
    strona = adres.split("/")
    if strona[0] != "http:" : 
        print("zly host http:")
        continue   
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        mysock.connect((strona[2], 80))
        break
    except:
        print("nie mozna sie polaczyc z : ",adres)
        continue
    
komenda = 'GET '+adres+' HTTP/1.0\r\n\r\n'
cmd = komenda.encode()
mysock.send(cmd)

lenght = 0

print("\n\nPoczatek danych\n\n")
while True:
    data = mysock.recv(3000)
    lenght = lenght + len(data)
    if len(data) < 1:
        break
    if lenght < 3001 :
        print(data.decode(),end='')
        print("\n\ndlugosc danych",lenght)
print("\n\nKoniec danych\n\n")
print (lenght)
mysock.close()
