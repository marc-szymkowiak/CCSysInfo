# Simple Demonstrator for applying at copycat
# written by Marc Szymkowiak June 2022

import configcatclient
import platform
import re, uuid
import socket

if __name__ == '__main__':
    configcat_client = configcatclient.create_client(
        'RU7aCCrLxUOIfDRfqO42Vg/dlNsa9FVL0qSUmdufdJiDQ')
    system = platform.uname()
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)

    print("Just a quick demonstrator to show the features ob Copycats' feature flag system")
    print("You can enable/disable network informations via the feature flag used:")
    print(f"Systemtype and CPU used in your system: {system.system} on {system.processor}")
    print(f"Architecture of your current system: {system.machine}")
if configcat_client.get_value('isNetworkInfoEnabled', False):
    print("Your machines hostname: " + hostname)
    print("IP address: " + ip)
    print("MAC address of the used netword adapter: ", end="")
    print(':'.join(re.findall('..', '%012x' % uuid.getnode())))

    configcat_client.stop()
