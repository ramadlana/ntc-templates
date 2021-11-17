from ntc_templates.parse import parse_output

vlan_output="""
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Gi0/1
10   Management                       active    
60   VLan50                           active    Fa0/1, Fa0/2, Fa0/3, Fa0/4, Fa0/5
                                                Fa0/6, Fa0/7, Fa0/8

"""
vlan_parsed = parse_output(platform="cisco_ios", command="show vlan", data=vlan_output)
print(vlan_parsed)