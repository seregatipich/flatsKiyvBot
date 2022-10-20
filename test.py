import requests

img_url = 'https://cdn.riastatic.com/photosnew/dom/photo/prodaja-kvartira-kiev-chapaevka-klavdii-radchenko-ulitsa__192769694xg.webp'
im = open(requests.get(img_url))
p = requests.get(img_url)
out = open(f"{beautiful_photo_url}__{i}raw.webp", "wb")
out.write(p.content)
out.close()
im.show()
