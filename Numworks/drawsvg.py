from math import *
from kandinsky import *

def decode(n):
  s = n>>15
  m = n&0x7fff
  num = (-1)**s*(m/2048)
  return num

character = '@ចƅCᎅ̳౒Ԋ\u00f6ة@ွσA᎚ૡ@ࢤ࣡Aଊ෬@ᥜ߬Cᖚ਩್฽\u0171ဩ@࿗౒CᗃᏬᢸᬳ፜⌳A໡⇬@ውႏC๻᐀ࢤᜊ\u011fᤳ@ᕱᘩCᅈ᦮਀\u1ea4\u00cd\u2148@᱒ΚA\u3348ΚA\u3348ሩA⊸ሩ@ᷬએA⸽એ@ᷬΚAᷬ\u2148@᦮∔A⥱\u1f0a@㖮ᙻA⻶ᵱ@⠩ᘽA㚏╱@Ⴄ⡒Aს㐀C᝜㕱\u210a㖅⮅㐀@ࡦ⤟Bۍ⶚ǃ㑦@᣶♦A⌳⯬@⻍⣍B\u319a⹦㘩㑻'

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
        3*(t*(t*(p[3]-3*p[2]+3*p[1]-p[0])+2*(p[2]-2*p[1]+p[0]))+p[1]-p[0]))
    else:
      raise Exception(p)

def draw(xoff,yoff,scale,xB,yB,xdB,ydB,width):
  r = 0.7/scale
  t = 0
  w = int(1*scale/5)
  # Path
  while t<=1:
    #print(t)
    d = r/(xdB(t)**2+ydB(t)**2)**0.5
    # Width
    for i in range(-w,w+1):
      x = xB(t)+ydB(t)*i*d
      y = yB(t)-xdB(t)*i*d
      x = x*scale + xoff
      y = y*scale + yoff
      set_pixel(int(x),int(y),(0,0,0))
    t += d

xoff,yoff,scale = 100,50,15

index = 0
while index < len(character):
  char = character[index]
  #print(char, index)
  type_ = ord(char)&3
  posnum = ord("\x02\x02\x04\x06"[type_])
  #print("MLQC"[type_],posnum)
  index += 1
  pos = character[index:index+posnum]
  #print(repr(pos), index, index+posnum)
  pos = [decode(ord(p)) for p in pos]
  #print(pos)
  if type_ == 0:
    x,y = pos
    index += 2
    continue
  xBez,yBez = Bezier([x]+pos[::2]),Bezier([y]+pos[1::2])
  px,py = x,y
  draw(xoff,yoff,scale,xBez.B,yBez.B,xBez.dB,yBez.dB, 1)
  x,y = pos[-2:]
  index += posnum

save_gif()