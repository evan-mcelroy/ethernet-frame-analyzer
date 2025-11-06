# Ethernet Frame Analyzer

## Overview
This project is a **basic Ethernet frame analyzer** written in Python.  
It uses a **raw socket** to capture **one Ethernet frame** directly from the network interface card (NIC), then **parses** and **displays** the frame’s header and payload.

This project demonstrates how low-level frame capture works at the **Data Link Layer (Layer 2)** in the OSI model.

---

## Features
- Captures a **single raw Ethernet frame** using a raw socket  
- Parses and prints:
  - Destination MAC address  
  - Source MAC address  
  - EtherType (e.g., IPv4, ARP, IPv6)  
  - Paload size (in bytes)
  - Payload data (in hexadecimal)  

---

## Requirements
- **Operating System:** Linux (raw sockets require it)
- **Python:** 3.8 or higher
- **Privileges:** Must run as `root` (administrator)

---

## Installation & Setup

1. Clone or download this repository:
   ```bash
   git clone https://github.com/evan-mcelroy/ethernet-frame-analyzer.git
   cd ethernet-frame-analyzer
   ```

2. Check your network interface name:
   ```bash
   ip a
   ```
   Examples:
   - Wired: `eth0`, `enp3s0`
   - Wireless: `wlo1`

3. Open `main.py` and replace `"wlo1"` with your actual interface name.

4. Run the program with elevated privileges:
   ```bash
   sudo python3 main.py
   ```

---

## Example Output
```
Destination MAC: ff:ff:ff:ff:ff:ff
Source MAC: a4:34:d9:12:ef:99
EtherType: 0x0800 (IPv4)
Payload size: 1420 bytes
Payload Data: 45 00 05 dc 1a 2b ...
```
---

## Project Tutorial
[Raw Ethernet Frame Analyzer Tutorial](https://evan.great-site.net/2025/11/06/using-python-to-code-a-raw-ethernet-frame-analyzer/)
