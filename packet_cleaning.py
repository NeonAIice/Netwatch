from scapy.all import rdpcap
import sys
import random
import csv


# Load the captured packets
file_name = sys.argv[1]
captured_packets = rdpcap(file_name)

# Display summary of the first few packets
for packet in captured_packets[:5]:
    print(packet.summary())

# Check for missing destination IP addresses
missing_dest_ip_packets = [packet for packet in captured_packets if 'IP' in packet and 'dst' not in packet['IP'].fields]

# Handle missing destination IP addresses (for demonstration, we'll simply remove them)
cleaned_packets = [packet for packet in captured_packets if packet not in missing_dest_ip_packets]

# Check if 'IP' layer is present before accessing its length
max_packet_size = max(packet['IP'].len for packet in cleaned_packets if 'IP' in packet)
# Normalize packet sizes
cleaned_packets_normalized = [
    {
        'timestamp': packet.time,
        'source_ip': packet['IP'].src if 'IP' in packet else None,
        'destination_ip': packet['IP'].dst if 'IP' in packet else None,
        'packet_size_normalized': packet['IP'].len / max_packet_size if 'IP' in packet else None,
    }
    for packet in cleaned_packets
]

# Encode protocol types, source IP, and destination IP
cleaned_packets_encoded = [
    {
        'timestamp': packet['timestamp'],
        'source_ip': packet['source_ip'],
        'destination_ip': packet['destination_ip'],
        'packet_size_normalized': packet['packet_size_normalized'],
        'protocol_type': 1 if 'TCP' in packet else 2,  # Example encoding
    }
    for packet in cleaned_packets_normalized
]

# Shuffle the dataset
random.shuffle(cleaned_packets_encoded)

# Split into training and testing sets
split_index = int(0.8 * len(cleaned_packets_encoded))
training_set = cleaned_packets_encoded[:split_index]
testing_set = cleaned_packets_encoded[split_index:]

# Write training_set to txt file
with open("training_set.csv", "w", newline='') as f:
    header = ['timestamp', 'source_ip', 'destination_ip', 'packet_size_normalized', 'protocol_type']
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()  # Header

    for entry in training_set:
        row_data = {field: entry.get(field, '') for field in header}
        writer.writerow(row_data)

# Write testing_set to txt file
with open("testing_set.csv", "w", newline='') as f:
    header = ['timestamp', 'source_ip', 'destination_ip', 'packet_size_normalized', 'protocol_type']
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()  # Header

    for entry in testing_set:
        row_data = {field: entry.get(field, '') for field in header}
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writerow(row_data)