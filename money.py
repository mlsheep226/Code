def findChange(coins, money):
    mon = money
    mins = {}
    min = 100
    while coins:
        go = mon
        out ={}
        num = 0
        while go > 0:
            for x in reversed(coins):
                if x <= go:
                    go -= x
                    if x in out.keys():
                        out[x] += 1
                        num +=1
                        break
                    else:
                        out[x] = 1
                        num += 1
                        break
        if num < min:
            min = num
            mins[min] = out
        coins.pop()
    return mins


def main():
    coins = []
    money = int(raw_input("Enter in amount of change: "))
    print "Enter in a list of your contries coin amounts from smallest to largest"
    t = " "
    print "(Press [Enter] on blank when done)"
    while t != "":
        t = raw_input("Enter in coin: ")
        if t:
            coins.append(int(t))
    final = findChange(coins, money)
    now ={}
    min = 100
    for x in final.keys():
        if x < min:
            min = x
    now = final[min]
    for key in now.keys():
        print ("Used {:d} cent coin {:d} times.".format(key, now[key]))
main()
