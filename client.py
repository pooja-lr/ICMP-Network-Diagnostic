import socket
import ssl

SERVER_IP = "127.0.0.1"
PORT = 9999

# Disable certificate verification (for self-signed cert)
context = ssl._create_unverified_context()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
secure_client = context.wrap_socket(client, server_hostname=SERVER_IP)

try:
    secure_client.connect((SERVER_IP, PORT))

    host = input("Enter host to diagnose: ")
    secure_client.send(host.encode())

    print("\n--- RESULT ---\n")

    result = secure_client.recv(65535).decode()
    print(result)

except Exception as e:
    print("Connection error:", e)

finally:
    secure_client.close()