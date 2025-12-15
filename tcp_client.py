# tcp_client.py
import socket
import time

SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345
NUM_CONNECTIONS = 20  # gives you 20 handshakes

def run_tcp_client():
    time.sleep(5)  # give tshark time to start
    for i in range(NUM_CONNECTIONS):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_sock:
            client_sock.connect((SERVER_IP, SERVER_PORT))
            print(f"[*] Connected #{i+1}")
            client_sock.sendall(b"Hello Server!")
            data = client_sock.recv(1024)
            print(f"[<] Reply #{i+1}: {data.decode('utf-8')}")
            # socket closes here -> teardown packets

if __name__ == "__main__":
    run_tcp_client()
