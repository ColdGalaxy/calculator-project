from math import *      

def b(n):
  b = bin(n)[2:]
  return "0"*max(0,16-len(b))+b

def decode(n):
  #print(b(n))
  s = n>>15
  m = n&0x7fff
  num = (-1)**s*(m/2048)
  #print(s, m, num)
  return num

def encode(n):
  s = int(n<0)<<15
  p = round(abs(n)*2048)
  num = s+p
  #print(b(num))
  return num

if __name__ == "__main__":
  decode(0xcafe)
  encode(-9.374)
