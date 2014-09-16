#from xml.sax import *

from lxml import etree
import binascii
tree = etree.parse('gwlist.xml')

#data = [binascii.unhexlify(e.get("value")) for e in tree.xpath('/pdml/packet/proto[@name="olsr"]/field[@name="olsr.packet_seq_num"]')]

#for e in tree.xpath('/pdml/packet/proto[@name="olsr"]/field[@name="olsr.packet_seq_num"]'):

#for e in tree.xpath('/pdml/packet/proto[@name="olsr"]/field[@name="olsr.message"]/field[@name="olsr.message_type" and @value="04"]'):

originatorset = set()

for f in tree.xpath('/pdml/packet/proto[@name="olsr"]/field[@name="olsr.message"]'):
    o = ""
    for e in f:
        propname = e.get("name").replace(".","_")
        propvalue = e.get("show")
        if propname == "olsr_message_type" and propvalue != "4":
            break
        if propname == "olsr_origin_addr":
            o = propvalue
        elif propname == "olsr_network_addr":
            if propvalue == "0.0.0.0":
                originatorset.add(o)

print originatorset

