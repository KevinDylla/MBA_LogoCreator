#!/usr/bin/python2

from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGB', (4500, 5400), color = None)

fnt = ImageFont.truetype('/usr/share/fonts/adobe-source-code-pro/SourceCodePro-MediumIt.otf', 100)
d = ImageDraw.Draw(img)
d.text((2000,2000), "Hello world", font=fnt, fill=(255, 255, 0))

img.save('test.png')
