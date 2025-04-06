N = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141

def rrr(i):
    tmpstr = hex(i)
    hexstr = tmpstr.replace('0x','').replace('L','').replace(' ','').zfill(64)
    return hexstr

def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    return x % m

def load(file):
    signatures=[]
    import csv
    with open(file,'r') as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=",")
        line = 0
        for row in csv_reader:
            r=int(row[1],16)
            s=int(row[2],16)
            z=int(row[3],16)
            t=tuple([r,s,z])
            signatures.append(t)
            line+=1
    return signatures
signatures = load("SignRSZ.txt")
nn = len(signatures)
for a in range(0,nn):
    mm = signatures[a][2]
    rr = signatures[a][0]
    ss = signatures[a][1]
#   zs = ((mm * modinv(ss,N)) % N)
#   rs = ((rr * modinv(ss,N)) % N)
    jx = 0x23D4A09295BE678B21A5F1DCEAE1F634A69C1B41775F680EBF8165266471401B
    jk = ((mm + rr * jx) * modinv(ss,N)) % N
#   print("Z/S=",hex(zs))
#   print("R/S=",hex(rs))
#   print("[0x"+rrr(jk)+"]1111"+","+rrr(r)+","+rrr(s)+","+rrr(z)+"")
#   print(">>"+rrr(jk)+","+rrr(jx)+"")
#   print(">>"+rrr(jk)+"")
    print("Secret Key  NONCE:  "+rrr(jk)+"")
    print("Signatere R value:  "+rrr(rr)+"")
    
