import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

matrice = cv.imread("lenna.png")   # charge le fichier dans une matrice de pixels couleur
print(matrice.shape)              # affiche les dimensions de la matrice (512 pixels par 512 et 3 octets par pixel) (512, 512, 3)
# accède à la valeur du premier pixel [ligne, colonne] [125 137 226] 1 octet = 0 à 255 lire en Bleu = 125 Vert = 137 Rouge = 226
print(matrice[0,0])   

matG = cv.cvtColor(matrice, cv.COLOR_BGR2GRAY) # conversion des triplets BVR en gris
# (512, 512)
print(matG.shape)
# 162 en gris je n'ai plus qu'une valeur de 0 à 255 sur un octet / 0 étant le noir, 255 le blanc
print(matG[0,0])

matG = cv.imread("lenna.png", 0)  # charge le fichier dans une matrice de pixels gris
plt.imshow(matG, cmap = 'gray')  # affiche la matrice de niveaux de gris
plt.show()

plt.imshow(matrice[..., ::-1])  
plt.show() # affiche l'image d'origine

#################################################################################################

########################### Conversion image en gris avec luminance y ###########################

#################################################################################################

b,v,r = cv.split(matrice)         # récupère 3 matrices d'octets séparées pour R et V et B
y = 0.299*r + 0.587*v + 0.114*b     # opération matricielle, avec les valeurs de l'algorithme de Luminance Y
y = y.astype(np.uint8)          # convertit les réels en octets

cv.imshow("Luminance Y", y) # premier param pour le titre de ma fenètre (obligatoire)
cv.waitKey(0)   # permet de laisser l'image affiché
cv.destroyAllWindows() # détruit toutes les images affichés

# Calcule l'histogramme de l'image, nombre de fois où apparait une valeur 
# exemple : 0 = noir apparait 2 fois dans mon image dans 2 pixels différents
hist = np.zeros(256, int)       # prépare un vecteur de 256 zéros (pour chaque gris)
for i in range(0,matrice.shape[0]):      # énumère les lignes
    for j in range(0,matrice.shape[1]):  # énumère les colonnes
        hist[y[i,j]] = hist[y[i,j]] + 1

print(hist)
plt.plot(hist)
plt.show()


#################################################################################################

############################### Augmente contraste image en gris  ###############################

#################################################################################################


# Calcule l'histogramme cumulé hc
hc = np.zeros(256, int)         # prépare un vecteur de 256 zéros
hc[0] = hist[0]
for i in range(1,256):
    hc[i] = hist[i] + hc[i-1]

# Normalise l'histogramme cumulé
nbpixels = y.size
hc = hc / nbpixels * 255
print(hc)
plt.plot(hc)
plt.show()

# Utilise hc comme table de conversion des niveaux de gris
for i in range(0,y.shape[0]):       # énumère les lignes
    for j in range(0,y.shape[1]):   # énumère les colonnes
        y[i,j] = hc[y[i,j]]
cv.imshow("Luminance Y apres egalisation", y)
cv.waitKey(0)
cv.destroyAllWindows()

#################################################################################################

############################### cache message dans autre image  ###############################

#################################################################################################


message = cv.imread("message.png",0)

b,v,r = cv.split(matrice)        # récupère 3 matrices d'octets séparées
b = b & 0b11111110             # efface le bit de poids faible des octets de b (bit de poid faible = bit le plus à droite)
                               # octet = 162, en bit = 10100010
b = b | (message > 0)          # ajoute le bit de de poids faible en fonction du message

cache = cv.merge((b,v,r))      # reconstruit une image à partir des 3 plans RVB
cv.imwrite("cache.png", cache)

cv.imshow("Image avec contenu caché", cache)
cv.waitKey(0)
cv.destroyAllWindows()

image = cv.imread("cache.png")

# Extrait le contenu caché en bit de poids faible de la composante B
b,v,r = cv.split(image)         # récupère 3 matrices d'octets séparées
cache = b & 1                   # extrait le 1er bit (de poids faible)
cache = cache * 255             # multiplie par 255 pour visualiser du noir ou du blanc

cv.imshow("Contenu caché", cache)
cv.waitKey(0)
cv.destroyAllWindows()