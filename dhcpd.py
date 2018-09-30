from lib import dhcpoption, dhcppacket
import random
import struct
import socket
import copy
import select
	
# Constant 
MAXLENGTH = 1500

# Loading configs to create packet templates
OFFER_TEMPLATE = dhcppacket.DhcpPacket()
OFFER_TEMPLATE.set_op(dhcppacket.BOOTREPLY)
OFFER_TEMPLATE.set_htype(dhcppacket.ETHER)
OFFER_TEMPLATE.add_option(dhcpoption.new_byte_option(dhcpoption.DHCP_MESSAGE_TYPE, dhcpoption.OFFER))
OFFER_TEMPLATE.add_option(dhcpoption.new_inet_addr_option(dhcpoption.DHCP_SERVER_IDENTIFIER, "202.166.119.145"))

# set default lease time 
default_lease_time = 65536;
OFFER_TEMPLATE.add_option(dhcpoption.new_int_option(dhcpoption.DHCP_LEASE_TIME, default_lease_time))

# T1/T2
OFFER_TEMPLATE.add_option(dhcpoption.new_int_option(dhcpoption.DHCP_RENEWAL_TIME, int(default_lease_time * 0.5)) )
OFFER_TEMPLATE.add_option(dhcpoption.new_int_option(dhcpoption.DHCP_REBINDING_TIME, int(default_lease_time * 0.875)) )

# Set Domain Name Servers
OFFER_TEMPLATE.add_option(dhcpoption.new_inet_addrs_option(dhcpoption.DOMAIN_NAME_SERVERS, "165.21.100.88, 165.21.83.88"))

# Set Routers
OFFER_TEMPLATE.add_option(dhcpoption.new_inet_addrs_option(dhcpoption.ROUTERS, "192.168.1.254"))

# Set Netmask
OFFER_TEMPLATE.add_option(dhcpoption.new_inet_addr_option(dhcpoption.SUBNET_MASK, "255.255.255.0"))

# Loading configs to create packet templates
ACK_TEMPLATE = dhcppacket.DhcpPacket()
ACK_TEMPLATE.set_op(dhcppacket.BOOTREPLY)
ACK_TEMPLATE.set_htype(dhcppacket.ETHER)
ACK_TEMPLATE.add_option(dhcpoption.new_byte_option(dhcpoption.DHCP_MESSAGE_TYPE, dhcpoption.ACK))
ACK_TEMPLATE.add_option(dhcpoption.new_inet_addr_option(dhcpoption.DHCP_SERVER_IDENTIFIER, "202.166.119.145"))

# set default lease time 
default_lease_time = 65536;
ACK_TEMPLATE.add_option(dhcpoption.new_int_option(dhcpoption.DHCP_LEASE_TIME, default_lease_time))

# T1/T2
ACK_TEMPLATE.add_option(dhcpoption.new_int_option(dhcpoption.DHCP_RENEWAL_TIME, int(default_lease_time * 0.5)) )
ACK_TEMPLATE.add_option(dhcpoption.new_int_option(dhcpoption.DHCP_REBINDING_TIME, int(default_lease_time * 0.875)) )

# Set Domain Name Servers
ACK_TEMPLATE.add_option(dhcpoption.new_inet_addrs_option(dhcpoption.DOMAIN_NAME_SERVERS, "165.21.100.88, 165.21.83.88"))

# Set Routers
ACK_TEMPLATE.add_option(dhcpoption.new_inet_addrs_option(dhcpoption.ROUTERS, "192.168.1.254"))

# Set Netmask
ACK_TEMPLATE.add_option(dhcpoption.new_inet_addr_option(dhcpoption.SUBNET_MASK, "255.255.255.0"))

REQUEST_CACHE = {}

AUTHORATATIVE = (192,168,1,0)
INTERFACE_MASK = (255,255,255,0)
NETWORKS = [ [(192,168,1,0),(255,255,255,0)]]

def do_offer(in_packet):
	out_packet = copy.deepcopy(OFFER_TEMPLATE)

	xid = in_packet.get_xid_raw() 
	out_packet.set_xid_raw( xid )

	out_packet.set_flags_raw( in_packet.get_flags_raw() )

	chaddr = in_packet.get_chaddr_raw()
	out_packet.set_chaddr_raw( chaddr )
		
	# Assign IP
	out_packet.set_yiaddr( (192,168,1,1) )
	REQUEST_CACHE["%s%s" % (chaddr,xid)] = (192,168,1,1) 

	return out_packet 

def do_ack(in_packet):
	out_packet = copy.deepcopy(ACK_TEMPLATE)
	xid = in_packet.get_xid_raw() 
	chaddr = in_packet.get_chaddr_raw()
	
	if REQUEST_CACHE.has_key("%s%s" % (chaddr,xid)):
		ip = REQUEST_CACHE["%s%s" % (chaddr,xid)]
		out_packet.set_xid_raw( xid )
		out_packet.set_flags_raw( in_packet.get_flags_raw() )
		out_packet.set_chaddr_raw( chaddr )
		out_packet.set_yiaddr( ip )
	return out_packet

def do_release(in_packet):
	return

def do_inform(in_packet):
	return

def handle(req_packet):
	if (req_packet.get_op() == dhcppacket.BOOTREQUEST): 

		if not (req_packet.is_dhcp):
			print "Not DHCP, BootP not supported"
			return

		msg_type_option = req_packet.get_option(dhcpoption.DHCP_MESSAGE_TYPE)
		msg_type = msg_type_option.get_value()

		if msg_type == dhcpoption.DISCOVER:
			return do_offer(req_packet)

		if msg_type == dhcpoption.OFFER: 
			print "Invalid Packet"	
			return 

		if msg_type == dhcpoption.REQUEST:
			return do_ack(req_packet)

		if msg_type == dhcpoption.DECLINE:
			print "Invalid Packet"	
			return 

		if msg_type == dhcpoption.ACK:
			print "Invalid Packet"	
			return 

		if msg_type == dhcpoption.NACK:
			print "Invalid Packet"	
			return 

                if msg_type == dhcpoption.RELEASE:
			return do_release(req_packet) 

                if msg_type == dhcpoption.INFORM:
			return do_inform(req_packet) 

                if msg_type == dhcpoption.FORCERENEW:
			print "Invalid Packet"	
			return 

                if msg_type == dhcpoption.LEASEQUERY:
			return

                if msg_type == dhcpoption.LEASEUNASSIGNED:
			return

                if msg_type == dhcpoption.LEASEUNKNOWN:
			return

                if msg_type == dhcpoption.LEASEACTIVE:
			return

			
	else:
		print "Invalid DHCP Request"
		return

# Setup up udp socket 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) 
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
sock.bind(('', 67))

sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock1.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) 
sock1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
sock1.bind(('192.168.1.115', 67))

socks = [sock1,sock]
while 1:
	try:
		inputready, outputready, exceptready = select.select(socks, [], [])
	except select.error, e:
		break
	except socket.error, e:
		break

	for s in inputready:

		if s == sock1:
			print "192.168.1.115"
		else:
			print "0.0.0.0"

		data, addr = s.recvfrom(MAXLENGTH)
		req_packet = dhcppacket.marshall(data)

		print "From: %s:%d" % (addr[0], addr[1])
		print req_packet	
	
		if addr[0] == "0.0.0.0":
			addr =("255.255.255.255", addr[1])
	
		resp_packet = handle(req_packet)
		if resp_packet:
			print resp_packet
			s.sendto(resp_packet.pack(), addr)
	
		print "-" * 100


