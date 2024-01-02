# Netwatch - Intrusion Detection System
Packet Collection & Cleaning

Version: 0.15

## Overview

This project is a network packet analysis tool developed in Python, designed to capture and analyze network packets, clean the data, and generate machine-readable datasets for further analysis. Future versions will include more robust data filtering and optimization. The product of this project will be used to train a supervised classifier machine model to monitor network traffic and alert SecOps of malicious activity.   

## Features

- Packet capture using Scapy library
- Data preprocessing to extract relevant features
- Integration with packet cleaning script
- Machine-readable output for training and testing datasets

## Requirements
- Scapy
- Npcap
  - https://npcap.com/#download

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/fusionpunk/Netwatch.git
```

2. Navigate to the project directory:

```bash
cd network-packet-analysis
```

3. Install required dependencies:

```bash
pip install -r requirements.txt
```

4. Run the packet capture script:

```bash
python packets_capture.py
```

5. Follow the on-screen instructions to input interface and packet count to complete the packet capture and cleaning.

```bash
The packets_capture.py script will execute the script packets_cleaning.py.
```

## Project Structure

    packets_capture.py: Script for capturing network packets using Scapy.
    packets_cleaning.py: Script for cleaning and preprocessing captured packet data.
    
## Roadmap

Version 0.2 (Soon)

    Add independent execution for capture and cleaning.
    Improve the data cleaning process with additional filters and optimizations.

Version 0.5 (Upcoming)

    Support exporting cleaned datasets in multiple formats besides CSV (Like JSON, etc.).
    
Version 1.0 (Future)
    
    Integrate visualization tools to display packet statistics and trends.
    Implement real-time packet analysis for live network monitoring.

## Change Log

  Version 0.15
  
    Added requirements.txt

## License

    This project is licensed under the MIT License - see the LICENSE file for details.
