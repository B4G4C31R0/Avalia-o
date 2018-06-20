l1=[int(x) for x in input().split()]
a11,a12,a13,a14,b11,b12,b13,b14=l1

l2=[int(y) for y in input().split()]
a21,a22,a23,a24,b21,b22,b23,b24=l2

l3=[int(z) for z in input().split()]
a31,a32,a33,a34,b31,b32,b33,b34=l3

l4=[int(w) for w in input().split()]
a41,a42,a43,a44,b41,b42,b43,b44=l4

print ("""
  |{} {} {} {}|     |{} {} {} {}|
A=|{} {} {} {}|   B=|{} {} {} {}|
  |{} {} {} {}|     |{} {} {} {}|
  |{} {} {} {}|     |{} {} {} {}|""".format(a11,a12,a13,a14,b11,b12,b13,b14,a21,a22,a23,a24,b21,b22,b23,b24,a31,a32,a33,a34,b31,b32,b33,b34,a41,a42,a43,a44,b41,b42,b43,b44))

print ("""
     |{} {} {} {}|
SOMA=|{} {} {} {}|
     |{} {} {} {}|
     |{} {} {} {}|""".format(a11+b11,a12+b12,a13+b13,a14+b14,a21+b21,a22+b22,a23+b23,a24+b24,a31+b31,a32+b32,a33+b33,a34+b34,a41+b41,a42+b42,a43+b43,a44+b44))

