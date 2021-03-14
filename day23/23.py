cups = [int(x) for x in list('523764819')]
# cups = [int(x) for x in list('389125467')]

def pickupCups(index,cups):
    if index + 4 < len(cups):
        return cups[index+1:index+4]
    else:
        return cups[index+1:] + cups[:(index+4)%len(cups)]

def simultateGame(turns,cups):
    cups[cups.index(max(cups))] = 0
    currIndex = 0
    currCup = cups[currIndex]
    
    for i in range(turns):
        pickup = pickupCups(currIndex,cups)
        dst = (currCup - 1) % len(cups)
        while dst in pickup:
            dst = (dst - 1) % len(cups)
        
        newCups = []
        for c in cups:
            if c not in pickup:
                if c == dst:
                    newCups += [c] + pickup
                else:
                    newCups += [c]
        cups = newCups
        print("CurrCup: {} Pickup: {} Dst: {}".format(currCup,pickup,dst))
        print(cups)
        currIndex = (cups.index(currCup) + 1) % len(cups)
        currCup = cups[currIndex]
    cups[cups.index(0)] = len(cups)
    return cups
def score(cups):
    oneIndex = cups.index(1)
    return "".join([str(x) for x in cups[oneIndex+1:]]) + "".join([str(x) for x in cups[:oneIndex]])

cups = simultateGame(100,cups)

print(cups)
print(score(cups))
