import socket
import ssl
import subprocess

HOST = "0.0.0.0"
PORT = 9999

# Create SSL context
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

# Create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print("Secure Server started...")
print("Waiting for client...")

while True:
    try:
        client, addr = server.accept()
        print("Connected to:", addr)

        # Wrap client socket with SSL
        secure_client = context.wrap_socket(client, server_side=True)

        # Receive host
        host = secure_client.recv(1024).decode()
        print("Diagnosing:", host)

        try:
            # Windows commands
            ping_result = subprocess.check_output(
                ["ping", "-n", "4", host], text=True
            )

            trace_result = subprocess.check_output(
                ["tracert", host], text=True
            )

            result = "\nPING RESULT:\n" + ping_result + "\nTRACEROUTE RESULT:\n" + trace_result

        except Exception as e:
            result = "Error: " + str(e)

        # Send result
        secure_client.send(result.encode())
        secure_client.close()

    except Exception as e:
        print("Server error:", e)