
def findAlign(seq1, seq2, match, mis, gap):
    lister = {}
    m = len(seq1)
    n = len(seq2)
    comp1 = "";
    comp2 = seq2
    i = m
    j = n-1
    while j > 0:
        comp1 += "~"
        j -= 1
    comp1 = list(comp1 + seq1)
    comp2 = list(comp2)
    count = m + n - 1
    ps = 0
    pe = n
    s1 = comp1
    s2 = comp2
    while count > 0:
        score = 0
        seg1 = s1[ps:pe]
        seg2 = s2[ps:pe]
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

        lister[score] = [seg1, seg2]
        s1.pop(0)
        s1.append("~")

        count -= 1 
    max = score
    k = 0
    for key in lister: 
        print lister[key]
        if key >= max:
            max = key
    print "The highest score is between: "
    print lister[max]
    print "With score of {}".format(max)

def main():
    print "Enter two sequences with A, T, C, G, or U wit hspaces being -."
    seq1 = raw_input("Enter Sequence 1: ")
    seq2 = raw_input("Enter Sequence 2: ")
    match = int(raw_input("Enter in the match count: "))
    mis = int(raw_input("Enter in the miss dec (negative): "))
    gap = int(raw_input("Enter in the gap dec(negative): "))\
    
    findAlign(seq1, seq2, match, mis, gap)
main()
