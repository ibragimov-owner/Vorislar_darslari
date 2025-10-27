# ASCII Art — rasmni terminalga ASCIIga aylantirish (Pillow kerak)

# Rasmni ASCII bilan ko‘rsatadi — fun.

# pip install pillow
from PIL import Image

def img_to_ascii(path, width=80):
    chars = "@%#*+=-:. "
    img = Image.open(path)
    wpercent = (width/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent))*0.5)
    img = img.resize((width, hsize)).convert("L")
    out = ""
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            out += chars[int(img.getpixel((x,y))/255*(len(chars)-1))]
        out += "\n"
    return out

print(img_to_ascii("phyton.jpg", width=80)) # shu code saqlangan joyda phyton rasm bo'lishi zarur