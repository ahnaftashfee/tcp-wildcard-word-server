# TCP Wildcard Word Server

A TCP-based client–server application written in Python that supports wildcard word queries using socket programming. The project includes both single-threaded and multi-threaded server implementations.

## Features
- TCP client–server communication using sockets
- Custom application-level request/response protocol
- Wildcard pattern matching using `?`
- Single-threaded server for basic client handling
- Multi-threaded server supporting concurrent clients
- Client supports multiple queries until termination

## Technologies Used
- Python 3
- TCP/IP Socket Programming
- Multithreading
- File-based word lookup

## Project Files
- `client_basic.py` / `server_basic.py` – single-client implementation
- `client_threaded.py` / `server_threaded.py` – concurrent server implementation
- `wordlist.txt` – English dictionary used by the server
- `thread-server.txt` – reference multithreaded socket example

## How to Run

Start the server:

python server_threaded.py
Start the client:



python client_threaded.py

Example
Client query:
a?t

Server response:
200 OK
Matches: 3
ant
act
apt

## What this Project Demonstrates

-Strong understanding of TCP/IP networking concepts

-Client–server system design

-Concurrent server architecture using threads

-Application-layer protocol design similar to HTTP

## Author
-Mohammad Tashfee
-University of Connecticut
