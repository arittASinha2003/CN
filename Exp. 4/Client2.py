# Client 2 Code
import socket
client=socket.socket()
source=input( "Enter desired file: " )
client.connect(( "localhost" ,5006))
client.send(source.encode())
n=input( "Enter new file name: " )
with open(n, "wb" ) as f:
    print( 'File opened' )
    while True:
        data=client.recv(1024)
        if not data:
            break
        print( 'Receiving data...' )
        print('Data in New file:')
        print(data)
        print( "file recieved by client02" )
        print( "Connection Lost" )
        f.close()
client.close()
