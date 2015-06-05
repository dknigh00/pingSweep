import os

used = []
notUsed = []
net = input("Network > ")


def pingSweep(network):
	for i in range(1, 254):
		result = str.join('.', (net, str(i)))
		if os.system("ping -c 1 %s" % result) == 0:
			used.append(result)
		else:
			notUsed.append(result)

def report():
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