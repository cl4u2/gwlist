#from xml.sax import *

from lxml import etree
import binascii
tree = etree.parse('gwlist.xml')

#data = [binascii.unhexlify(e.get("value")) for e in tree.xpath('/pdml/packet/proto[@name="olsr"]/field[@name="olsr.packet_seq_num"]')]

#for e in tree.xpath('/pdml/packet/proto[@name="olsr"]/field[@name="olsr.packet_seq_num"]'):

#for e in tree.xpath('/pdml/packet/proto[@name="olsr"]/field[@name="olsr.message"]/field[@name="olsr.message_type" and @value="04"]'):

class OlsrMessage:
    pass

msglist = []

for f in tree.xpath('/pdml/packet/proto[@name="olsr"]/field[@name="olsr.message"]'):
    m = OlsrMessage()
    for e in f:
        propname = e.get("name").replace(".","_")
        setattr(m, propname, e.get("show"))
    msglist.append(m)
        
hnas = [m for m in msglist if m.olsr_message_type == "4"]

gws = [h for h in hnas if h.olsr_network_addr == "0.0.0.0"]

#for g in gws:
#    print g.olsr_origin_addr, g.olsr_network_addr, g.olsr_netmask

gworiginators = list(set([g.olsr_origin_addr for g in gws]))
for o in gworiginators:
    print o


