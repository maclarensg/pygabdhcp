#!/usr/bin/python

import struct
import types


# Constants
# DHCP MESSAGE TYPE
DISCOVER = 1
OFFER = 2 
REQUEST = 3
DECLINE = 4
ACK = 5
NACK = 6
RELEASE = 7
INFORM = 8 
FORCERENEW = 9 
LEASEQUERY = 10
LEASEUNASSIGNED = 11
LEASEUNKNOWN = 12 
LEASEACTIVE = 13


# Constants
PAD = 0
SUBNET_MASK = 1
TIME_OFFSET = 2
ROUTERS = 3
TIME_SERVERS = 4
NAME_SERVERS = 5
DOMAIN_NAME_SERVERS = 6      
LOG_SERVERS = 7              
COOKIE_SERVERS = 8               
LPR_SERVERS = 9
IMPRESS_SERVERS = 10          
RESOURCE_LOCATION_SERVERS = 11
HOST_NAME = 12                
BOOT_SIZE = 13             
MERIT_DUMP = 14                 
DOMAIN_NAME = 15                
SWAP_SERVER = 16                 
ROOT_PATH = 17                  
EXTENSIONS_PATH = 18
IP_FORWARDING = 19
NON_LOCAL_SOURCE_ROUTING = 20
POLICY_FILTER = 21
MAX_DGRAM_REASSEMBLY = 22
DEFAULT_IP_TTL = 23
PATH_MTU_AGING_TIMEOUT = 24
PATH_MTU_PLATEAU_TABLE = 25
INTERFACE_MTU = 26
ALL_SUBNETS_LOCAL = 27
BROADCAST_ADDRESS = 28
PERFORM_MASK_DISCOVERY = 29
MASK_SUPPLIER = 30
ROUTER_DISCOVERY = 31
ROUTER_SOLICITATION_ADDRESS = 32
STATIC_ROUTES = 33
TRAILER_ENCAPSULATION = 34
ARP_CACHE_TIMEOUT = 35
IEEE802_3_ENCAPSULATION = 36
DEFAULT_TCP_TTL = 37
TCP_KEEPALIVE_INTERVAL = 38
TCP_KEEPALIVE_GARBAGE = 39
NIS_SERVERS = 41
NTP_SERVERS = 42
VOR_ENCAPSULATED_OPTIONS = 43
NETBIOS_NAME_SERVERS = 44
NETBIOS_DD_SERVER = 45
NETBIOS_NODE_TYPE = 46
NETBIOS_SCOPE = 47
FONT_SERVERS = 48
X_DISPLAY_MANAGER = 49
DHCP_REQUESTED_ADDRESS = 50
DHCP_LEASE_TIME = 51
DHCP_OPTION_OVERLOAD = 52
DHCP_MESSAGE_TYPE = 53
DHCP_SERVER_IDENTIFIER = 54
DHCP_PARAMETER_REQUEST_LIST = 55
DHCP_MESSAGE = 56
DHCP_MAX_MESSAGE_SIZE = 57
DHCP_RENEWAL_TIME = 58
DHCP_REBINDING_TIME = 59
VENDOR_CLASS_IDENTIFIER = 60
DHCP_CLIENT_IDENTIFIER = 61
NWIP_DOMAIN_NAME = 62					# rfc 2242
NWIP_SUBOPTIONS = 63					# rfc 2242
NISPLUS_DOMAIN = 64
NISPLUS_SERVER = 65
TFTP_SERVER = 66
BOOTFILE = 67
MOBILE_IP_HOME_AGENT = 68
SMTP_SERVER = 69
POP3_SERVER = 70
NNTP_SERVER = 71
WWW_SERVER = 72
FINGER_SERVER = 73
IRC_SERVER = 74
STREETTALK_SERVER = 75
STDA_SERVER = 76
USER_CLASS = 77						# rfc 3004
FQDN = 81
DHCP_AGENT_OPTIONS = 82					# rfc 3046
NDS_SERVERS = 85					# rfc 2241
NDS_TREE_NAME = 86					# rfc 2241
NDS_CONTEXT = 87					# rfc 2241
CLIENT_LAST_TRANSACTION_TIME  = 91			# rfc 4388
ASSOCIATED_IP = 92					# rfc 4388
USER_AUTHENTICATION_PROTOCOL = 98
AUTO_CONFIGURE = 116    
NAME_SERVICE_SEARCH = 117				# rfc 2937        
SUBNET_SELECTION = 118					# rfc 3011
DOMAIN_SEARCH = 119					# rfc 3397
CLASSLESS_ROUTE = 121					# rfc 3442
ENDPAD = -1

