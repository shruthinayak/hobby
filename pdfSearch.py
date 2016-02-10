import os
cmd="find \"path\" -name '*pdf' -exec sh -c 'pdftotext \"{}\" - | grep --with-filename --label=\"{}\" --color \"pattern\"' \\;";
pattern=""
path=""
path = raw_input("Path: ")
cmd = cmd.replace("path", path)
print "Press 'q' to quit!"
while(True):
	pattern = raw_input("Keyword: ")
	if pattern=='q':
		break
	cmd=cmd.replace("pattern", pattern)
	os.system(cmd)
	cmd=cmd.replace(pattern, "pattern")
