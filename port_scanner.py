import socket
import csv
import re

commonPorts = {}

def searchPorts(ports):
	print("Starting scan...");
	for port in ports:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
		sock.settimeout(0.1);

		res = sock.connect_ex((ipAddress, port));

		if res == 0:
			print(f"Port {port if port not in commonPorts else f'{str(port)} ({commonPorts[port]})'} is open.");

try:
	with open("Common Ports.csv", newline="") as portsFile:
		reader = csv.DictReader(portsFile)
		for row in reader:
			key = int(row["port"])
			commonPorts[key] = row["usage"]
except FileNotFoundError:
	print("The Common Ports file could not be found.");
except PermissionError:
	print("Insufficient permissions to open Common Ports file.");
except IOError:
	print("An error occurred while reading the Common Ports file.");
	

while True:
	ipAddress = input("Enter an IPv4 address to scan: ");
	
	if re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$", ipAddress):
		break;
	else:
		print("Invalid IPv4 address. Try again.")

while True:
	mode = int(input("Scan mode - 1 (Common ports) or 2 (Custom): "));

	match mode:
		case 1:
			searchPorts(commonPorts.keys());
			break;
		case 2:
			customPorts = map(int, input("Enter ports separated by , : ").split(","));
			searchPorts(customPorts);
			break;
		case _:
			print("Invalid selection. Try again.");
			continue;
