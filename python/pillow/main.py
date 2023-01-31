from PIL import Image, ImageFilter, ImageDraw, ImageFont,  ImageColor 

im = Image.open("lenna.png")  

im.show()  
print(im.filename)  
print(im.format)
print(im.mode)
print(im.size)
print(im.width)
print(im.height)
print(im.info)

# Show rotated Image  
imim = im.rotate(45)  
imim.show()  

# create a thumbnail 
imim.thumbnail((150,150), resample=3) 
imim.show() 

# recompose une image en modifiant l'ordre des rgb
r, g, b = im.split()  
image = Image.merge("RGB", (b, g, r))  
image.show()  

# Show rotated Image 
rotated_image2 = im.transpose(Image.ROTATE_90)
rotated_image2.show() 

rotated_image2.save('lenna_rotate.png')  

# floutera la photo
blur_Image = im.filter(ImageFilter.BLUR)  
blur_Image.show()  

# floutera la photo selon la valeur passé en param de boxblur, de 1 à 9
blur_Image = im.filter(ImageFilter.BoxBlur(1))  
blur_Image.show()  

# ajouter watermark à photo
text = "c'est moi"  
draw = ImageDraw.Draw(im) 
font = ImageFont.truetype('arial.ttf', 36)  
textwidth, textheight = draw.textsize(text, font)

# calculate the x,y coordinates of the text
width, height = im.size    
margin = 10  
x = width - textwidth - margin  
y = height - textheight - margin 

draw.text((x, y), text, fontfont=font)  
im.show()  

# affiche le code de la couleur passé en param encodé sur 3 octet ex : (255, 255, 0)
blue = ImageColor.getrgb("blue")  
print(blue)  

# créera une image de taille 256 pixels par 256 pixels avec une unique couleur de code "#add8e6"
img = Image.new("RGB", (256, 256), ImageColor.getrgb("#add8e6"))  
img.show() 


# intègre du texte à une image 
img = im.convert('RGBA')  
text = Image.new('RGBA', im.size, (255,255,255,0))  
d = ImageDraw.Draw(text) 

# en param le positionnement du texte dans la photo, le texte à intégrer, les 3 premier param de
# fill sont les 3 octets pour la couleur et le dernier la transparence de 0 à 255
d.text((14,14), "Tutorials", fill=(255,4,255,128)) 
d.text((14,60), "Point", fill=(255,255,255,255)) 

out = Image.alpha_composite(img, text)    
out.show()  

# inverse le sens d'une photo horizontalement
im_flip = im.transpose(Image.FLIP_LEFT_RIGHT)

# inverse le sens d'une photo de bas en haut
im_flip = im.transpose(Image.FLIP_TOP_BOTTOM) 
im_flip.show()

# convertit l'image en noir et blanc
image = im.convert('L')
image.show()
