[![Build Status](https://travis-ci.org/networktocode/ntc-templates.svg?branch=master)](https://travis-ci.org/networktocode/ntc-templates)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

NTC TEMPLATES CUSTOM FORK
=============
This is fork from the original https://github.com/networktocode/ntc-templates
this fork is for my personal or private parser for unique purposed

```
Contact Person
hidayah.ramadalana@multipolar.com
MULTIPOLAR TECHNOLOGY TBK
```


Installation and Usage
----------------------
- open run-me.py
- put unparsed data on unparsed variable
- ctrl+p and search for vendorname_osname_show_test
- edit the textfsm (vendorname_osname_show_test.textfsm files)
- edit ntc_templates/templates/index files and update in CUSTOME TEMPLATE


##### SOP for creating new template
- create new templates with name vendorname_osname_show_your_command_here.textfsm
- update index files with: vendorname_osname_show_your_command_here.textfsm, .*, os_name, show your command here

##### Typing rules and index file naming
```
vendorname_osname_show_test.textfsm, .*, os_name, <command ex: show ver>
vendorname_osname_show_your_command_here.textfsm
```
-----

### Example 1
```
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
```
```
Value INTERFACE (\S+)
Value STATUS (up|down|admin down|deleted)
Value PROTOCOL (\S+)
Value DESCRIPTION (\S.*?)

Begin
  ^Interface\.*$$ -> Start

Start
  ^Interface.*$$
  ^${INTERFACE}\s+${STATUS}\s+${PROTOCOL}\s+$$ -> Record
  ^${INTERFACE}\s+${STATUS}\s+${PROTOCOL}$$ -> Record
  ^${INTERFACE}\s+${STATUS}\s+${PROTOCOL}\s+${DESCRIPTION}$$ -> Record
  ^\s*$$
  ^. -> Error
```


### Example 2
```
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
```
```
Value Filldown ROUTETABLES (\S+)
Value DESTINATION (\S+)
Value PROTO (\S+)
Value PRE (\S+)
Value COST (\S+)
Value FLAG (\S+)
Value NEXTHOP (\S+)
Value Required INTERFACE (\S+)

Start
  ^Routing Tables:\s+${ROUTETABLES} -> Record
  ^Destination/Mask.*NextHop\s+Interface$$ -> Interfaces

Interfaces
  ^\s*${DESTINATION}\s+${PROTO}\s+${PRE}\s+${COST}\s+${FLAG}\s+${NEXTHOP}\s+${INTERFACE}.*$$ -> Record
  ^\s*$$
  ^. -> Error
```
##### Output
```
[
    {
        "routetables": "Public",
        "destination": "1.1.1.1/32",
        "proto": "OSPF",
        "pre": "10",
        "cost": "65000",
        "flag": "D",
        "nexthop": "172.31.104.69",
        "interface": "Eth-Trunk4"
    },
    {
        "routetables": "Public",
        "destination": "1.1.1.5/32",
        "proto": "Direct",
        "pre": "0",
        "cost": "0",
        "flag": "D",
        "nexthop": "127.0.0.1",
        "interface": "LoopBack0"
    },
    {
        "routetables": "Public",
        "destination": "10.14.19.0/24",
        "proto": "Direct",
        "pre": "0",
        "cost": "0",
        "flag": "D",
        "nexthop": "10.14.19.23",
        "interface": "GigabitEthernet0/0/0"
    },
 ... OMITED....
]
```

### Example 3
```
XGSPON-D3-DDS_LAB#display service-port vlan 2250    
{ <cr>|e2e<K>|inner-vlan<K>|sort-by<K>||<K> }: 

  Command:
          display service-port vlan 2250
  Switch-Oriented Flow List
  -----------------------------------------------------------------------------
   INDEX VLAN VLAN     PORT F/ S/ P VPI  VCI   FLOW  FLOW       RX   TX   STATE
         ID   ATTR     TYPE                    TYPE  PARA
  -----------------------------------------------------------------------------
       4 2250 common   gpon 0/2 /0  3    3     vlan  200        240  158  up   
      16 2250 common   gpon 0/2 /2  4    3     vlan  200        40   22   down 
      19 2250 common   gpon 0/2 /2  5    3     vlan  200        40   22   down 
      22 2250 common   gpon 0/2 /2  6    3     vlan  200        40   22   down 
      25 2250 common   gpon 0/2 /2  7    3     vlan  200        40   22   down 
      28 2250 common   gpon 0/2 /2  8    3     vlan  200        40   22   down 
      37 2250 common   gpon 0/2 /3  0    3     vlan  200        40   22   down 
      40 2250 common   gpon 0/2 /3  2    3     vlan  200        40   22   down 
      44 2250 common   gpon 0/2 /3  1    3     vlan  200        40   22   down 
      47 2250 common   gpon 0/2 /3  3    3     vlan  200        40   22   down 
      50 2250 common   gpon 0/2 /0  5    0     vlan  2250       250  163  down 
      51 2250 common   gpon 0/2 /0  6    0     vlan  2250       250  163  down 
  -----------------------------------------------------------------------------
   Total : 12  (Up/Down :    1/11)
   Note : F--Frame, S--Slot, P--Port,
          VPI indicates ONT ID for PON, VCI indicates GEM index for GPON,
          v/e--vlan/encap, pritag--priority-tagged,
          ppp--pppoe, ip--ipoe, ip4--ipv4oe, ip6--ipv6oe, vxl--vxlan.
```

```
Value INDEX (\S+)
Value VLANID (\S+)
Value VLANATTR (\S+)
Value PORTTYPE (\S+)
Value FRAMESLOT (\S+)
Value PORT (\S+)
Value VPI (\S+)
Value VCI (\S+)
Value FLOWTYPE (\S+)
Value FLOWPARA (\S+)
Value RX (\S+)
Value TX (\S+)
Value STATE (\S+)

Start
  ^\s+ID\s+ATTR\s+TYPE\s+TYPE\s+PARA.*$$ -> Interface

Interface
  ^\s*------.*$$
  ^\s*${INDEX}\s+${VLANID}\s+${VLANATTR}\s+${PORTTYPE}\s+${FRAMESLOT}\s+${PORT}\s+${VPI}\s+${VCI}\s+${FLOWTYPE}\s+${FLOWPARA}\s+${RX}\s+${TX}\s+${STATE}\s*$$ -> Record
  ^.*$$ {{untuk ambl (Total : 12  (Up/Down :    1/11) dan seterusnya) }}
  ^\s*$$
  ^. -> Error

```

---

##### Values

The capture group names should be in UPPERCASE.

An example of the proper format is shown below.

```
Value TIME (\d+:\d+:\d+)
Value TIMEZONE (\S+)
Value DAYWEEK (\w+)
Value MONTH (\d+)
Value DAY (\d+)
Value YEAR (\d+)

Start
  ^${TIME}\s+${TIMEZONE}\s+${DAYWEEK}\s+${DAY}/${MONTH}/${YEAR} -> Record
  ^. -> Error
```
##### States

If the raw output has a heading, the `Start` state should match on the column headings and then transition to another state that will match the device's output table with the capture groups. This helps ensure the regex patterns for the capture groups are attempting to match the correct information, and allows templates to easily add additional States for tables that have different headings. 
Example:

*Raw Output*
```
... omitted
Network Next Hop Metric LocPrf Weight Path
*> 111.111.111.111/32 112.112.112.112 4294967295 4294967295 65535 1000 1000 1000 i
```

*Sample Template*
```
Start
# Checking for header
^\s*Network\s+Next(?:\s+|-)[Hh]op\s+Metric\s+LocPrf\s+Weight\s+Path\s*$$ -> BGPTable

BGPTable
 ... omitted
```

Each **state** should end with `^. -> Error`. This helps to ensure we're accounting for every line within the raw output for the command. This doesn't mean we have to capture all the data as a **Value**, but we do have to account for it. In addition, it is also good to provide an expression to match blank lines, `^\s*$$`

An example would be the following raw output:
```
NAME: "3640 chassis", DESCR: "3640 chassis"
PID: , VID: 0xFF, SN: FF1045C5
```

The template would be the following:
```
Value NAME (.*)
Value DESCRIPTION (.*)

Start
  ^NAME:\s+"${NAME}",\s*DESCR:\s+"${DESCRIPTION}"
  ^PID:\s*,\s*VID:\s*\S+,\s*SN:\s*\S+
  ^\s*$$
  ^. -> Error
```

Taking a look at the example template above, you notice that we're using **\s*** and **\s+**. These are the preferred way to match space characters, and should be used over the literal space character. For example, `This\s+is\s+preferred\s*$$` vs `This is not preferred$$`

- **\s*** accounts for zero or more spaces (use when the output may or may not have a space between characters)
- **\s+** accounts for one or more spaces (use when output will have a space, but could have more than one space)

