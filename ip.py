import socket

website = input("Enter a hostname: ")
ip = socket.gethostbyname(website)

print ("The IP address of " + website + " is " + ip)
