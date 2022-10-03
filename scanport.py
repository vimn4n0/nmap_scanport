import nmap
import re 

ip_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
port_pattern = re.compile("([0-9]+)-([0-9]+)")
port_min = 0
port_max = 65535
open_port = []
meh = nmap.PortScanner()

while True:
    ip_add = input("\n Masukin ip_address : " )
    if ip_pattern.search(ip_add):
        print(f"{ip_add} valid")
        break

for i in range(port_min, port_max + 1):
    try:
        hasil = meh.scan(ip_add, str(i))
        status_port = (hasil['scan'][ip_add]['tcp'][i]['state'])
        print(f"Port{i} adalah {status_port}")
    except KeyboardInterrupt:
        print(f"tidak dapat port {i}.")
        exit()

