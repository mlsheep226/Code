import numpy as nump
import string

#@author MItchell Sheep
#@version 1.0
#@since 3/29/2018
#-------------------------------------------------------
#This function returns to values for cae of match or mismatcih

def Diagonal(n1,n2,pt):
    if(n1 == n2):
        return pt['MATCH']
    else:
        return pt['MISMATCH']

#------------------------------------------------------------   
#This function gets the optional elements of the aligment matrix and returns the elements for the pointers matrix.
def Pointers(di,ho,ve):

    pointer = max(di,ho,ve) #based on python default maximum(return the first element).

    if(di == pointer):
        return 'D'
    elif(ho == pointer):
        return 'H'
    else:
         return 'V'   
#------------------------------------------------------------   
def findAlign(s1,s2,match,mis, gap):
    penalty = {'MATCH': match, 'MISMATCH': mis, 'GAP': gap} #A dictionary for all the penalty valuse.
    n = len(s1) + 1 #The dimension of the matrix columns.
    m = len(s2) + 1 #The dimension of the matrix rows.
    al = nump.zeros((m,n),dtype = int) #Initializes the alighment matrix with zeros.
    p = nump.zeros((m,n),dtype = str) #Initializes the alighment matrix with zeros.
    #Scans all the first rows element in the matrix and fill it with "gap penalty"
    for i in range(m):
        al[i][0] = penalty['GAP'] * i
        p[i][0] = 'V'
    #Scans all the first columns element in the matrix and fill it with "gap penalty"
    for j in range (n):
        al[0][j] = penalty['GAP'] * j
        p[0][j] = 'H'
    #Fill the matrix with the correct values.

    p[0][0] = 0 #Return the first element of the pointer matrix back to 0.
    for i in range(1,m):
        for j in range(1,n):
            di = al[i-1][j-1] + Diagonal(s1[j-1],s2[i-1],penalty) #The value for match/mismatch -  diagonal.
            ho = al[i][j-1] + penalty['GAP'] #The value for gap - horizontal.(from the left cell)
            ve = al[i-1][j] + penalty['GAP'] #The value for gap - vertical.(from the upper cell)
            al[i][j] = max(di,ho,ve) #Fill the matrix with the maximal value.(based on the python default maximum)
            p[i][j] = Pointers(di,ho,ve)
    print nump.matrix(al)
    print "\n---------------------------------------\n"
    print nump.matrix(p)
    print "\n---------------------------------------\n"
    num = len(p)
    x = num
    row = len(s2)
    col = len(s1)
    out1 = []
    out2 = []
    while  x >= 0:
        if row == 0 or col == 0:
			break
        elif p[row][col] == 'D':
            out1.append(s1[col-1])
	    out2.append(s2[row-1])
            x -= 1
            row -= 1
            col -= 1
	elif p[row][col] == 'H':
	    out1.append(s1[col-1])
	    out2.append("-")
            x -= 1
            col -= 1
	elif p[row][col] == 'V':
	    out1.append("-")
	    out2.append(s2[row-1])
            x -= 1
            row -= 1
        else:
            print "ERROR!!!"
            break
	score = 0	
    out1 = ''.join(out1[::-1])
    out2 = ''.join(out2[::-1])
    seg1 = out1
    seg2 = out2
    l = len(seg1) - 1
    while l >= 0:
        if seg1[l] == "-" or seg2[l] == "-":
            if seg1[l] != "-" or  seg2[l] != "-":
                if seg1[l] == "~" or seg2[l] == "~":
                    score += 0    
                else:
                    score += gap
            else:
                score += 0
        elif seg1[l] == "~" or seg2[l] == "~":
            score += 0
        else:
            if seg1[l] == seg2[l]:
                score += match
            else:
                score += mis
        l -= 1

    print "The outputs of the best alignment bewreen the sequences strings are:\n---------------------------------------\n"
    print "Score: {}".format(score)
    print out1
    print out2
#--------------------------------------------------------------
#main of the program
def main():
    print "Enter two sequences with A, T, C, G, or U wit hspaces being -."
    seq1 = raw_input("Enter Sequence 1: ")
    seq2 = raw_input("Enter Sequence 2: ")
    match = int(raw_input("Enter in the match count: "))
    mis = int(raw_input("Enter in the miss dec (negative): "))
    gap = int(raw_input("Enter in the gap dec(negative): "))

    findAlign(seq1, seq2, match, mis, gap)
main()
