import os

used = []
notUsed = []
net = input("Network > ") 
## Input Network as XXX.XXX.XXX***  EX. => 192.168.10
## This will cover the /24 subnet.

def pingSweep(network):
	"""Ping's Subnets via CMD
	
	The loop appends the last . and octet from
	1 to 254 and pings the ip individually.
	replace the -n with -c for LINUX or MAC
	
	Args:
		network: XXX.XXX.XXX
	
	Return:
		used:	 List of assigned IP addresses
		notUsed: List of unassigned IP addresses
	"""
	for i in range(1, 254):			
		result = str.join('.', (net, str(i)))
		if os.system("ping -n 1 %s" % result) == 0: 	
			used.append(result)
		else:
			notUsed.append(result)

def report():
	"""
	"""
	print("Addresses in use")
	print("*" * 20)
	for i in used:
		print(i)

	print("\nAddresses NOT in use")
	print("*" * 20)
	for i in notUsed:
		print(i)


def main():
	pingSweep(net)
	report()


if __name__ == '__main__':
	main()
