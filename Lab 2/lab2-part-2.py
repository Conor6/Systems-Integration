import dns
import sys

#Part 2
import sys

#Part 2
s = sys.argv[1]
print(s.split('.'))

question = dns.DNSQuestion(
    #Part 2
    qname = s.split('.'),
    qtype = 1,
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

for answer in r.answers:
    print(f'{answer.rdata[0]}.{answer.rdata[1]}.{answer.rdata[2]}.{answer.rdata[3]}')


