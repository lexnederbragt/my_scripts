import sys

with open(sys.argv[1], "r") as fh:
    lines = fh.readlines()

for line in lines:
    # remove newlines
    line = line.strip()
    # header line starts with ">"
    if line.startswith(">"):
        header = line
    # all other lines are sequences
    else:
        length = len(line)
        # print results
        print(length, header)
