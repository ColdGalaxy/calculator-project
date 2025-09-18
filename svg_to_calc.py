from xml.etree import ElementTree
from fpcalc import encode, decode
import re

tree = ElementTree.parse('symbol1.svg')
root = tree.getroot()
for elem in root:
    if elem.tag == "{http://www.w3.org/2000/svg}g":
        groot = elem
        break
print(groot.attrib)

paths = ""
for elem in sorted(groot,key=lambda elem: int(elem.attrib["{http://www.inkscape.org/namespaces/inkscape}label"])):
    if elem.tag == "{http://www.w3.org/2000/svg}path":
        attrs = elem.attrib
        style,path,label = attrs["style"].split(";"), attrs["d"], attrs["{http://www.inkscape.org/namespaces/inkscape}label"]
        style = {attr.split(":")[0]:attr.split(":")[1] for attr in style}
        print(style["stroke-width"], repr(path), repr(label))
        paths += path + " "
    else:
        print(elem.tag, elem.attrib)

paths = re.sub(r" (M|H|V|L|C|Q)",r"|\1",paths.strip()) # Remove ending space, separated
print(repr(paths), paths.count("|")+paths.count(" ")+paths.count(",")+paths.count("H")+paths.count("V"))
paths = paths.split("|")

cond_path = ""

for path in paths:
    print(path[0],end=" ")
    ptype = 0x40 # Default width (= 1 in condensed notation)
    match path[0]:
        case "M":
            ptype += 0
        case "H":
            ptype += 1
        case "V":
            ptype += 1
        case "L":
            ptype += 1
        case "Q":
            ptype += 2
        case "C":
            ptype += 3
    cond_path += chr(ptype)

    p = [tuple(map(float,i.split(","))) for i in path[2:].split(" ")]
    print(p)
    if path[0] == "H":
        print(decode(ord(cond_path[-3])), decode(ord(cond_path[-2])))
        x = chr(encode(p[0][0]))
        cond_path += x+cond_path[-2]
    elif path[0] == "V":
        print(decode(ord(cond_path[-3])), decode(ord(cond_path[-2])))
        y = chr(encode(p[0][0]))
        cond_path += cond_path[-3]+y
    else:
        for x,y in p:
            x,y = chr(encode(x)), chr(encode(y))
            cond_path += x+y
        
    """else:
        p = list(map(float,p.split(",")))
        pathchrs = "".join(chr(encode(i)) for i in p)
        print(p,repr(pathchrs), end=" ")
        if len(pathchrs) != 2:
            print(len(pathchrs))
            raise Exception
        cond_path += pathchrs"""

print("\n",repr(cond_path), repr(cond_path.encode("utf-8")), len(cond_path))

