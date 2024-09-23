# Detection and Mitigation of RPL Attacks Using Machine Learning
## Table of Contents 🧾
- [Introduction 📌](#introduction)
- [Motivation](#motivation)
- [Objectives](#objectives)
- [Installation](#installation)
- [Literature Survey](#literature-survey)
- [Implemented System](#implemented-system)
- [System Design](#system-design)
- [Implementation](#implementation)
- [Testing](#testing)
- [Results & Discussion](#results-discussion)
- [Conclusion](#conclusion)
- [References](#references)
- [Appendix](#appendix)

## Introduction 📌

RPL (Routing Protocol for Low-Power and Lossy Networks) is designed for IoT and low-power wireless networks. However, it is vulnerable to several attacks, including decreased rank and DoS attacks, which exploit its routing mechanisms. This project implements a detection and mitigation system using machine learning to secure RPL networks from these routing attacks. The system captures network traffic, detects malicious behavior, and mitigates threats to ensure a secure IoT environment.

## Motivation

With the rise of IoT, low-power networks like RPL have become critical. These networks are particularly vulnerable to security threats due to resource constraints. Attacks like decreased rank and DoS can degrade network performance, leading to data loss and compromised functionality. This project aims to provide a real-time detection and mitigation solution for these attacks using machine learning.

## Objectives
- Implement a Mininet-WiFi 6LoWPAN-based simulation of RPL networks.
- Generate RPL attacks (e.g., decreased rank, DoS).
- Capture traffic using Wireshark.
- Use Random Forest for detecting attacks based on the captured network traffic.

## Installation

1. Install [Mininet-WiFi](https://github.com/intrig-unicamp/mininet-wifi).
   ```bash
   git clone https://github.com/intrig-unicamp/mininet-wifi.git
   sudo ./install.sh -Wlnfv
   ```
2. Install RPLD:
   ```bash
   sudo apt-get install rpld
   ```
3. Ensure `rpld` runs in the background while capturing traffic:
   ```bash
   sudo rpld &
   ```
4. Download and configure `mac802154_hwsim` for the 6LoWPAN environment.
5. Run Mininet-WiFi with the 6LoWPAN.py file:
   ```bash
   sudo python 6LoWPAN.py
   ```
6. Capture traffic using Wireshark and store the files for later analysis.

## Literature Survey

1. **RPL Attack Detection and Mitigation in IoT**: Various approaches to detect and mitigate routing attacks using machine learning are explored, including methods for feature selection and optimization for constrained networks.
2. **Machine Learning Techniques for IoT Security**: Recent studies emphasize the use of Random Forest and other classifiers for effective intrusion detection in RPL-based networks.

## Implemented System

The system uses Mininet-WiFi for simulating 6LoWPAN networks with RPL. It generates attacks such as decreased rank and DoS attacks, capturing traffic in Wireshark for analysis. The captured data is processed, and Random Forest is planned to be used for detecting abnormal network behavior.

## System Design

The system operates in the following phases:

1. **Traffic Capture**: 
   - Mininet-WiFi simulates the RPL network with attack scenarios.
   - Wireshark captures the network traffic for later analysis.

2. **Detection and Mitigation**:
   - A machine learning model, specifically Random Forest, is used to classify network traffic as normal or under attack.
   - Upon detecting an attack, the compromised nodes are isolated from the network.

## Implementation

To run the project:
1. Ensure Mininet-WiFi and RPLD are installed and running.
2. Execute the `6LoWPAN.py` file to simulate the network.
   ```bash
   sudo python 6LoWPAN.py
   ```
3. Start capturing traffic with Wireshark.
4. After capturing sufficient data, proceed with analysis using a Random Forest model for attack detection.

## References

- [Mininet-WiFi](https://github.com/intrig-unicamp/mininet-wifi)
- [RPLD](https://github.com/cetic/rpld)

This version reflects your implementation setup with Mininet-WiFi, 6LoWPAN, RPLD, and Wireshark【5†source】. Let me know if you need further adjustments!
