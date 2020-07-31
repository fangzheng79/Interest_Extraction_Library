import wikipediaapi


def wikicategory(interest):
    symbols = ['0','1','2','3','4','5','6','7','8','9','(',')',',']
    stoplist = ['of', 'by','lists','from','articles','terms']
    wiki = wikipediaapi.Wikipedia('en')
    categorie = []
    noise = []
    l = wiki.page(interest)
    a = wiki.categories(l, clshow='!hidden')

    for k in a.keys():
        cat = k.replace("Category:","")
        if len(cat.split())<= 4 and cat!='Disambiguation pages':
            categorie.append(cat)

    for s in symbols:
        for c in categorie:
            if s in c.lower():
                 noise.append(c)
            
    for c in categorie:
        for s in stoplist:
            if s in c.lower().split():
                noise.append(c)
    
    noise = list(set(noise))
    
    for n in noise:
        categorie.remove(n)

    return categorie
            
if __name__ == "__main__":
    print(wikicategory("Analytics"))
    