REFERENCE = {
	0 : "PAD",  
	1 : "SUBNET_MASK",  
	2 : "TIME_OFFSET",  
	3 : "ROUTERS",  
	4 : "TIME_SERVERS",  
	5 : "NAME_SERVERS",  
	6 : "DOMAIN_NAME_SERVERS",  
	7 : "LOG_SERVERS",  
	8 : "COOKIE_SERVERS",  
	9 : "LPR_SERVERS",  
	10 : "IMPRESS_SERVERS",  
	11 : "RESOURCE_LOCATION_SERVERS",  
	12 : "HOST_NAME",  
	13 : "BOOT_SIZE",  
	14 : "MERIT_DUMP",  
	15 : "DOMAIN_NAME",  
	16 : "SWAP_SERVER",  
	17 : "ROOT_PATH",  
	18 : "EXTENSIONS_PATH",  
	19 : "IP_FORWARDING",  
	20 : "NON_LOCAL_SOURCE_ROUTING",  
	21 : "POLICY_FILTER",  
	22 : "MAX_DGRAM_REASSEMBLY",  
	23 : "DEFAULT_IP_TTL",  
	24 : "PATH_MTU_AGING_TIMEOUT",  
	25 : "PATH_MTU_PLATEAU_TABLE",  
	26 : "INTERFACE_MTU",  
	27 : "ALL_SUBNETS_LOCAL",  
	28 : "BROADCAST_ADDRESS",  
	29 : "PERFORM_MASK_DISCOVERY",  
	30 : "MASK_SUPPLIER",  
	31 : "ROUTER_DISCOVERY",  
	32 : "ROUTER_SOLICITATION_ADDRESS",  
	33 : "STATIC_ROUTES",  
	34 : "TRAILER_ENCAPSULATION",  
	35 : "ARP_CACHE_TIMEOUT",  
	36 : "IEEE802_3_ENCAPSULATION",  
	37 : "DEFAULT_TCP_TTL",  
	38 : "TCP_KEEPALIVE_INTERVAL",  
	39 : "TCP_KEEPALIVE_GARBAGE",  
	41 : "NIS_SERVERS",  
	42 : "NTP_SERVERS",  
	43 : "VOR_ENCAPSULATED_OPTIONS",  
	44 : "NETBIOS_NAME_SERVERS",  
	45 : "NETBIOS_DD_SERVER",  
	46 : "NETBIOS_NODE_TYPE",  
	47 : "NETBIOS_SCOPE",  
	48 : "FONT_SERVERS",  
	49 : "X_DISPLAY_MANAGER",  
	50 : "DHCP_REQUESTED_ADDRESS",  
	51 : "DHCP_LEASE_TIME",  
	52 : "DHCP_OPTION_OVERLOAD",  
	53 : "DHCP_MESSAGE_TYPE",  
	54 : "DHCP_SERVER_IDENTIFIER",  
	55 : "DHCP_PARAMETER_REQUEST_LIST",  
	56 : "DHCP_MESSAGE",  
	57 : "DHCP_MAX_MESSAGE_SIZE",  
	58 : "DHCP_RENEWAL_TIME",  
	59 : "DHCP_REBINDING_TIME",  
	60 : "VENDOR_CLASS_IDENTIFIER",  
	61 : "DHCP_CLIENT_IDENTIFIER",  
	62 : "NWIP_DOMAIN_NAME",  
	63 : "NWIP_SUBOPTIONS",  
	64 : "NISPLUS_DOMAIN",  
	65 : "NISPLUS_SERVER",  
	66 : "TFTP_SERVER",  
	67 : "BOOTFILE",  
	68 : "MOBILE_IP_HOME_AGENT",  
	69 : "SMTP_SERVER",  
	70 : "POP3_SERVER",  
	71 : "NNTP_SERVER",  
	72 : "WWW_SERVER",  
	73 : "FINGER_SERVER",  
	74 : "IRC_SERVER",  
	75 : "STREETTALK_SERVER",  
	76 : "STDA_SERVER",  
	77 : "USER_CLASS",  
	81 : "FQDN",  
	82 : "DHCP_AGENT_OPTIONS",  
	85 : "NDS_SERVERS",  
	86 : "NDS_TREE_NAME",  
	87 : "NDS_CONTEXT",  
	91 : "CLIENT_LAST_TRANSACTION_TIME",  
	92 : "ASSOCIATED_IP",  
	98 : "USER_AUTHENTICATION_PROTOCOL",  
	116 : "AUTO_CONFIGURE",  
	117 : "NAME_SERVICE_SEARCH",  
	118 : "SUBNET_SELECTION",  
	119 : "DOMAIN_SEARCH",  
	121 : "CLASSLESS_ROUTE",  
	-1 : "ENDPAD"
}

