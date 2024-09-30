import sys
from mininet.log import setLogLevel, info
from mn_wifi.net import Mininet_wifi
from time import sleep

def topology():
    net = Mininet_wifi(iot_module='mac802154_hwsim')
    info("*** Creating nodes\\n")
    sensor1 = net.addSensor('sensor1', ip6='fe80::1/64', panid='0xbeef', dodag_root=True)
    sensor2 = net.addSensor('sensor2', ip6='fe80::2/64', panid='0xbeef')

    info("*** Configuring nodes\\n")
    net.configureNodes()

    info("*** Adding links\\n")
    net.addLink(sensor1, sensor2)

    info("*** Starting network\\n")
    net.build()

# Perform DODAG version number attack
    perform_dodag_version_attack(sensor2)

    info("*** Running CLI\\n")
    CLI(net)

    info("*** Stopping network\\n")
    net.stop()
def perform_dodag_version_attack(sensor):
    info("*** Performing DODAG Version Number Attack from {}\n".format([sensor.name](http://sensor.name/)))
    sensor.cmd('rpld -d fe80::2/64 -v 255')  
    sleep(10)

if __name__ == '__main__':
    setLogLevel('info')
    topology()