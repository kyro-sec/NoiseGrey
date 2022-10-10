import socket
import time
import threading
from queue import Queue
import dns
import dns.resolver

print_lock = threading.Lock()

# Threader function
def threader():
    # Parses through queue to grab available "workers" and send them to portscan function
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()
        
# Port scanning function
def portscan(port):
    # Initializes socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # The actual scanning to verify if port is available
    result = s.connect((IP,port))
    with print_lock:
        open_ports.append(port)   
    s.close()
    
# Main (initial) function
def main():
    # Gets the hostname from the IP
    hostname = socket.gethostbyaddr(str(IP))
    hostname = str(hostname).split("'")[1:2]

    # Gets the 'A' records
    A_result = dns.resolver.query(URL, 'A')
    A_result_list = []
    for value in A_result:
        A_result_list.append(value)
    
    # Prints information gathered
    print("\n\nURL: " + URL)
    print("IP Address: " + IP)
    print("Hostname: " + hostname[0])
    print("\nA record ports:")
    for x in A_result_list:
        print(x)

    print("\nScanning ports...\nThis may take a while...")
    print("Open ports: ")        

# Start
URL = input("Enter the URL: ")
# Gets the IP of the URL
IP = socket.gethostbyname(URL)    

# Calls main 
if __name__ == "__main__":
    main()

# Creates queue for thread    
q = Queue()
open_ports = []

# Using 4 threads
for x in range(4):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()
    
start = time.time()

# Running through all ports
for worker in range(1, 65353):
    q.put(worker)
    
q.join()

# Prints ports
for item in open_ports:
    print(item)