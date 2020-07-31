import wikipediaapi
import requests
import json
from pattern.text.en import singularize



def wikifilter(keyword):
    wiki_wiki = wikipediaapi.Wikipedia('en')
    candidate = {}
    for key in keyword.keys():
        page_py = wiki_wiki.page(key)
        if page_py.exists() == True:
            candidate[key] =keyword[key]
        elif page_py.exists() == False:
            singles = singularize(key)
            page_py = wiki_wiki.page(singles)
            if page_py.exists() == True:
                candidate[singles] =keyword[key]
#     print(candidate)


    final = {}
    redirect = {}
    relation = {}
    
    for ca in candidate:
        query = requests.get(r'https://en.wikipedia.org/w/api.php?action=query&titles={}&&redirects&format=json'.format(ca))
        data = json.loads(query.text)
        PAGES = data["query"]["pages"]
        for v in PAGES.values():
            redirect[ca]= v["title"]
            relation[v["title"]] = ca
            final[v["title"]]=0

    for ca in redirect.keys():
        final[redirect[ca]]= candidate[ca]
#     print(final)
    
    
    return relation, final