DHCP_MSG_TYPE = {
        1 : "DISCOVER",
        2 : "OFFER",
        3 : "REQUEST",
        4 : "DECLINE",
        5 : "ACK",
        6 : "NACK",
        7 : "RELEASE",
        8 : "INFORM",
        9 : "FORCERENEW",
        10 : "LEASEQUERY",
        11 : "LEASEUNASSIGNED",
        12 : "LEASEUNKNOWN",
        13 : "LEASEACTIVE",
}

def content_to_ip(content): 
        ipaddr = struct.unpack("BBBB", content)
        return ipaddr

def content_to_ip_list(content):
	if (len(content) < 4):
		print "Content len %s" % len(content)
		return []
        if ( len(content)%4 != 0 ):
                return []
        i=0
        list = [] 
        while i < len(content):
               	list.append(content_to_ip(content[i:i+4]))
               	i += 4
        return list  

def convert_to_ip_str(val):
	return ".".join(map(str,val))


def list_to_str(list):
        return "".join(list)

# DhcpOption 
class DhcpOption:

	def __init__(self):
		self.data = []
	
	def __str__(self):
		code = self.get_code() 
		length = self.get_length()
		value = self.get_value()

		value_str = ""
		if type(value) is types.StringType:
			value_str = value
		if type(value) is types.IntType:
			value_str = "%s" % value
		if type(value) is types.TupleType:
			value_str =  convert_to_ip_str(value) 
		if type(value) is types.ListType:
			value_str = ", ".join(map(convert_to_ip_str, value))

		return_string =  "%s (%s): length = %s, content = %s" % (REFERENCE[code], code, length, value_str )
		if code == 53:
			return_string += " (%s)" % DHCP_MSG_TYPE[value]
		return return_string

	def set_code(self, code):
		self.data[0] = struct.pack('b', code)
	
	def set_data(self, data):
		self.data = data
	
	def get_code(self):
		return struct.unpack('b', self.data[0])[0]
	
	def get_content(self):
		code = struct.unpack('b', self.data[0])[0]
		length = struct.unpack('B', self.data[1])[0]
		return list_to_str( self.data[2:2+len(self.data)] )
	
	def get_value(self):
		length = self.get_length()
		code = self.get_code() 

		if code == 12: return self.get_content()
		if code == 14: return self.get_content()
		if code == 15: return self.get_content()
		if code == 17: return self.get_content()
		if code == 18: return self.get_content()
		if code == 47: return self.get_content()
		if code == 56: return self.get_content()
		if code == 60: return self.get_content()
		if code == 61: return self.get_content()
		if code == 62: return self.get_content()
		if code == 64: return self.get_content()
		if code == 65: return self.get_content()
		if code == 66: return self.get_content()
		if code == 67: return self.get_content()
		if code == 86: return self.get_content()
		if code == 98: return self.get_content()
		
		if code == 19: return struct.unpack('B', self.get_content())[0]
		if code == 20: return struct.unpack('B', self.get_content())[0]
		if code == 23: return struct.unpack('B', self.get_content())[0]
		if code == 27: return struct.unpack('B', self.get_content())[0]
		if code == 29: return struct.unpack('B', self.get_content())[0]
		if code == 30: return struct.unpack('B', self.get_content())[0]
		if code == 31: return struct.unpack('B', self.get_content())[0]
		if code == 34: return struct.unpack('B', self.get_content())[0]
		if code == 36: return struct.unpack('B', self.get_content())[0]
		if code == 37: return struct.unpack('B', self.get_content())[0]
		if code == 39: return struct.unpack('B', self.get_content())[0]
		if code == 46: return struct.unpack('B', self.get_content())[0]
		if code == 52: return struct.unpack('B', self.get_content())[0]
		if code == 53: return struct.unpack('B', self.get_content())[0]
		if code == 116: return struct.unpack('B', self.get_content())[0]
		
		if code == 13: return struct.unpack('H', self.get_content())[0]
		if code == 22: return struct.unpack('H', self.get_content())[0]
		if code == 26: return struct.unpack('H', self.get_content())[0]
		if code == 57: return struct.unpack('H', self.get_content())[0]
	
		if code == 2: return struct.unpack('I', self.get_content())[0]
		if code == 24: return struct.unpack('I', self.get_content())[0]
		if code == 35: return struct.unpack('I', self.get_content())[0]
		if code == 38: return struct.unpack('I', self.get_content())[0]
		if code == 51: return struct.unpack('I', self.get_content())[0]
		if code == 58: return struct.unpack('I', self.get_content())[0]
		if code == 59: return struct.unpack('I', self.get_content())[0]

		if code == 1: return content_to_ip(self.get_content()) 
		if code == 16: return content_to_ip(self.get_content())
		if code == 28: return content_to_ip(self.get_content())
		if code == 32: return content_to_ip(self.get_content())
		if code == 50: return content_to_ip(self.get_content())
		if code == 54: return content_to_ip(self.get_content())
		if code == 118: return content_to_ip(self.get_content())

		if code == 3: return content_to_ip_list(self.get_content())
		if code == 4: return content_to_ip_list(self.get_content())
		if code == 5: return content_to_ip_list(self.get_content())
		if code == 6: return content_to_ip_list(self.get_content())
		if code == 7: return content_to_ip_list(self.get_content())
		if code == 8: return content_to_ip_list(self.get_content())
		if code == 9: return content_to_ip_list(self.get_content())
		if code == 10: return content_to_ip_list(self.get_content())
		if code == 11: return content_to_ip_list(self.get_content())
		if code == 21: return content_to_ip_list(self.get_content())
		if code == 33: return content_to_ip_list(self.get_content())
		if code == 41: return content_to_ip_list(self.get_content())
		if code == 42: return content_to_ip_list(self.get_content())
		if code == 44: return content_to_ip_list(self.get_content())
		if code == 45: return content_to_ip_list(self.get_content())
		if code == 48: return content_to_ip_list(self.get_content())
		if code == 49: return content_to_ip_list(self.get_content())
		if code == 68: return content_to_ip_list(self.get_content())
		if code == 69: return content_to_ip_list(self.get_content())
		if code == 70: return content_to_ip_list(self.get_content())
		if code == 71: return content_to_ip_list(self.get_content())
		if code == 72: return content_to_ip_list(self.get_content())
		if code == 73: return content_to_ip_list(self.get_content())
		if code == 74: return content_to_ip_list(self.get_content())
		if code == 75: return content_to_ip_list(self.get_content())
		if code == 76: return content_to_ip_list(self.get_content())
		if code == 85: return content_to_ip_list(self.get_content())
		return None  
			
	def get_length(self):
		return struct.unpack('B', self.data[1])[0]

	def pack(self):
		return list_to_str( self.data )

