#!/usr/bin/env python

import sys
from mininet.log import setLogLevel, info
from mn_wifi.sixLoWPAN.link import LoWPAN
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi
from random import choice
from time import sleep

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

    # Function to simulate Decreased Rank Attack
    perform_decreased_rank_attack(net)

    info("*** Running CLI\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop()

def perform_decreased_rank_attack(net):
    """Simulate a decreased rank attack."""
    # Pick a node (sensor3 here as an example)
    attacker = net.get('sensor3')

    info("*** Performing Decreased Rank Attack\n")
    # Simulate the attack by sending fake RPL messages with a decreased rank
    attacker.cmd('rpld -r fe80::3/64 -m 1')  # Decrease the rank artificially

    # Give some time for the attack to affect the network
    sleep(10)

if name == 'main':
    setLogLevel('info')
    topology()