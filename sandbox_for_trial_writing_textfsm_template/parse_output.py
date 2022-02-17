# run use:
# python3 parse_output.py template/show_ip_interface_brief.textfsm raw_data/show_ip_interface_brief.txt
import sys
import textfsm
from tabulate import tabulate

template = sys.argv[1]
output_file = sys.argv[2]

with open(template) as f, open(output_file) as output:
    re_table = textfsm.TextFSM(f)
    header = re_table.header
    result = re_table.ParseText(output.read())
    # print(100*"=")
    # print(result)
    print(100*"=")
    print(tabulate(result, headers=header))