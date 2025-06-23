# get_ipconfig.py
A simple Python script to display detailed IP configuration information (IPv4, IPv6, and MAC addresses) for all active network interfaces on your system. 

---

## Features
- Lists all active network interfaces
- Displays
    - IPv4 and IPv6 addresses
    - Subnet masks
    - MAC addresses
    - Broadcast address
- Uses `psutil` and `socket` for cross-platform compatibility

## Installation

```Bash
git clone https://github.com/ScarMaxwell/get_ipconfig.git
cd get_ipconfig
```
### Requirements

- Python 3.7 or higher
- `psutil` library 

Install directly with:
```bash
pip install psutil
```
or use the provided `requirements.txt`:
```bash
pip install -r requirements.txt
```
---

## Example Output
```yaml
en0:
    IPv4 address   : 192.168.1.25
         netmask   : 255.255.255.0
         broadcast : 192.168.1.255
    IPv6 address   : fe80::1c3b:eeff:fe6e:abcd
         netmask   : ffff:ffff:ffff:ffff::
    MAC address    : 58:ef:68:21:ab:cd
```

---

## Why I Made This

While studying for the CompTIA Network+ certification, I frequently used `ipconfig` and its Linux equivalents in labs. I built this tool to practice my Python skills and create something I would’ve found genuinely useful during those exercises.

---

## Future Plans

- Convert to Bash and Powershell for broader system compatibility
- Add output saving (e.g., JSON or text file)
- Add command-line arguments (e.g., --interface, --ipv4-only)
## License

MIT License. Feel free to reuse and adapt with credit.

