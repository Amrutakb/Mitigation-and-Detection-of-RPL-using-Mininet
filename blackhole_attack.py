#!/usr/bin/env python

import sys
from mininet.log import setLogLevel, info
from mn_wifi.net import Mininet_wifi
from time import sleep

def topology():
    net = Mininet_wifi(iot_module='mac802154_hwsim')
    info("*** Creating nodes\\n")
    sensor1 = net.addSensor('sensor1', ip6='fe80::1/64', panid='0xbeef')
    sensor2 = net.addSensor('sensor2', ip6='fe80::2/64', panid='0xbeef')

    info("*** Configuring nodes\\n")
    net.configureNodes()

    info("*** Adding links\\n")
    net.addLink(sensor1, sensor2)

    info("*** Starting network\\n")
    net.build()

# Perform Blackhole Attack
    perform_blackhole_attack(sensor1)
    info("*** Running CLI\\n")
    CLI(net)
    
    info("*** Stopping network\\n")
    net.stop()
def perform_blackhole_attack(sensor):
    info("*** Performing Blackhole Attack from {}\n".format([sensor.name](http://sensor.name/)))
    sensor.cmd('iptables -A INPUT -j DROP')  # Drop all incoming traffic
    sleep(10)

if __name__ == '__main__':  
    setLogLevel('info')
    topology()