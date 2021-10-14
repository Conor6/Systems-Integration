import dns
import sys
import sys


print("Part 3")

#Part 2
s = sys.argv[1]
print(s.split('.'))

question = dns.DNSQuestion(
    #Part 2
    qname = s.split('.'),
    qtype = 28,
    qclass = 1
)

header = dns.DNSHeader(
    ident = 100,
    qr = 0,
    opcode = 0,
    aa = 0,
    tc = 0,
    rd = 1,
    ra = 0,
    z = 0,
    rcode = 0,
    qdcount = 1,
    ancount = 0,
    nscount = 0,
    arcount = 0
)

datagram = dns.DNSDatagram(
    header = header,
    questions = [question],
    answers = []
)

datagram_bytes = dns.make_dns_datagram(datagram)

import socket

destination = ('8.8.8.8', 53)

connection = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
connection.sendto(datagram_bytes, destination)

result = connection.recvfrom(4096)[0]


#Part 1
r = dns.read_dns_datagram(result)

#print(r.answers)

print((r.answers[0].rdata).hex())
#print(r.answers[1].rdata)
#print(r.answers[2].rdata)
#print(r.answers[3].rdata)
#print(r.answers[4].rdata)
#print(r.answers[5].rdata)
#print(r.answers[6].rdata)
#print(r.answers[7].rdata)

for answer in r.answers:
   print(f'{hex(answer.rdata[0])}:{hex(answer.rdata[1])}:{hex(answer.rdata[2])}:{hex(answer.rdata[3])}')


