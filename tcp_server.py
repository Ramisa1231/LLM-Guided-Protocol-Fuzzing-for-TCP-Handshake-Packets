# tcp_server.py
import socket

HOST = '0.0.0.0'
PORT = 12345

def run_tcp_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
        server_sock.bind((HOST, PORT))
        server_sock.listen()
        print(f"[*] TCP Server listening on {HOST}:{PORT}")

        while True:  # accept many clients
            conn, addr = server_sock.accept()
            with conn:
                print(f"[+] Connection from {addr}")
                data = conn.recv(1024)
                print(f"[>] Received: {data.decode('utf-8')}")
                conn.sendall(b"Hello Client!")

if __name__ == "__main__":
    run_tcp_server()
