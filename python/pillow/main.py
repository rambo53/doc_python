from PIL import Image, ImageFilter, ImageDraw, ImageFont,  ImageColor, ImageEnhance, ImageOps 

im = Image.open("lenna.png")  

im.show()  
print(im.filename)  
print(im.format)
print(im.mode)
print(im.size)
print(im.width)
print(im.height)
print(im.info)

#########################################################################
    #################### FILTER ENHANCE ########################
#########################################################################

# pour intensifier les couleurs
im_enh = ImageEnhance.Color(im)
im_enh = im_enh.enhance(2)
im_enh.show()

# pour augmenter le contraste des couleurs
im_con = ImageEnhance.Contrast(im)
im_con = im_con.enhance(2)
im_con.show()

# pour augmenter la luminosité
im_br = ImageEnhance.Brightness(im)
im_br = im_br.enhance(2)
im_br.show()

# pour augmenter le détail d'une image
im_sh = ImageEnhance.Sharpness(im)
im_sh = im_sh.enhance(5)
im_sh.show()

# floutera la photo
blur_Image = im.filter(ImageFilter.BLUR)  
blur_Image.show()  

# floutera la photo selon la valeur passé en param de boxblur, de 1 à 9
blur_Image = im.filter(ImageFilter.BoxBlur(1))  
blur_Image.show()  

#########################################################################
#########################################################################


#########################################################################
         #################### OPS ########################
#########################################################################

# Ajuste le contraste et applique divers traitement directement
im_auto_con = ImageOps.autocontrast(image=im, cutoff=5)
im_auto_con.show() 

# redimensionne une photo technique 2
im_resize = ImageOps.scale(image = im, factor = 0.4)
im_resize.show()

# pour garder un ratio normal et ne pas risquer de déformer mon image avec une largeur ou hauteur trop importante
# ici par exemple une largeur de 500 est trop importante, pillow gardera donc une largeur de 300 pour ne pas déformer l'image
im_contain = ImageOps.contain(image = im, size = (500,200))
im_contain.show()

# ajoute un cadre de 100 px autour de mon image, par défaut de couleur noir, sinon on change avec fill
im_border = ImageOps.expand(image = im, border =100, fill = (255,255,0))
im_border.show()

# pour rogner mon image de 100px de chaques côtés
im_crop = ImageOps.crop(image = im, border = 100)
im_crop.show()

#########################################################################
#########################################################################


#########################################################################
         #################### DEFORMER ########################
#########################################################################

class Deformer():
    def getmesh(self, im):
        w, h = im.size
        # les coordonnées des 4 angles de mon img en partant du coin haut gauche puis dans le sens inverse des aiguilles d'une montre
        # voir deform_1.png
        im_shape_source = (0,0,0,h,w,h,w,0)
        # dimensions du rectangle de notre img qui servira pour analyse (convolution tensorflow) en partant de l'angle en haut à gauche
        # de position x et y 0, puis 100 de largeur par 200 de hauteur
        im_target_rect = (0,0,100,200)

        return [(im_target_rect, im_shape_source)]

im_deform = ImageOps.deform(im, Deformer())
im_deform.show()

#########################################################################
#########################################################################

#########################################################################
         #################### DRAW ########################
#########################################################################

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

draw.text((x, y), text, font=font)  
#im.show()  

# intègre du texte à une image 
img = im.convert('RGBA')  
text = Image.new('RGBA', im.size, (255,255,255,0))  
d = ImageDraw.Draw(text) 

# en param le positionnement du texte dans la photo, le texte à intégrer, les 3 premier param de
# fill sont les 3 octets pour la couleur et le dernier la transparence de 0 à 255
d.text((14,14), "Tutorials", fill=(255,4,255,128)) 
d.text((14,60), "Point", fill=(255,255,255,255)) 

out = Image.alpha_composite(img, text)    
#out.show() 

# pour dessiner des formes avec draw
# 100 = x (départ à gauche), 150 = y (départ du haut), 120 = largeur rectangle (x + 20px), 250 = hauteur rectangle (y + 100)
x = 100
y = 150
largeur = x + 20
hauteur = y + 100
draw.rectangle((x,y,largeur,hauteur), fill=(255,0,0), outline="red", width=5)
# un ovale ou rond en fonction des dimensions passés en param
draw.ellipse((x,y,largeur,hauteur), fill=(255,0,0), outline="yellow", width=2)
# un polygone de la forme que l'on souhaite en param ce sera un tuple de tuple
draw.polygon(((0,0), (100,0), (100, 100), (50,200)))
# un trait avec un tuple de tuple en premier le point de départ avec x et y puis le point d'arrivée x et y
draw.line(((80,100), (110, 150)))
# un arc de cercle, un tuple point départ et point d'arrivée avec la valeur d'où le tracé démarre et où il s'arrête en degrés
draw.arc((400, 100, 500, 200), start = 0, end =50, width=5)
# un demi cercle fermé
draw.chord((400, 100, 500, 200), start = 0, end = 100, width=5)
# une partie d'un camembert pour graphique par exemple
draw.pieslice((400, 100, 500, 200), start = 0, end = 100, width=5)
im.show()

#########################################################################
#########################################################################


#########################################################################
        #################### COMBINE IMAGE ########################
#########################################################################

# superpose 2 images de même taille, la valeur float sera de 0 à 1 pour la transparence
second_im = Image.open("lenna_rotate.png") 
im_mix = Image.blend(im, second_im, 0.5)
#im_mix.show()

# ajoute une image à la première même si celle ci n'est pas de même taille 
im_logo = Image.open("logo.png")
im_logo = ImageOps.scale(image = im_logo, factor = 0.4)
# le tuple est pour le positionnement de l'image que j'insère, mask est pour une image avec transparence
im.paste(im_logo,(100,200), mask=im_logo) 
im.show()

#########################################################################
#########################################################################


#########################################################################
        #################### MASK ########################
#########################################################################

# fusionne 2 image selon un mask noir et blanc
mask = Image.open("mask.png").convert("RGBA").resize(im.size)
im_mask = Image.composite(im,Image.open("lenna_rotate.png"), mask)
im_mask.show()

#########################################################################
#########################################################################


# redimensionner une photo
im_resize = im.resize((im.width*2, im.height*2))
im_resize.show()

# extrait un bout de mon image
# comme css mes 4 côtés dans le sens des aiguilles d'une montre en partant du côté gauche
im = im.crop((0,0,20,20))
im.show() 

# Show rotated Image, l'arg "expand=true" permet d'étendre les côtés de l'image pour ne pas couper les angles lors de la rotation
# fillcolor remplit les contours avec une couleur passé en param, par défaut ils sont noirs
# print(ImageColor.colormap) pour voir les couleurs natives dispos 
imim = im.rotate(45, fillcolor="blue")  
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

# affiche le code de la couleur passé en param encodé sur 3 octet ex : (255, 255, 0)
blue = ImageColor.getrgb("blue")  
print(blue)  

# créera une image de taille 256 pixels par 256 pixels avec une unique couleur de code "#add8e6"
img = Image.new("RGB", (256, 256), ImageColor.getrgb("#add8e6"))  
img.show() 

# inverse le sens d'une photo horizontalement
im_flip = im.transpose(Image.FLIP_LEFT_RIGHT)

# inverse le sens d'une photo de bas en haut
im_flip = im.transpose(Image.FLIP_TOP_BOTTOM) 
im_flip.show()

# convertit l'image en noir et blanc
image = im.convert('L')
image.show()
