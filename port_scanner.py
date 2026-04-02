import socket

commonPorts = {
	20: "FTP-data",
	21: "FTP-control",
	22: "SSH",
	23: "Telnet",
	25: "SMTP",
	53: "DNS",
	80: "HTTP",
	110: "POP3",
	143: "IMAP",
	443: "HTTPS",
	465: "SMTPS",
	1433: "MSSQL",
	3306: "MYSQL",
	3389: "RDP",
	5432: "PostgreSQL",
	5900: "VNC",
	6379: "Redis",
	8080: "HTTP-Proxy",
	8443: "HTTPS-Alt"
};

def searchPorts(ports):
	for port in ports:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
		sock.settimeout(0.1);

		res = sock.connect_ex((ipAddress, port));

		if res == 0:
			print(f"Port {port if port not in commonPorts else f'{str(port)} ({commonPorts[port]})'} is open.");

ipAddress = input("IP address to scan: ");

while True:
	mode = int(input("Scan mode - 1 (Common ports) or 2 (Custom): "));

	match mode:
		case 1:
			searchPorts(commonPorts.keys());
			break;
		case 2:
			customPorts = input("Enter ports separated by , : ").split(",");
			customPorts = map(int, customPorts);
			searchPorts(customPorts);
			break;
		case _:
			print("Invalid selection. Try again.");
			continue;