def marshall(bytes):
        option = DhcpOption()
        option.set_data(bytes)
        return option

# This method is allowed for the following option codes:
# HOST_NAME(12)
# MERIT_DUMP(14)
# DOMAIN_NAME(15)
# ROOT_PATH(17)
# EXTENSIONS_PATH(18)
# NETBIOS_SCOPE(47)
# DHCP_MESSAGE(56)
# VENDOR_CLASS_IDENTIFIER(60)
# NWIP_DOMAIN_NAME(62)
# NISPLUS_DOMAIN(64)
# NISPLUS_SERVER(65)
# TFTP_SERVER(66)
# BOOTFILE(67)
# NDS_TREE_NAME(86)
# USER_AUTHENTICATION_PROTOCOL(98)

def new_string_option(code, string):
	option = DhcpOption()
	option.set_data( struct.pack('b', code) + struct.pack('B', len(string)) + string );
	return option

# IP_FORWARDING(19)
# NON_LOCAL_SOURCE_ROUTING(20)
# DEFAULT_IP_TTL(23)
# ALL_SUBNETS_LOCAL(27)
# PERFORM_MASK_DISCOVERY(29)
# MASK_SUPPLIER(30)
# ROUTER_DISCOVERY(31)
# TRAILER_ENCAPSULATION(34)
# IEEE802_3_ENCAPSULATION(36)
# DEFAULT_TCP_TTL(37)
# TCP_KEEPALIVE_GARBAGE(39)
# NETBIOS_NODE_TYPE(46)
# DHCP_OPTION_OVERLOAD(52)
# DHCP_MESSAGE_TYPE(53)
# AUTO_CONFIGURE(116)

