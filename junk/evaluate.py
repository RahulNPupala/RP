# Evaluation
# compare the generated output string with the given output for the training data

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-mpnet-base-v2")

def semantic_score(expected, predicted):
    e = model.encode(expected)
    p = model.encode(predicted)

    return cosine_similarity([e], [p])[0][0]