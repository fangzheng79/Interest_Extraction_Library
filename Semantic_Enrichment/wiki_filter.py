import wikipediaapi
import requests
import json
from pattern.text.en import singularize



def wikifilter(keyword):
    wiki_wiki = wikipediaapi.Wikipedia('en')
    candidate = {}
    final = {}
    redirect = {}
    relation = {}
    
    
    for key in keyword.keys():
        page_py = wiki_wiki.page(key)
        if page_py.exists() == True:
            query = requests.get(r'https://en.wikipedia.org/w/api.php?action=query&titles={}&&redirects&format=json'.format(key))
            data = json.loads(query.text)
            PAGES = data["query"]["pages"]
            #print(PAGES)
            for v in PAGES.values():
                redirect[key]= v["title"]
                #print(redirect)
                temp_list = relation.get(v["title"], [])
                temp_list.append(key)
                relation[v["title"]] = temp_list
                #print(relation)
                final[v["title"]]=0  
            
        elif page_py.exists() == False:
            singles = singularize(key)
            page_py = wiki_wiki.page(singles)
            if page_py.exists() == True:
                query = requests.get(r'https://en.wikipedia.org/w/api.php?action=query&titles={}&&redirects&format=json'.format(singles))
                data = json.loads(query.text)
                PAGES = data["query"]["pages"]
                #print(PAGES)
                for v in PAGES.values():
                    redirect[key]= v["title"]
                    #print(redirect)
                    temp_list = relation.get(v["title"], [])
                    temp_list.append(key)
                    relation[v["title"]] = temp_list
                   # print(relation)
                    final[v["title"]]=0

    for k in redirect.keys():
        final[redirect[k]]=  final[redirect[k]]+keyword[k]
#     print(final)
    
    
    return relation, final
