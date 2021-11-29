[![Build Status](https://travis-ci.org/networktocode/ntc-templates.svg?branch=master)](https://travis-ci.org/networktocode/ntc-templates)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

NTC TEMPLATES - ramadlana FORK
=============
This is fork from the original https://github.com/networktocode/ntc-templates
this fork is for my personal or private parser for unique purposed


Installation and Usage
----------------------
- open run-me.py
- put unparsed data on unparsed variable
- ctrl+p and search for vendorname_osname_show_test
- edit the textfsm (vendorname_osname_show_test.textfsm files)

Example textfsm files
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

Example Unparsed data
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

#### Index File

The Index file binds the templates to the commands being run. Special care has been taken on ordering, as there is potential for issues. e.g. `show ip route` picking up for `show ip router vrf <vrf-name>`. We have used a combination of ordering, as defined:

 - OS in alphabetical order
 - Template name in length order
 - When length is the same, use alphabetical order of command name
 - Keep space between OS's

Example:

```
Template, Hostname, Platform, Command

# same os, same length, used alphabetical order of command name
arista_eos_show_mlag.textfsm, .*, arista_eos, sh[[ow]] ml[[ag]]
arista_eos_show_vlan.textfsm, .*, arista_eos, sh[[ow]] vl[[an]]

# os in alphabetical order and space between cisco_asa and arista_eos
cisco_asa_dir.textfsm,  .*, cisco_asa, dir

# same os, template name length different and space between cisco_asa and cisco_ios
cisco_ios_show_capability_feature_routing.textfsm,  .*, cisco_ios, sh[[ow]] cap[[ability]] f[[eature]] r[[outing]]
cisco_ios_show_interface_transceiver.textfsm, .*, cisco_ios, sh[[ow]] int[[erface]] trans[[ceiver]]
cisco_ios_show_cdp_neighbors_detail.textfsm, .*, cisco_ios, sh[[ow]] c[[dp]] neig[[hbors]] det[[ail]]
```
