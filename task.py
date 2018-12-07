#!/usr/bin/env python
import os, sys, getopt
import pandas as pd
import numpy as np

def mergy(filename, outname = 'Out.txt'):
	Filelist = 'Sum of '
	#Check File Valid
	res = np.zeros((51200,5))
	for i in range(len(filename)):
		path = str(os.getcwd())+"/bader_files/"+filename[i]
		try:
			x = open(path).readline()
			print("Success input "+str(filename[i]))
			a = np.loadtxt(path , skiprows = 16)
			res += a
			Filelist += filename[i] + ' '
		except FileNotFoundError:
			print("Error: Cannot find "+str(filename[i]))
	Filelist += '\n\n\n'
	np.savetxt(outname,res,fmt='%.11E',header=Filelist)
		#check first line
		# if i>0 :
		# 	crc = open(str(os.getcwd())+"/"+filename[i-1]).readline()
		# 	if crc==x :
		# 		pass
		# 	else:
		# 		print("Dimensial Error")
		# 		sys.exit()


def main(argv):
	inputfile = []
	outputfile_name = ''

	try:
		opts, args = getopt.getopt(argv, "ci:o:",["infile=","outfile="])

	except getopt.GetoptError:
		print ("Error parameter: task.py -i <inputfile_1> -i <inputfile_2> -o <outputfile_name>")
		sys.exit(2)

	for opt, arg in opts:
		if opt == '-c':
			print ('Copyright CaoZheng @ 2018')
			sys.exit()

		elif opt in ("-i","--infile"):
			inputfile.append(arg)

		elif opt in ("-o","--outfile"):
			outputfile_name = arg

	if inputfile == []:
		print ("No inputfile!")
	else:
		print ("Input file:" + str(inputfile))
		if outputfile_name != '':
			mergy(inputfile,outputfile_name)
		else:
			mergy(inputfile)


if __name__ == "__main__":
	main(sys.argv[1:])