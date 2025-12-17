"""
server_basic.py
Single-threaded TCP server for CSE3300 Project 1
This is for one client at a time and not multiple
"""

import socket
import re


HOST = ''           #this is the loal host the machine
PORT = 50007        # this is the port number and we will use port 50007
WORDLIST_FILE = 'wordlist.txt' #this is the wordfile query which the program will access to find the words


def load_words():


    #reading the entire wordlist file into memory once

    with open(WORDLIST_FILE, 'r') as file:
        return [line.strip() for line in file]

def find_matches(pattern, words):

    #this will find all words matching the query pattern with '?' wildcard.

    regex_pattern = '^' + pattern.replace('?', '.') + '$'
    regex = re.compile(regex_pattern)
    return [w for w in words if regex.match(w)]

# main function

def main():

    #loads the whole file of words at once

    words = load_words()
    print("Server started on port", PORT)
    print("Waiting for client connection...")

    # creating the socket


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:

        server_socket.bind((HOST, PORT))
        server_socket.listen(1) #this makes sure one client ONLY is handled

        while True:

            conn, addr = server_socket.accept() #the client connects
            print(f"Connected by {addr}")

            # Receive query

            data = conn.recv(1024).decode().strip()
            print(f"Received query: {data}")

            matches = find_matches(data, words) ## Find all words matching the query


          #build the response message

            if matches:
                response = f"200 OK {len(matches)} matches found\n" + "\n".join(matches)
            else:
                response = "404 Not Found\nNo words matched your query."

            conn.sendall(response.encode())   # Send response to client

            # Close connection for this client

            conn.close()
            

            print("Connection closed.\n")



if __name__ == "__main__":
    main()
