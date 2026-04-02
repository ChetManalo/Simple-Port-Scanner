# Simple Port Scanner
This is a simple port scanner I made after relearning the basics of Python and starting my Cybersecurity journey. I'm looking forward to expanding its functionalities as I learn more.

## Changelog

### 4/2/26

- Renamed popular ports to common ports (Sounds better to me)
- Expanded common ports and converted the list to a dictionary to add what ports are used for
- Got rid of the "All ports" scan because I realized that wasn't all the ports and scanning the actual number of total ports would take forever.
- If a port is open and its a common port, it'll show the port usage next to the port number

I'll maybe eventually add an all ports scan again if I can find a fast way to scan them all. The next update will probably include a validation check for entering an IP address. At some point as well I'd like to see about turning this into a CLI tool. It'll be easier and faster to use that way.

### 4/1/26 (The beginning)
The app allows you to scan commonly used ports, custom ports, and all ports. You're also able to enable a verbose mode that as of now just tells you that a port is closed.

## Have a suggestion?
Please let me know! Create an issue or reach out via email (manalochet01@gmail.com). Thanks!
