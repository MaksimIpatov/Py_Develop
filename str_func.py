def upper(x):
    for c in x:
        if c.isupper():
            return(c)
        elif x.islower():
            return('')