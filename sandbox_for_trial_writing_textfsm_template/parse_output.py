#run use:  $ python parse_output.py template1.textfsm unparsed1.txt
import sys
import textfsm
from tabulate import tabulate

template = sys.argv[1]
output_file = sys.argv[2]

with open(template) as f, open(output_file) as output:
    re_table = textfsm.TextFSM(f)
    header = re_table.header
    result = re_table.ParseText(output.read())
    print(100*"=")
    print(result)
    print(100*"=")
    print(tabulate(result, headers=header))