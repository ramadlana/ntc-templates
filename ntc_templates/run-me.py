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
Interface                      Status         Protocol Description
Vl1                            admin down     down     
Vl99                           up             up       10.20.99.0_Switch_mgmt_VLAN
Gi0/1                          down           down     D3 USER
Gi0/2                          down           down     D3 USER
Gi0/3                          down           down     D3 USER
Gi0/4                          down           down     D3 USER
Gi0/5                          down           down     D3 USER
Gi0/6                          down           down     D3 USER
Gi0/7                          down           down     D3 USER
Gi0/8                          up             up       MERAKI TEST AP
Gi0/9                          admin down     down     
Gi0/10                         up             up       UPLINK TO TULCCD3S01P
Gi0/10.10                      deleted        down
Gi0/10.20                      up             up       Carrier VLAN
"""
parsed = parse_output(platform="os_name", command="show test", data=unparsed)
print(json.dumps(parsed, indent=4))