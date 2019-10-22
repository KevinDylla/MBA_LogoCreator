

from PIL import Image, ImageDraw, ImageFont

groesse_in_dim = [(4500, 5400),(4500,4050)]
global groesse

def eingabe():
    global groesse
    ie = int(input("Welche Größe 4500x5400(1) - Alles andere oder 4500x4050(2) - Hoodies ~> "))
    if ie == 1:
        groesse = groesse_in_dim[0]
        print (groesse)
        return
    elif ie == 2:
        groesse = groesse_in_dim[1]
        print (type(groesse))
        print (len(groesse))
        return
    else:
        print("falsche eingabe: entweder 1 (4500x5400) oder 2 (4500x4050)")
        eingabe()

def BildErstellen(px):
    img = Image.new('RGBA', px, (0,0,0,0))
    fnt = ImageFont.truetype('/usr/share/fonts/adobe-source-code-pro/SourceCodePro-MediumIt.otf', 500)
    d = ImageDraw.Draw(img)
    d.text((100,100), "Test", font=fnt, fill=(255, 255, 0))
    img.save(f'test_{groesse}.png', 'PNG')

eingabe()
BildErstellen(groesse)






