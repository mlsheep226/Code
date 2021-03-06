

def findGCS(seq1, seq2):
    one = len(seq1)
    two = len(seq2)
    i = 0
    length = []
    while i <= one:
        length.append([])
        j = 0
        while j <= two:
            if i == 0 or j == 0:
                length[i].append(0)
            else:
                if seq1[i-1] == seq2[j-1]:
                    s = length[i-1][j-1] + 1
                    length[i].append(s)
                else:
                    if length [i-1][j] >= length[i][j-1]:
                        length[i].append(length[i-1][j])
                    else:
                        length[i].append(length[i][j-1])
            j += 1
        i += 1
    num = length[one][two]
    return make(length, num, one, two, seq1, seq2)
def make(length, num, one, two, seq1, seq2):
    x = num
    output = [None] * num
    row = one
    col = two
    while x > 0:
        if row == 0 or col == 0:
            print "ERROR!!!"
            break;
        elif seq1[row-1] == seq2[col-1]:
            output[x-1] = seq1[row-1]
            x -= 1
            row -= 1
            col -= 1
        else:
            if length[row][col] == length[row-1][col]:
                row -= 1
            else:
                col -= 1
    return output

def main():
    seq1 = list(raw_input("Enter in sequence 1: ").upper())
    seq2 = list(raw_input("Enter in sequence 2: ").upper())
    output = "".join(findGCS(seq1, seq2))
    print "Here is the output: "
    print output
main()
