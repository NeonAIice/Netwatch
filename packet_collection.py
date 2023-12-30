from scapy.all import sniff, wrpcap
from datetime import datetime
from scapy.arch.windows import get_windows_if_list
import platform
import sys
import subprocess


def packet_callback(packet):
    # Process each captured packet here
    print(packet.summary())


def get_valid_interface():
    while True:
        net_interface = input("Which interface would you like to use: ")
        # Check for the validity of the interface
        available_interfaces = {iface["name"]: iface["description"] for iface in get_windows_if_list()}
        if net_interface in available_interfaces:
            return net_interface
        print("Invalid interface. Available interfaces: {}".format(", ".join(available_interfaces)))


def get_valid_packet_count():
    while True:
        packets = input("How many packets to capture: ")
        try:
            packets = int(packets)
            if packets > 0:
                return packets
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid entry. Please enter a valid number.")


# Prompt user for the network interface to capture packets
interface = get_valid_interface()

# Prompt user for the number of packets to capture
num_packets = get_valid_packet_count()

# Get the computer name
computer_name = platform.node()

# Get the current date and time for the filename
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

# Start capturing packets
captured_packets = sniff(iface=interface, prn=packet_callback, count=num_packets)

# Save captured packets to a pcap file
file_name = f'packets_{computer_name}_{interface}_{timestamp}.pcap'
wrpcap(file_name, captured_packets)

# Call the cleaning script with the captured_packets variable and the file name
subprocess.run([sys.executable, 'packet_cleaning.py', file_name])
