from dotenv import load_dotenv
import os
from time import sleep
from sysap import SysAP

load_dotenv()

'''

Beispiel zur Nutzung des SysAP-Moduls:

Es wird ein virtueller Binärer Sensor erzeugt, Lebenszeit ist drei Minuten (180 Sekunden).
Im Anschluss weird der Sensor für eine Sekunde ein- und wieder ausgeschaltet.

'''

hostname = os.getenv("SYSAP")
username = os.getenv("USERNAME")
password = os.getenv("PASSWD")
sysap_uuid = "00000000-0000-0000-0000-000000000000"

sysap = SysAP(hostname, username, password, sysap_uuid)
result = sysap.register_virtual_device("EXAMPLE001", SysAP.DEVTYPE_BINARY_SENSOR, 180, "Virtueller Schalter 1")
print(result)
device_serial = next(iter(result[sysap_uuid]['devices']))
print(sysap.set_datapoint(device_serial, "ch0000", "odp0000","0"))
sleep(1)
print(sysap.set_datapoint(device_serial, "ch0000", "odp0000","1"))