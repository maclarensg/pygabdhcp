#!/usr/bin/python
import struct
import dhcpoption

# Constants
BOOTREQUEST =  1
BOOTREPLY = 2

ETHER = 1
IEEE802 = 6
FDDI = 8
IEEE1394 = 24

BOOTP = {
	1 : "BOOTREQUEST",
	2 : "BOOTREPLY"
}
  
HTYPE = {
	1 : "ETHER",
	6 : "IEEE802",
	8 : "FDDI",
	24 : "IEEE1394"
}
        
AGENT_OPTIONS = {
	1 : "CIRCUIT_ID",
	2 : "REMOTE_ID"
}
                                                        

def convert_to_ip_str(val):
	return ".".join(map(str,val))

def list_to_str(list):
	return "".join(list)

def to_byte(value):
        return struct.pack('B', value)

def convert_to_ip(content): 
        ipaddr = struct.unpack("BBBB", content)
        return ipaddr

def convert_data_to_chaddr(content): 
        chaddr = struct.unpack("B"*len(content), content)
        return chaddr

def convert_to_hex_str(value):
        return "%02X" % value

def hex_to_int(val):
        return int(val, 16)

def convert_tuples_to_chaddr(tuples):
	return ":".join(map(convert_to_hex_str,tuples))

class DhcpPacket:
	def __init__(self):
		self.data = list("\x00"* 240)
		self.options_index = {}
		self.data[236:240] = "\x63\x82\x53\x63" 		
	
#
# OP Code byte[0:1]
#
	def get_op(self):
        	return struct.unpack('B', list_to_str(self.data[0:1]))[0]

	def get_op_raw(self):
        	return self.data[0:1]

	def set_op(self, code):
		self.data[0:1] = struct.pack('B', code)

	def set_op_raw(self, bytes):
        	self.data[0:1] = bytes

#
# Hytpe byte[1:2]
#
	def get_htype(self):
	        return struct.unpack('B', list_to_str(self.data[1:2]))[0]

	def get_htype_raw(self):
	        return self.data[1:2]

	def set_htype_raw(self, bytes):
		self.data[1:2] = bytes

	def set_htype(self, code):
		self.data[1:2] = struct.pack('B', code)


#
# Hlen byte[2:3]
#
	def get_hlen(self):
	        return struct.unpack('B', list_to_str(self.data[2:3]))[0]

	def get_hlen_raw(self):
	        return self.data[2:3]

	def set_hlen_raw(self, bytes):
		self.data[2:3] = bytes

	def set_hlen(self, code):
		self.data[2:3] = struct.pack('B', code)

#
# Hops byte[3:4]
#
	def get_hops(self):
	        return struct.unpack('B', list_to_str(self.data[3:4]))[0]

	def get_hops_raw(self):
	        return self.data[3:4]

	def set_hops_raw(self, bytes):
		self.data[3:4] = bytes

	def set_hops(self, code):
		self.data[3:4] = struct.pack('B', code)

#
# XID byte[4:8]
#
	def get_xid(self):
	        return struct.unpack('I', list_to_str(self.data[4:8]))[0]

	def get_xid_raw(self):
	        return self.data[4:8]
	
	def get_xid_hex_str(self):
		value =  self.get_xid()
		string = "%08X" % value
		return string 

	def set_xid_raw(self, bytes):
		self.data[4:8] = bytes

	def set_xid(self, id):
		self.data[4:8] = struct.pack('I', id)
	
	def set_xid_hex_str(self, hex):
		self.set_xid( int(hex, 16) )

	def match_xid(self, xid):
		return xid == self.get_xid_raw()

#
# Seconds Elapse byte[8:10]
#
	def get_secs(self):
		return struct.unpack('H', list_to_str(self.data[8:10]))[0]

	def get_secs_raw(self):
		return self.data[8:10]

	def set_secs(self, value):
		self.data[8:10] = struct.pack('H', value)

	def set_secs_raw(self, bytes):	
		self.data[8:10] = bytes 
	
#
# Flags byte[10:12]
#
	def get_flags(self):
                return struct.unpack('H', list_to_str(self.data[10:12]))[0]

        def get_flags_raw(self):
                return self.data[10:12]

        def set_flags(self, value):
                self.data[10:12] = struct.pack('H', value)

        def set_flags_raw(self, bytes):  
                self.data[10:12] = bytes

#
# Client IP ADDR bytes[12:16]
#

	def get_ciaddr(self):
                return convert_to_ip(list_to_str(self.data[12:16]))

        def get_ciaddr_raw(self):
                return self.data[12:16]

        def set_ciaddr(self, value):
                self.data[12:16] =  map(to_byte, value) 

        def set_ciaddr_raw(self, bytes):
                self.data[12:16] = bytes

#
# Your IP ADDR bytes[16:20]
#
	def get_yiaddr(self):
                return convert_to_ip(list_to_str(self.data[16:20]))

        def get_yiaddr_raw(self):
                return self.data[16:20]

        def set_yiaddr(self, value):
                self.data[16:20] =  map(to_byte, value) 

        def set_yiaddr_raw(self, bytes):
                self.data[16:20] = bytes

