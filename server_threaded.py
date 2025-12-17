"""
server_threaded.py
Multi-threaded TCP server for CSE3300 Project 1
"""
#importing
import socket
import threading
import re

HOST = '' #this is the local host tge machine and means the server is running locally on the same machine
PORT = 50007 #this is the port number and we will use 50007
WORDLIST_FILE = 'wordlist.txt' #this is the wordfile query which the program will access to find the words

def load_words():
    #reading the entire wordlist file into memory once.
    with open(WORDLIST_FILE, 'r') as file:
        return [line.strip() for line in file]

def find_matches(pattern, words):
    #turn the query into a regex pattern and find matches.
    regex_pattern = '^' + pattern.replace('?', '.') + '$'
    regex = re.compile(regex_pattern)
    return [w for w in words if regex.match(w)]

def handle_client(conn, addr, words):
    #This function handles one client connection
    #tt stays active until the client types 'quit'
    print(f"Client connected: {addr}")
    while True:

         # Wait for a query from this specific client


        data = conn.recv(1024).decode().strip()
         # If no data or user typed 'quit', end this session

        if not data or data.lower() == "quit":

            print(f"Client {addr} disconnected.")

            break

        print(f"Received from {addr}: {data}")
        matches = find_matches(data, words) #lookup all the matching words from the query
#the response 
        if matches:
            response = f"200 OK {len(matches)} matches found\n" + "\n".join(matches)
        else:
            response = "404 Not Found\nNo words matched your query."

        conn.sendall(response.encode()) #send the results

    conn.close()

#main dfunction

def main():
    # Load words into memory before starting the server
    words = load_words()
    print("Multi-threaded server started...")
    print("Listening for client connections...")


#create a socket

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)

        while True:
            # waits for the new connection
            conn, addr = server_socket.accept()
            # Create a new thread for each connected client
            thread = threading.Thread(target=handle_client, args=(conn, addr, words))
            thread.start()

if __name__ == "__main__":
    main()
