# This is for testing purposed
# 1. put unparsed data on unparsed variable
# 2. ctrl+p and search for vendorname_osname_show_test
# 3. edit the textfsm
# 4. run the test here

import os
import json
from parse import parse_output

directory = os.path.dirname(__file__)
fileLoc = os.path.join(directory, "templates")
os.environ["NTC_TEMPLATES_DIR"] = fileLoc

unparsed="""
<PE-D1-RDC-TRANSIT>display ip interface brief
*down: administratively down
!down: FIB overload down
^down: standby
(l): loopback
(s): spoofing
(d): Dampening Suppressed
(E): E-Trunk down
The number of interface that is UP in Physical is 11
The number of interface that is DOWN in Physical is 12
The number of interface that is UP in Protocol is 6
The number of interface that is DOWN in Protocol is 17

Interface                         IP Address/Mask      Physical   Protocol VPN 
Eth-Trunk0                        192.168.0.1/30       down       down     --  
Eth-Trunk4                        172.31.104.69/31     up         up       --  
GigabitEthernet0/0/0              10.14.19.80/24       up         up       --  
GigabitEthernet3/0/0              unassigned           up         down     --  
GigabitEthernet3/0/0.100          unassigned           up         down     --  
GigabitEthernet3/0/1              unassigned           up         down     --  
GigabitEthernet3/0/2              unassigned           up         down     --  
GigabitEthernet3/0/2.100          unassigned           up         down     --  
GigabitEthernet3/0/4              unassigned           down       down     --  
GigabitEthernet3/0/4.850          unassigned           down       down     --  
GigabitEthernet3/0/5(10G)         unassigned           down       down     --  
GigabitEthernet3/0/5.3(10G)       192.168.2.1/30       down       down     l3vpn
GigabitEthernet3/0/5.300(10G)     unassigned           down       down     --  
GigabitEthernet3/0/5.3197(10G)    20.20.20.1/30        down       down     l3vpn
GigabitEthernet3/0/5.3199(10G)    21.21.21.1/30        down       down     l3vpn
GigabitEthernet3/0/5.3413(10G)    22.22.22.1/30        down       down     l3vpn
GigabitEthernet3/0/5.3414(10G)    20.20.30.1/29        down       down     l3vpn
GigabitEthernet3/0/5.3415(10G)    172.10.11.1/30       down       down     l3vpn
LoopBack0                         1.1.1.1/32           up         up(s)    --  
LoopBack2147483647                128.82.240.165/16    up         up(s)    l3vpn
NULL0                             unassigned           up         up(s)    --  
Vbdif100                          unassigned           down       down     --  
Virtual-Template0                 unassigned           up         up(s)    --  

"""
parsed = parse_output(platform="vrp", command="display ip interface brief", data=unparsed)
print(json.dumps(parsed, indent=4))
