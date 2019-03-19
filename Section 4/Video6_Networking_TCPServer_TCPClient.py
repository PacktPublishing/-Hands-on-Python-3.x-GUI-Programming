'''
Created on Mar 12, 2019
@author: Burkhard A. Meier
'''






# imports 
from PyQt5.QtNetwork import QTcpServer, QHostAddress, QTcpSocket
from PyQt5.QtCore import QDataStream, QByteArray, QIODevice

# globals
SERVER_ADDRESS = 'localhost'
SERVER_PORT = 12345             # read in from GUI


# TCP Server code ------------------------------------  
class TcpServer():
     
    def __init__(self):
        self.tcp_server = QTcpServer()
        self.tcp_server.listen(QHostAddress(SERVER_ADDRESS), SERVER_PORT)
        self.tcp_server.newConnection.connect(self.connect_client)
        self.clients = []

    def connect_client(self):
        client_socket = self.tcp_server.nextPendingConnection()    # Returns the next pending connection as a connected QTcpSocket object
        self.clients.append(client_socket)
        client_socket.readyRead.connect(self.read_data)

    def read_data(self):
        for client_id, client_socket in enumerate(self.clients):
            if client_socket.bytesAvailable() > 0:
                stream = QDataStream(client_socket)
                stream.setVersion(QDataStream.Qt_5_9)
                stream.readUInt32()
                client_data = stream.readQString()               
                self.return_data_to_clients(client_id, client_data)
                        
    def return_data_to_clients(self, client_id, data):
        for client_socket in self.clients:
            return_data_string = 'Client {} sent: {}'.format(client_id, data)
            data_byte_array = QByteArray()
            stream = QDataStream(data_byte_array, QIODevice.WriteOnly)    # Constructs a data stream that operates on a byte array
            stream.setVersion(QDataStream.Qt_5_9)               
            stream.writeUInt32(0)
            stream.writeQString(return_data_string)
            client_socket.write(data_byte_array)
            


# TCP Client code ------------------------------------
class TcpClient():
    
    def __init__(self, line_edit_widget=None, text_widget=None):
        self.line_edit = line_edit_widget
        self.text_widget = text_widget
        self.socket = QTcpSocket()      # client "is a" socket


    def connect_server(self):
        print('inside connect_server')
        print('Port is: ' + str(SERVER_PORT))
        self.socket.connectToHost(SERVER_ADDRESS, SERVER_PORT)


    def write_data(self):
        data_byte_array = QByteArray()
        stream = QDataStream(data_byte_array, QIODevice.WriteOnly)
        stream.setVersion(QDataStream.Qt_5_9)   
        stream.writeUInt32(0)
        if self.line_edit:
            print('inside write_data')
            stream.writeQString(self.line_edit.text())
            
        self.socket.write(data_byte_array)
        data_byte_array = None
        if self.line_edit:
            self.line_edit.setText("")
        
        
    def read_data(self):
        stream = QDataStream(self.socket)
        stream.setVersion(QDataStream.Qt_5_9)   

        while True:
            if self.socket.bytesAvailable() <= 0:
                break
            stream.readUInt32()
            text_from_server = stream.readQString()
            if self.text_widget:
                print('display_text')
                print(text_from_server)
                self.text_widget.append(text_from_server)
                   
            
#-----------------------------
if __name__ == '__main__':
    server = TcpServer()
    print(server.tcp_server)
    
    client = TcpClient()
    print(client.socket)




