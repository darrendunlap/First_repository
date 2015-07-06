import sys

dir = sys.argv[1]

input=open(dir+"seqs.fastq", "r")
all_lines = input.readlines()
input.close()

output = open(dir+"seqs_fixed_header.fastq", "w")
for i, line in enumerate(all_lines):
	temp = line[1:].split()
	if len(temp)>1:
		samplenum = temp[0]
		origID = temp[1]+" "+ temp[2]
		new_header = "@"+origID+" "+samplenum+"\n"
		output.write(new_header)
	else:
		output.write(line)
output.close()
