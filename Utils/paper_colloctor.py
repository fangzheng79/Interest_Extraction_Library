import semanticscholar as sch 
from langdetect import detect
import json

def papercollector(id, year):
    author = sch.author(id)
    paper = author["papers"]
    collectedpapers=[]
    for p in paper:
        if p["year"]==year:
            a=sch.paper(p["paperId"])["abstract"]
#             print(a)
            try:
                lan = detect(a)
#                 print(lan)
                if lan == 'en':
                    p["abstract"]=a
                    collectedpapers.append(p)
            except TypeError:
                collectedpapers.append(p)
    print(collectedpapers)
    return collectedpapers


if __name__ == "__main__":
    id = 1724546
    year = 2019
    papercollector(id,year)
