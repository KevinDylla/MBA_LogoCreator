#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont
import sys

groesse_in_dim = [(4500, 5400),(4500,4050)]

# TODO :

# - UI(x- ish) 
# - Automation / Scaling ()
# - Vllt. MBA API ()
# - Sprüche hinzugefügt werden [json ?] ()
# - Textgröße angepasst werden 
# - Setup für PyInstaller
def eingabe():
    global groesse
    ie = int(input("Welche Größe 4500x5400(1) - Alles andere oder 4500x4050(2) - Hoodies ~> "))
    if ie == 1:
        groesse = groesse_in_dim[0]
        return
    elif ie == 2:
        groesse = groesse_in_dim[1]
        return
    else:
        print("falsche eingabe: entweder 1 (4500x5400) oder 2 (4500x4050)")
        eingabe()


#with open('sprueche/sprueche.txt') as sprueche:
#    for spruch in sprueche:
def BildErstellen(px):
   img = Image.new('RGBA', px, (0,0,0,0))
   fnt = ImageFont.truetype('/usr/share/fonts/adobe-source-code-pro/SourceCodePro-MediumIt.otf', 500)
   d = ImageDraw.Draw(img)
   d.text((100,100), sys.argv[1], font=fnt, fill=(255, 255, 0))
   img.save(f'test_{groesse}.png', 'PNG')

eingabe()
BildErstellen(groesse)

