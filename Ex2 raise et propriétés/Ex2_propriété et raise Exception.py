from math import pi
#1. Ajouter un raise Exception qui lèvera une exception de type TypeError si le type de paramètre passé
#        lors du __init__ n’est pas un int ou float ( vous pouvez utiliser la fonction type() )

#2.	Ajouter un raise Exception qui lèvera une exception de type ValueError  si la valeur du rayon est 
#       égale ou inférieure à 0

#3.	Terminer la propriété rayon

#4.	Ajouter un setter à la propriété rayon. Le setter doit faire les mêmes vérifications que dans 
#       le __init__ afin de s’assurer que le rayon est correct.

#5.	Terminer les propriétés, circonférence, volume et aire qui ont déjà été déclarés dans la classe.
#       (NOTEZ : la valeur de pi à été importer, vous pouvez utilisé pi comme une constante)




class Sphere:
    def __init__(self, pRayon) -> None:
        self._rayon = pRayon
        
    @property
    def rayon(self,pRayon) :
        if type(pRayon) != int and type(pRayon) != float:
            raise TypeError ("Veuillez changer le type")
        if pRayon <= 0:
            raise ValueError ("Veuillez mettre une valeur positive + que 0")
        else:
            self._rayon = pRayon
    
    def set_rayon(self,pRayon):
        self._rayon = pRayon

        if type(pRayon) != int and type(pRayon) != float:
            raise TypeError ("Veuillez changer le type")
        if pRayon <= 0:
            raise ValueError ("Veuillez mettre une valeur positive + que 0")
        else:
            self._rayon = pRayon

    @property
    def circonference(self,pRayon):
        self.circonference = 2 * pi * pRayon
        return self.circonference # la circonférence d'une sphère est égal à " 2 * pi * rayon "

    @property
    def volume(self):
         # le volume d'une sphère est égale à " 4/3 * pi * (rayon ** 3) "

    @property
    def aire(self):
        pass


if __name__ == "__main__" :
    print(pi) #voyez que vous pouvez utilisé la constante pi

    #Testez votre code, voir l'énoncé

