import pickle, struct
import socket
import pandas as pd

BUFSIZ = 1024 * 4

def recvall(sock, size):
    message = bytearray()
    while len(message) < size:
        buffer = sock.recv(size - len(message))
        if not buffer:
            raise EOFError('Could not receive all expected data!')
        message.extend(buffer)
    return bytes(message)

def receive(client):
    packed = recvall(client, struct.calcsize('!I'))
    size = struct.unpack('!I', packed)[0]
    data = recvall(client, size)
    return data

def send_kill(conn:socket.socket, process_id):
    conn.sendall(b"0".ljust(BUFSIZ))
    s = str(process_id)
    conn.sendall(s.encode().ljust(BUFSIZ))
    ack = conn.recv(BUFSIZ).decode()
    return ack

def _list(conn:socket.socket, s):
    conn.sendall(b"1".ljust(BUFSIZ))
    conn.sendall(s.encode().ljust(BUFSIZ))

    ls1 = receive(conn)
    ls1 = pickle.loads(ls1)
    ls2 = receive(conn)
    ls2 = pickle.loads(ls2) 
    ls3 = receive(conn)
    ls3 = pickle.loads(ls3)

    process_list = pd.DataFrame(
        {
            'Name': ls1,
            'ID': ls2,
            'Count Threads': ls3,
        }
    )

    str_process_list = process_list.to_string(index = True)
    return str_process_list