
from Keyword_Extractor.extractor import getKeyword

text ='Personalization is crucial for achieving smart learning environments in different lifelong learning contexts. There is a need to shift from one-size-fits-all systems to personalized learning environments that give control to the learners. Recently, learning analytics (LA) is opening up new opportunities for promoting personalization by providing insights and understanding into how learners learn and supporting customized learning experiences that meet their goals and needs. This paper discusses the Personalization and Learning Analytics (PERLA) framework which represents the convergence of personalization and learning analytics and provides a theoretical foundation for effective analytics-enhanced personalized learning. The main aim of the PERLA framework is to guide the systematic design and development of effective indicators for personalized learning.'

keyword = getKeyword(text, model= "Yake" ,num = 20)

print(keyword)