def new_byte_option(code, value):
	option = DhcpOption()
	option.set_data( struct.pack('b', code) + "\001" + struct.pack('B', value) ) 
	return option

# BOOT_SIZE(13)
# MAX_DGRAM_REASSEMBLY(22)
# INTERFACE_MTU(26)
# DHCP_MAX_MESSAGE_SIZE(57)

def new_short_option(code, value):
	option = DhcpOption()
	option.set_data( struct.pack('b', code) + "\002" + struct.pack('H', value) )
	return option

# Create a DHCP Option as Int Format
#
# IME_OFFSET(2)
# DHCPOPTION_PATH_MTU_AGING_TIMEOUT(24)
# DHCPOPTION_ARP_CACHE_TIMEOUT(35)
# CP_KEEPALIVE_INTERVAL(38)
# DHCPOPTION_DHCP_LEASE_TIME(51)
# DHCPOPTION_DHCP_RENEWAL_TIME(58)
# DHCPOPTION_DHCP_REBINDING_TIME(59)

def new_int_option(code, value):
	option = DhcpOption()
        option.set_data( struct.pack('b', code) + "\004" + struct.pack('I', value) )
        return option


# Create a DHCP Option with Inet Address Format         
#       
# This method is allowed for the following option codes:
# SUBNET_MASK(1)
# SWAP_SERVER(16)
# BROADCAST_ADDRESS(28)
# ROUTER_SOLICITATION_ADDRESS(32)
# DHCP_REQUESTED_ADDRESS(50)
# DHCP_SERVER_IDENTIFIER(54)
# SUBNET_SELECTION(118)      
#               
# and also as a simplified version for setOptionAsInetAddresses
# ROUTERS(3)
# TIME_SERVERS(4)
# NAME_SERVERS(5)
# DOMAIN_NAME_SERVERS(6)
# LOG_SERVERS(7)
# COOKIE_SERVERS(8)
# LPR_SERVERS(9)
# IMPRESS_SERVERS(10)
# RESOURCE_LOCATION_SERVERS(11)
# POLICY_FILTER(21)
# STATIC_ROUTES(33)
# NIS_SERVERS(41)
# NTP_SERVERS(42)
# NETBIOS_NAME_SERVERS(44)
# NETBIOS_DD_SERVER(45)
# FONT_SERVERS(48)
# X_DISPLAY_MANAGER(49)
# MOBILE_IP_HOME_AGENT(68)
# SMTP_SERVER(69)
# POP3_SERVER(70)
# NNTP_SERVER(71)
# WWW_SERVER(72)
# FINGER_SERVER(73)
# IRC_SERVER(74)
# STREETTALK_SERVER(75)
# STDA_SERVER(76)
# NDS_SERVERS(85)

def new_inet_addr_option(code, addr):
	bytes = ""
        for tuple in addr.split('.'):
                bytes += struct.pack('B', int(tuple))
        option = DhcpOption()
        option.set_data( struct.pack('b', code) + "\004" + bytes )
	return option 

	
# Create a DHCP Option with an array of Inet Addresses
#
# This method is allowed for the following option codes:
#
# ROUTERS(3)
# TIME_SERVERS(4)
# NAME_SERVERS(5)
# DOMAIN_NAME_SERVERS(6)
# LOG_SERVERS(7)
# COOKIE_SERVERS(8)
# LPR_SERVERS(9)
# IMPRESS_SERVERS(10)
# RESOURCE_LOCATION_SERVERS(11)
# POLICY_FILTER(21)
# STATIC_ROUTES(33)
# NIS_SERVERS(41)
# NTP_SERVERS(42)
# NETBIOS_NAME_SERVERS(44)
# NETBIOS_DD_SERVER(45)
# FONT_SERVERS(48)
# X_DISPLAY_MANAGER(49)
# MOBILE_IP_HOME_AGENT(68)
# SMTP_SERVER(69)
# POP3_SERVER(70)
# NNTP_SERVER(71)
# WWW_SERVER(72)
# FINGER_SERVER(73)
# IRC_SERVER(74)
# STREETTALK_SERVER(75)
# STDA_SERVER(76)
# NDS_SERVERS(85)

def new_inet_addrs_option(code, addrs):
	bytes = ""
	for addr in addrs.split(','):
		tuples = addr.split(".")
		if len(tuples) == 4:
			for tuple in tuples:
				bytes += struct.pack('B', int(tuple))
	option = DhcpOption()
        option.set_data( struct.pack('b', code) + struct.pack('B', len(bytes)) + bytes )
        return option


	
		

	
