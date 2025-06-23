# A Python script to retrieve and display IP configuration information for each active network interface.
# Uses psutil and socket to show IPv4, IPv6, MAC, netmask, and broadcast addresses where available.

import socket
import psutil

# Maps socket.AF_* values with human readable names
af_map = {
    socket.AF_INET: 'IPv4',
    socket.AF_INET6: 'IPv6',
    psutil.AF_LINK: 'MAC',
}

def main():
    
    # Grabs key and value from a dictionary, value is a list
    for nic, addrs in psutil.net_if_addrs().items():

        # nic = key within dictionary which is the network interface card name
        print(f"{nic}:")

        # Iterates over each value which is the ip configuration info of the NIC
        for addr in addrs:

            # Formats and turns the socket.AF_INET into human readable strings - IPv4, IPv6, MAC
            fam = "   {:<4}".format(af_map.get(addr.family, addr.family))
            print(fam, end="")
            print(f" address   : {addr.address}")

            # Formats and displays the different IP configuration details 
            if addr.broadcast:
                print(f"        broadcast : {addr.broadcast}")
            if addr.netmask:
                print(f"        netmask   : {addr.netmask}")
        print()

if __name__ == '__main__':
    main()