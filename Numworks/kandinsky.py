# A way to replace the kandinsky library that is reserved for Numworks calculators
from PIL import Image
import sys

img0 = Image.new("RGB",(320,222),(255,255,255))
img = img0.copy()
frames = []

def save_image(img):
    frames.append(img.copy())
def save_gif():
    img0.save("numworks_screen.gif",save_all=True,append_images=frames,duration=1)

save_image(img)


def get_pixel(x,y):
    img.getpixel((x,y))

def set_pixel(x,y,col):
    img.putpixel((x,y),color(*col))
    save_image(img)

def color(r,g,b):
    return (int(r),int(g),int(b))

def fill_rect(x,y,w,h,col):
    for _x in range(x,x+w):
        for _y in range(y,y+h):
            img.putpixel((_x,_y),color(*col))
    save_image(img)