#
# Server IP ADDR bytes[20:24]
#
	def get_siaddr(self):
                return convert_to_ip(list_to_str(self.data[20:24]))

        def get_siaddr_raw(self):
                return self.data[20:24]

        def set_siaddr(self, value):
                self.data[20:24] =  map(to_byte, value) 

        def set_siaddr_raw(self, bytes):
                self.data[20:24] = bytes

#
# Gateway IP ADDR bytes[24:28]
#
	def get_giaddr(self):
                return convert_to_ip(list_to_str(self.data[24:28]))

        def get_giaddr_raw(self):
                return self.data[24:28]

        def set_giaddr(self, value):
                self.data[24:28] =  map(to_byte, value) 

        def set_giaddr_raw(self, bytes):
                self.data[24:28] = bytes


#
# Hardware ADDR bytes[28:44]
#
	def get_chaddr(self):
                return convert_data_to_chaddr(list_to_str(self.data[28:28+self.get_hlen()]))

	def get_chaddr_hex(self):
		return convert_tuples_to_chaddr(self.get_chaddr())

        def get_chaddr_raw(self):
                return self.data[28:28+self.get_hlen()]

        def set_chaddr(self, value):
                self.data[28:28+len(value)] =  map(to_byte, value) 
		self.set_hlen(len(value))
	
	def set_chaddr_hex(self, string):
		return self.set_chaddr(map(hex_to_int, string.split(":")))

        def set_chaddr_raw(self, bytes):
                self.data[28:28+len(bytes)] = bytes
		self.set_hlen(len(bytes))

#
# SNAME bytes[44:108]
#
	def get_sname(self):
		return list_to_str(self.data[44:108])

	def set_name(self, name):
		self.data[44:108] = name	

#
# FILE bytes[108:236]
#
	def get_file(self):
                return list_to_str(self.data[108:236])

        def set_file(self, file):
                self.data[108:236] = file 

#
# Magic Cookie
#
	def get_magic_cookie(self):
		return  struct.unpack('I', list_to_str(self.data[236:240]))[0] 
	
	def is_dhcp(self):
		 return (self.data[236:240] == list("\x63\x82\x53\x63"))

#
# pack to bytes
#
	def pack(self):
		return "".join(self.data) + "\377"

	def __str__(self):
		string = ""
		string += "OP: %s (%s)\n" % (BOOTP[self.get_op()], self.get_op())
		string += "HTYPE: %s (%s)\n" % (HTYPE[self.get_htype()], self.get_htype())
		string += "HLEN: %s\n" % (self.get_hlen())
		string += "HOPS: %s\n" % (self.get_hops())
		string += "XID: %s\n" % (self.get_xid_hex_str())
		string += "Seconds Elapsed: %s\n" % (self.get_secs())
		string += "Flags: %s\n" % (self.get_flags())
		string += "Client IP Address: %s\n" % convert_to_ip_str(self.get_ciaddr())	
		string += "Your IP Address: %s\n" % convert_to_ip_str(self.get_yiaddr())	
		string += "Server IP Address: %s\n" % convert_to_ip_str(self.get_siaddr())	
		string += "Gateway IP Address: %s\n" % convert_to_ip_str(self.get_giaddr())	
		string += "Hardware Address: %s\n" % self.get_chaddr_hex()	
		string += "Server Name: %s\n" % self.get_sname()
		string += "File: %s\n" %  self.get_file()
		string += "Magic Cookie: %X " % self.get_magic_cookie()
		if self.is_dhcp(): string += "is DHCP Packet"
		string += "\n" 
		string += "Options:\n"
		for opt in self.options_index:
			string += "\t"
			start, end = self.options_index[opt]
			option_data = self.data[start:end]
			option = dhcpoption.marshall(option_data)
			string += option.__str__()
			string += "\n"
		string += "\n"
		return string

	def add_option(self, option):
		i = len(self.data)
		code = option.get_code()
		data = option.pack()
		length = len(data)

		if self.options_index.has_key(code):
			start, end = self.options_index[code]			
			self.data[start:end] = list(data)
			i = 240
			while (i < len(self.data) ):
				code = struct.unpack('b', self.data[i])[0]
				length = 0
				
				if code == 0 or code == -1:
					i += 1
					continue	

				length = struct.unpack('B', self.data[i+1])[0]
				self.options_index[code] = [i,i+2+length]
		
				i += 2 + length

		else:
		    self.data += list(data)
	 	    self.options_index[code] = [i, i+length]

	def add_option_raw(self, bytes):
		self.add_option( dhcpoption.marshall(self.data[start:end]) )
	
	def get_option(self, code):
		start, end = self.options_index[code]
		return dhcpoption.marshall(self.data[start:end])

	def get_option_raw(self, code):
		start, end = self.options_index[code]
		return self.data[start:end]
		
		
		


def marshall(data):
	bytes = list(data)	
	packet = DhcpPacket()
	packet.data = bytes 

	i = 240
	while (i < len(bytes) ):
		
		code = struct.unpack('b', bytes[i])[0]
		length = 0
				
		if code == 0 or code == -1:
			i += 1
			continue	

		length = struct.unpack('B', bytes[i+1])[0]
		packet.options_index[code] = [i,i+2+length]
		
		i += 2 + length
	
	return packet


		
			
