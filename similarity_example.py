from Semantic_Similarity.WikiLink_Measure.Wiki import wikisim
from Semantic_Similarity.Word_Embedding.IMsim import calculate_similarity

s = ["Learning", "Massive open online course","Learning analytics","Analytics","Peer assessment"]

t = ["Educational technology","data datatest","Social network analysis","Learning"]

sim_scores = calculate_similarity(s, t)

print(sim_scores)

# print(wikisim(s,t))