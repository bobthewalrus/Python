x = [4, 6, 1, 3, 5, 7, 25]
def draw_stars(x):
    for element in x:
        print "*"*element

draw_stars(x)

y=[4,"Tom",1,"Michael",5,7,"Jimmy Smith"]
def draw_stars2(y):
    for element2 in y:
        if type(element2) is int:
            print "*"*element2
        elif type(element2) is str:
            lower=element2.lower()
            # element2[0].lower()
            print lower[0]*len(lower)
            # print element2[0]*element2
draw_stars2(y)
