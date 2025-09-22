from math import *
from kandinsky import *

class Bezier():
  def __init__(self,pos):
    self.pos = pos
    self.B, self.dB = self.getf()
  def getf(self):
    p = self.pos
    l = len(p)
    if l == 2: # Linear
      return (lambda t: \
        t*(p[1]-p[0])+p[0]
      , lambda t: \
        p[1]-p[0])
    elif l == 3: # Quadratic
      return (lambda t: \
        t*(t*(p[2]-2*p[1]+p[0])+2*(p[1]-p[0]))+p[0]
      , lambda t: \
        2*(t*(p[2]-2*p[1]+p[0])+p[1]-p[0]))
    elif l == 4: # Cubic
      return (lambda t: \
        t*(t*(t*(p[3]-3*p[2]+3*p[1]-p[0])+3*(p[2]-2*p[1]+p[0]))+3*(p[1]-p[0]))+p[0]
      , lambda t: \
        3*(t*(t*(p[3]-3*p[2]+2*p[1]-p[0])+2*(p[2]-2*p[1]+p[0]))+p[1]-p[0]))
    else:
      raise Exception(p)

def draw(xB,yB,xdB,ydB):
  x = xB
  y = yB
  set_pixel(int(x),int(y),(0,0,0))

pos = [
  (100,50),
  (250,100),
  (100,150),
  (200,50)
      ]

Δθ = 0.05
tθ = int(1/Δθ)
for pnum,(x,y) in enumerate(pos):
  c = int(255*pnum/len(pos))
  for θ in range(tθ):
    θ *= 2*pi*Δθ
    set_pixel(int(x+2*sin(θ)),int(y+2*cos(θ)),(0,c,255-0.5*c))

X, Y = zip(*pos)
xBez, yBez = Bezier(X), Bezier(Y)

px,py = X[0],Y[0]
r = 1
t = 0
while t<=1:
  #print(t)
  l = (xBez.dB(t)**2+yBez.dB(t)**2)**0.5
  x,y = xBez.B(t),yBez.B(t)
  c = 0+100*((x-px)**2+(x-px)**2)**0.5
  print(c)
  set_pixel(int(x),int(y),(c,c,c))
  px,py = x,y
  t += r/l

save_gif()