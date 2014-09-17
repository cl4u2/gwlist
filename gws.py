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

originatorlist = list(originatorset)

for o in originatorlist:
    print "echo '----->' %s" % o
    if o.split('.')[0] == "172" or ".".join(o.split('.')[:3]) == "10.0.1":
        # special subnets
        oregex = "\.".join(o.split('.')) + "\\b.*\|"
    else:
        # other subnets, assume /24
        oregex = "\.".join(o.split('.')[:3]) + "\..*/.*\|"
    print "egrep '%s' gestioneindirizzi.txt" % oregex

