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
def kmer(s, pat):
    print "here"
    dList = {}
    occ = ""
    i = 0
    max = 0
    while i < len(s):
        l = i + pat
        up = True
        if l <= len(s):
            occ = s[i:l]
            for key in dList.keys():
                if key == occ:
                    up = False
                    dList[occ] += 1
                    if dList[occ] > max:
                        max = dList[occ]
            if up:
                dList.update({occ:1})
        i += 1 
    print '{:10}{:10}'.format("Pattern", "Occurence") 
    for x in dList:
        print '{:10}{:10}'.format(x, dList[x])
    if max > 1:
        print "\nThe most frequent Khmers are:"
        for x in dList.keys():
            if dList[x] >= max:
                print '{:10}{:10} Occurences'.format(x, dList[x])
def main():
    num = int(raw_input("Enter in the length of sequence: "))
    dna = generate_string(num)
    print dna
    count(dna)
    pat = int(raw_input('Enter in kmer length: '))
    kmer(dna, pat)
    best = (1, 0)
    print best[0]

main()
