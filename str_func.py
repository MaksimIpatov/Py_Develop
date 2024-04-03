def upper(x): """Функция написана"""
    for c in x:
        if c.isupper():
            return(c)
        elif x.islower():
            return('')
def Capitalize(S):    """function создана разработчиком № 2 !!!!"""
   return S.title()    """Function"""
S = input()
print (Capitalize(S))