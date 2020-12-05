with open('input.txt','r') as f:
    s = f.read().split('\n')
 
k = {"F":0,"B":1,"L":0,"R":1}
def decodeSeat(s):
    return sum((k[s[i]] << (len(s) - i-1)) for i in range(len(s)))

def day5(s):
    seats = list(map(decodeSeat,s))
    m,M = min(seats),max(seats)
    return M, set(range(m,M+1)).difference(seats)

print(day5(s))