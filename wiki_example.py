from Semantic_Enrichment.wiki_filter import wikifilter
from Semantic_Enrichment.wiki_category import wikicategory

keywords_based_interests= {'personalized learning': 3, 'different lifelong learning contexts': 1, 'learning analytics': 3, 'learning environments': 2, 'learning experiences': 1, 'moocs': 1, 'personalization': 4, 'personal learning environment': 1, 'MOOC': 4, 'effective indicators': 1, 'systematic design': 1, 'theoretical foundation': 1, 'main aim': 1, 'new opportunities': 1, 'perla': 2, 'framework': 2, 'environments': 2, 'smart phones': 2, 'applications': 1}

mapping = wikifilter(keywords_based_interests)[0]
wiki_interests = wikifilter(keywords_based_interests)[1]


top5intersts = sorted(wiki_interests.items(), key = lambda item:item[1], reverse = True)[:5]
top = {}
for i in top5intersts:
    top[i[0]]= i[1]

cat = []
for t in top.keys():
    cat+=wikicategory(t)

category = list(set(cat))



print(wiki_interests)
print(category)
print(mapping)


