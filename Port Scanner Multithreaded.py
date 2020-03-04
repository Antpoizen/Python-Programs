import socket
from datetime import datetime
import sys
from multiprocessing.dummy import Pool as ThreadPool


server = input("Enter a Host to scan: \n")
serverip = socket.gethostbyname(server)
print ("Scan Common Ports --- 1")
print ("Scan Range ---------- 2")
print ("Scan All ------------ 3")
choice = input ("-" * 60 + "\n")

top10 = (20,21,22,23,25,53,80,95,107,110,119,123,135,137,138,139,143,161,194,443,1433,1434)
openp = ["Ports Open: "]
cusrange = []
allpo = []
total = ""
totaltime = ""

def commonports(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((serverip, port))
        if result == 0:
            openp.append("{}".format(port))
        sock.close()

    except KeyboardInterrupt:
        print ("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print ('Hostname could not be resolved. Exiting')
        sys.exit()

    except socket.error:
        print ("Couldn't connect to server")
        sys.exit()
        
    return openp

def rangep(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((serverip, port))
        if result == 0:
            openp.append("Port {}: Open".format(port))
        sock.close()

    except KeyboardInterrupt:
        print ("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print ('Hostname could not be resolved. Exiting')
        sys.exit()

    except socket.error:
        print ("Couldn't connect to server")
        sys.exit()
        
    return openp
    
def allp(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((serverip, port))
        if result == 0:
            openp.append("Port {}: Open".format(port))
        sock.close()

    except KeyboardInterrupt:
        print ("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print ('Hostname could not be resolved. Exiting')
        sys.exit()

    except socket.error:
        print ("Couldn't connect to server")
        sys.exit()

    return openp

if choice == "1":
    pool = ThreadPool(22)
    print ("-" * 60)
    print ("Please wait, scanning ", serverip)
    print ("-" * 60)
    starttime = datetime.now()
    results = pool.map(commonports, top10)
    pool.close()
    pool.join()
    endtime = datetime.now()
    totaltime = endtime-starttime
    print (openp)
    print ("Scan Completed in: ", totaltime)
elif choice == "2":
    startport = input("Start Port: \n")
    endport = input("End Port: \n")
    s = int(startport)
    e = int(endport)
    for x in range(s,e+1):
        cusrange.append(x)
    pool = ThreadPool(100)
    print ("-" * 60)
    print ("Please wait, scanning ", serverip)
    print ("-" * 60)
    starttime = datetime.now()
    results = pool.map(rangep, cusrange)
    pool.close()
    pool.join()
    endtime = datetime.now()
    totaltime = endtime-starttime
    print (openp)
    print ("Scan Completed in: ", totaltime)
elif choice == "3":
    pool = ThreadPool(120)
    for x in range(1,49151):
        allpo.append(x)
    print ("-" * 60)
    print ("Please wait, scanning ", serverip)
    print ("-" * 60)
    starttime = datetime.now()
    results = pool.map(allp, allpo)
    pool.close()
    pool.join()
    endtime = datetime.now()
    totaltime = endtime-starttime
    print (openp)
    print ("Scan Completed in: ", totaltime)
else:
    print("Not a valid option!")
    exit
