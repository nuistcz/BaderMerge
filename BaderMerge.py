#!/usr/bin/env python
import os, sys, getopt
import numpy as np
def replacefooter(content, flag):
	finalcontent = content.split()
	print(finalcontent)

def addlines(linelist, lineindex, needlineindex):
	output = ''
	count = 1
	for i in needlineindex:
		startline = lineindex[int(i)-1]
		endline = lineindex[int(i)]-1
		flag = startline

		templine = linelist[flag].split()
		templinecontent = templine[0] + ' '+ templine[1] + '   ' + str(count) + '  ' +templine[3] + '\n'
		count += 1
		output += templinecontent

		for j in range(endline-startline):
			output += linelist[flag+1]
			flag += 1
	return output

def mergy(filename, outname = 'CHGCAR_OUTPUT'):
	headercontent = ''
	footercontent = ''
	p = len(filename)
	CHGCAR_path = str(os.getcwd())+ '/bader_files/CHGCAR'
	#Add the first 6 lines in head
	for i in range(5):
		headercontent += open(CHGCAR_path).readlines()[i]
	line_7 = open(CHGCAR_path).readlines()[6]
	rows = 0
	for s in line_7.split():
		rows += int(s)
	factor = int(rows/p)
	#Add line #7
	headercontent += '     ' + str(int(int(line_7.split()[0])/factor)) + '     '+ str(int(int(line_7.split()[1])/factor)) + '\n'
	# open(CHGCAR_path).readlines()[0:5]
	for i in range(p):
		nextrow = int(filename[i]) + 7
		headercontent += open(CHGCAR_path).readlines()[nextrow]
	# Add final line
	headercontent += open(CHGCAR_path).readlines()[8+rows]
	finalrow = open(CHGCAR_path).readlines()[9+rows].splitlines()
	headercontent += finalrow[0]
	# Caculate the main martix
	flag = 0


	for i in range(len(filename)):
		path = str(os.getcwd())+"/bader_files/BvAt"+filename[i]+".dat"
		try:
			x = open(path).readline()
			print("Processing Atom#"+str(filename[i]))
			a = np.loadtxt(path , skiprows = rows + 10)
			if flag == 0:
				res = a
				flag = 1
			else:
				res += a
		except FileNotFoundError:
			print("Error: Cannot find "+str(filename[i]))

	# Add footer
	print (res.shape[0])
	footerlist = open(CHGCAR_path).readlines()[res.shape[0]+10+rows : len(open(CHGCAR_path).readlines())]
	footerindex = []
	for i, val in enumerate(footerlist):
		if val.find('augmentation') == 0:
				footerindex.append(i)
	footerindex.append(len(footerlist))

	footercontent = addlines(footerlist,footerindex,filename)
	# print (footercontent)

	np.savetxt(outname,res,fmt='%.11E',header=headercontent, footer=footercontent, comments='')
	print ("Finish Successfully")


def main(argv):
	Atom_selection = []
	outputfile_name = ''

	try:
		opts, args = getopt.getopt(argv, "ci:o:",["inputfile=","outputfile="])

	except getopt.GetoptError:
		print ("Error parameter: BaderMerge.py -i <AtomSelection_1> -i <AtomSelection_2> -o <Outputfile_name>")
		sys.exit(2)

	for opt, arg in opts:
		if opt == '-c':
			print ('Copyright CaoZheng @ 2018')
			sys.exit()

		elif opt in ("-i","--inputfile"): #Atom-selection number
			# Atom_selection.append(arg)
			pass

		elif opt in ("-o","--outputfile"):
			outputfile_name = arg

	Atom_selection_file_path = str(os.getcwd())+ '/bader_files/atom_selection.txt'
	Atom_selection_file = open(Atom_selection_file_path, 'r') 
	sourcelines = Atom_selection_file.readlines()
	for lines in sourcelines:
		Atom_selection.append(lines.strip('\n'))

	if Atom_selection == []:
		print ("Please add -i atom-selection!")
	else:
		print ("Atom selection:" + str(Atom_selection))
		if outputfile_name != '':
			mergy(Atom_selection,outputfile_name)
		else:
			mergy(Atom_selection)


if __name__ == "__main__":
	main(sys.argv[1:])