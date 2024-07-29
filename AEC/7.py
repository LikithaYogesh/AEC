from scapy.all import sniff, IP, TCP

def sniff_packets(interface, filter=None):
    def process_packet(packet):
        if packet.haslayer(IP):
            ip_src = packet[IP].src
            ip_dst = packet[IP].dst
            ip_protocol = packet[IP].proto
            print(f"IP Packet: {ip_src} -> {ip_dst}, Protocol: {ip_protocol}")
        if packet.haslayer(TCP):
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            print(f"TCP Packet: {src_port} -> {dst_port}")
    sniff(iface=interface, store=False, prn=process_packet, filter=filter)


if __name__ == "__main__":
    interface = input("Enter the interface (e.g., eth0, wlan0): ")
    filter = input("Enter the filter (optional, press enter to continue): ")
    print("Starting packet sniffing...")
    sniff_packets(interface, filter)

