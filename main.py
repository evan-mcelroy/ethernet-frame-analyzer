import socket, struct

# open socket to receive raw packets, not processed ones. capture all protocols. 3 = ETH_P_ALL
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

# bind socket to your NIC(network interface card)
s.bind(("wlo1", 0))

# read one packet
raw_data, addr = s.recvfrom(65536)

# split the header from the payload
header = raw_data[:14]
payload = raw_data[14:]

# unpack the mac header
dest_mac, src_mac, proto = struct.unpack('!6s6sH', header)

# ethertypes dictionary
ether_types = {
    0x0800: "IPv4",
    0x86DD: "IPv6",
    0x0806: "ARP",
    0x8035: "RARP",
    0x8100: "802.1Q VLAN"
}

# format mac addresses
def format_mac(addr_bytes):
    return ':'.join(f'{b:02x}' for b in addr_bytes)

# format ethertype
def format_ethertype(ethertype):
    proto_name = ether_types.get(ethertype, "Unknown")
    return f'0x{ethertype:04x} ({proto_name})'

# print datalink header
def datalink_header():
    print("Destination MAC:", format_mac(dest_mac))
    print("Source MAC:", format_mac(src_mac))
    print("EtherType:", format_ethertype(proto))
    return

# print payload
def payload_info():
    print("Payload size:", len(payload), "bytes")
    print("Payload Data:", ' '.join(f'{b:02x}' for b in payload[:1500]))
    return

def main():
    datalink_header()
    payload_info()
    return

if __name__ == "__main__":
    main()