import random
import string

def generate_string(N, alphabet='ACGT'):
            return ''.join([random.choice(alphabet) for i in xrange(N)])
def main():
    num = int(raw_input("Enter in the length of sequence: "))
    times = int(raw_input("Enter number of strings: "))
    for i in range(times): 
        dna = generate_string(num)
        print "String {}: {} ".format(i, dna)
main()
