
import socket
import os
import tkMessageBox as tkmb
addr = socket.gethostbyname(socket.gethostname())
ip = '192.168.0.193' #put your ip addres between the ''
if ip == 'ip goes here':
        tkmb.showinfo("Alert", "You must specify an ip addres on line 5, have read the instructions?")
        os._exit(1)
fake=['guzzoni.apple.com', ip]

def fake_ip(domain,fake):
	count=len(fake)-1
	i=0
	while i<count:
		if domain==fake[i]:
			return fake[i+1]
		i=i+2
	try:
		return socket.gethostbyname(domain)
	except socket.error:
		print "\nServer error get ip for this domain: "+domain 
		print "\nReturn 127.0.0.1\n"
		#udps.close()
		return ip
		#exit()
		
	#return ip
	
if __name__ == '__main__':
	
	#banner


	
	count=len(fake)-1
	i=0
	while i<count:
		print("Domain: "+fake[i]+" has this fake ip:"+fake[i+1])
		i=i+2
	
	print("=====Server Started=====")	
	udps = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	udps.bind(('',53))
	
	try:
		while 1:
			data, addr = udps.recvfrom(1024)
			print "Connect to server:"+addr[0]
			dominio=''
			tipo = (ord(data[2]) >> 3) & 15   # Opcode bits
			if tipo == 0:                     # Standard query
				ini=12
				lon=ord(data[ini])
			while lon != 0:
				dominio+=data[ini+1:ini+lon+1]+'.'
				ini+=lon+1
				lon=ord(data[ini])
			#packet dns
			packet=''
			if dominio:
				ip=fake_ip(dominio[:-1],fake)
				
				packet+=data[:2] + "\x81\x80"
				packet+=data[4:6] + data[4:6] + '\x00\x00\x00\x00'   # Questions and Answers Counts
				packet+=data[12:]                                         # Original Domain Name Question
				packet+='\xc0\x0c'                                             # Pointer to domain name
				packet+='\x00\x01\x00\x01\x00\x00\x00\x3c\x00\x04'             # Response type, ttl and resource data length -> 4 bytes
				packet+=str.join('',map(lambda x: chr(int(x)), ip.split('.'))) # 4bytes of IP
			#dns	
			
			udps.sendto(packet, addr)
			print 'Request: %s and response with -> %s' % (dominio[:-1], ip)
			
	except KeyboardInterrupt:
		print '\n=====Shutting down Server=====\ngood bye\n'
		udps.close()
