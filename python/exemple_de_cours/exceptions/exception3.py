print("Debut de mon programme")


nombre_modules = 2

try:
#    ma_super_phrase = "Hands On les cours qui dechirent ! Nombre de modules : " + nombre_modules
#    print(ma_super_phrase)

#    mon_super_calcul = 18.06 / 0

    print(variable_non_declaree)
except TypeError as err:
    print("Erreur de type! En Python que des transtypages explicites! Allez relire cette partie du cours ;)")
    print(err)
except ZeroDivisionError as err:
    print("Une division par zero !!! On aurait limite pas besoin de l'afficher celle-ci !")
    print(err)
except Exception as err:
    print("Erreur non anticipee ! Affichage de l'erreur ci-dessous :")
    print(err)
finally:
    print("Hands On ca dechire !")


print("Fin de mon programme")
