"""
client_threaded.py
Multi-query TCP client for CSE3300 Project 1
"""

import socket
#this is the local host tge machine and means the server is running locally on the same machine

HOST = 'localhost'


PORT = 50007 #this is the port number and we will use 50007

def main():
    #
    print("Connected to server. Type 'quit' to exit.")

# Create socket and connect once

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))

        while True:

             # Ask user for query each time

            query = input("\nEnter your query (use ? as wildcard): ").strip()

            # If user wants to exit, break loop

            if query.lower() == "quit":

                  # Send the query to the server

                client_socket.sendall(query.encode())
                break
            
# Receive and display the results

            client_socket.sendall(query.encode())
            response = client_socket.recv(8192).decode()
            print("\n--- Server Response ---")
            print(response)
            print("-----------------------")

if __name__ == "__main__":
    main()
