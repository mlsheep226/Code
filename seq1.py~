import random
import string

def generate_string(N, alphabet='ACGT'):
        return ''.join([random.choice(alphabet) for i in xrange(N)])
def count(dna):
    t = 0
    a =0
    c = 0
    g = 0
    for x in dna:
        if x=='T':
            t = t + 1
        elif x=='A':
            a = a + 1
        elif x=='C':
            c = c + 1
        else:
            g = g + 1
    print "C count is: %d" % c
    print "G count is: %d" % g
    print "T count is: %d" % t
    print "A count is: %d" % a
dList = []
def findPattern(pat, dna, patLen):
    there = False
    count = 0
    for x in dna:
        if pat[0] == x:
            max = count + patLen
            there = comp(pat, dna, count, max)
        if there == True:
            dList.append(count)
        there = False
        count = count + 1
def comp(pat, dna, count, max):
    i = count
    c = 0
    stop = len(dna)-1
    if max > stop:
        return False
    while i < max:
        if pat[c] != dna[i]:
            return False
        i+=1
        c+=1
    return True
def main():
    num = int(raw_input("Enter in the length of sequence: "))
    dna = generate_string(num)
    print dna
    count(dna)
    pat = raw_input('Enter in pattern of A,T,C, or G to find in the DNA: ')
    out = findPattern(pat, dna, len(pat))
    print "Pattern %s exists at positions: %s" % (pat, dList)
main()
