# import socket
# from _thread import *
# import pickle


# server = "192.168.1.7"
# port = 5555

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# try:
#     s.bind((server, port))
# except socket.error as e:
#     str(e)

# s.listen(2)
# print("Waiting for a connection, Server Started")

# connected = set()
# games = {}
# idCount = 0


# def threaded_client(conn):
#     global idCount
#     conn.send(str.encode("Connected"))

#     reply = ""
#     while True:
#         try:
#             data = conn.recv(2048)
#             reply = data.decode("utf-8")
#             # if gameId in games:
#             #     game = games[gameId]

#             if not data:
#                 print("Disconnected")
#                 break
#             else:
#                 print("Received", reply)
#                 print("Sending", reply)
#                     # if data == "reset":
#                     #     game.resetWent()
#                     # elif data != "get":
#                     #     game.play(p, data)

#                     # conn.sendall(pickle.dumps(game))
#             # else:
#             #     break
#         except:
#             break

#     print("Lost connection")
#     # try:
#     #     del games[gameId]
#     #     print("Closing Game", gameId)
#     # except:
#     #     pass
#     # idCount -= 1
#     conn.close()



# while True:
#     conn, addr = s.accept()
#     print("Connected to:", addr)

#     # idCount += 1
#     # p = 0
#     # gameId = (idCount - 1)//2
#     # if idCount % 2 == 1:
#     #     games[gameId] = Game(gameId)
#     #     print("Creating a new game...")
#     # else:
#     #     games[gameId].ready = True
#     #     p = 1


#     start_new_thread(threaded_client, (conn,))

import socket
from _thread import *
import sys

server = "192.168.1.7"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")


def threaded_client(conn):
    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending : ", reply)

            conn.sendall(str.encode(reply))
        except:
            break

    print("Lost connection")
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn,))