import scapy.all as scapy

def scan(ip_range):
    arp_request = scapy.ARP(pdst=ip_range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    request = broadcast / arp_request
    answered = scapy.srp(request, timeout=2, verbose=False)[0]

    print("IP Address\t\tMAC Address")
    print("-" * 40)
    for sent, received in answered:
        print(f"{received.psrc}\t\t{received.hwsrc}")

if __name__ == "__main__":
    ip_range = input("Enter IP range (e.g., 192.168.1.1/24): ")
    scan(ip_range)
