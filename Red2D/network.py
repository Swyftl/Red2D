import socket
import Red2D.Logging as Logging

class Network():
    def __init__(self, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = port

        self.socket.bind(("", self.port))
        print("socket binded to port", self.port)

        self.socket.listen(5)
        print("socket is listening")


'''
This is a package that will be implemented and used later on. This will aim to provide the user with the ability to create and use servers for
their game. The main way this will be done is with the python socket package.

The systems will be implemented by us. And the user will be able to set an object to be client or server based.

### Client Based Objects ###
The client based objects will be controlled by the player, and the client will send the data of this object to the server, where the information
will be then sent back to the other connected users to update their display.

### Server Based Objects ###
Like game objects and NPCs, these objects will be controlled and used by the server, and each time the server is meant to udpate the player, will
give each user the updated variables around each object that it needs to.

The server will initially give all players the information for each item that the server controls, and send an update to display each connected
users correct information.

After the player has joined, the server will only ever update the server side assets if they have had any changes made to them

The other player's variables will be updated each server tick, if the player has had any changes made to them locally.
'''