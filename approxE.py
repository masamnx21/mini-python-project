#e = lim <N->inf> (1 + 1/N)^N
if __name__=='__main__':

	#importing packages
	import math
	
	#tolerance
	import sys
	
	TOL = float(sys.argv[1])

	outfile = open('eOut.txt', 'w')
    
    
	#list of N values to try
	N = 2
	err = 1.00
	#approximating e and calculating abs. and relative error
	while err > TOL:
		approx_e = (1 + 1/N)**N
		err = abs(math.e - approx_e)/math.e
		N = N**2
		outfile.write('approx e: '+str(approx_e))
		outfile.write(' absolute error: '+str(abs(math.e - approx_e)))
		outfile.write(' relative error: '+str((abs(math.e - approx_e))/math.e)+'\n')
#               print(err)
#		err = abs(math.e - approx_e)/math.e
		#N = N**2
