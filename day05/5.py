print((lambda seats: (seats[-1], set(range(seats[0],seats[-1]+1)).difference(seats)))((lambda s,k: sorted(list(map(lambda l: sum((k[l[i]] << (len(l) - i-1)) for i in range(len(l))),s))))(open('input.txt','r').read().split('\n'), {"F":0,"B":1,"L":0,"R":1})))