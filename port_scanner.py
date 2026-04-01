import socket

popularPorts = [21, 22, 25, 53, 80, 443];

def searchPorts(ports, verbose):
	for port in ports:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
		sock.settimeout(0.1);

		res = sock.connect_ex((ipAddress, port));

		if res == 0:
			print(f"Port {port} is open.");

		if res != 0 and verbose == "y":
			print(f"Port {port} is closed.");

ipAddress = input("IP address to scan: ");
verbose = input("Enable verbose mode y/n: ").lower();

while True:
	mode = int(input("Scan mode - 1 (Popular ports) or 2 (Custom) or 3 (All ports): "));

	match mode:
		case 1:
			searchPorts(popularPorts, verbose);
			break;
		case 2:
			customPorts = input("Enter ports separated by , : ").split(",");
			customPorts = map(int, customPorts);
			searchPorts(customPorts, verbose);
			break;
		case 3:
			searchPorts(range(1, 1024), verbose);
			break;
		case _:
			print("Invalid selection");
			continue;
