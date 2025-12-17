"""
client_basic.py

Single-query TCP client for CSE3300 Project 1


"""

import socket
#this is the local host tge machine and means the server is running locally on the same machine

HOST = 'localhost'

#this is the port number and we will use 50007


PORT = 50007

def main():

# prompting the user to type a wildcard query

    query = input("Enter your query (use ? as wildcard): ").strip()

 # Create socket and connect to the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:


# Send the query to the server


        client_socket.connect((HOST, PORT))

        client_socket.sendall(query.encode()) # Wait for the server's response


# Print the response

        response = client_socket.recv(4096).decode()
        print("\n--- Server Response ---")
        print(response)
        print("-----------------------")




if __name__ == "__main__":
    main()
