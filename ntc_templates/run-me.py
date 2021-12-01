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
Route Flags: R - relay, D - download to fib
------------------------------------------------------------------------------
Routing Tables: Public
         Destinations : 15       Routes : 15       

Destination/Mask    Proto   Pre  Cost      Flags NextHop         Interface

        1.1.1.1/32  OSPF    10   65000       D   172.31.104.69   Eth-Trunk4
        1.1.1.5/32  Direct  0    0           D   127.0.0.1       LoopBack0
     10.14.19.0/24  Direct  0    0           D   10.14.19.23     GigabitEthernet0/0/0
    10.14.19.23/32  Direct  0    0           D   127.0.0.1       GigabitEthernet0/0/0
   10.14.19.255/32  Direct  0    0           D   127.0.0.1       GigabitEthernet0/0/0
      127.0.0.0/8   Direct  0    0           D   127.0.0.1       InLoopBack0
      127.0.0.1/32  Direct  0    0           D   127.0.0.1       InLoopBack0
127.255.255.255/32  Direct  0    0           D   127.0.0.1       InLoopBack0
  172.31.104.66/31  Direct  0    0           D   172.31.104.67   Eth-Trunk5
  172.31.104.67/32  Direct  0    0           D   127.0.0.1       Eth-Trunk5
  172.31.104.68/31  Direct  0    0           D   172.31.104.68   Eth-Trunk4
  172.31.104.68/32  Direct  0    0           D   127.0.0.1       Eth-Trunk4
  172.31.104.70/31  Direct  0    0           D   172.31.104.70   Eth-Trunk6
  172.31.104.70/32  Direct  0    0           D   127.0.0.1       Eth-Trunk6
255.255.255.255/32  Direct  0    0           D   127.0.0.1       InLoopBack0
"""
parsed = parse_output(platform="vrp", command="display ip routing-table", data=unparsed)
print(json.dumps(parsed, indent=4))
