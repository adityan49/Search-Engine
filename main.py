import txtai
import numpy as np
import pandas as pd

np.random.seed(1)
df = pd.read_csv('train.csv')

titles = df.dropna().sample(100000).TITLE.values

embeddings = txtai.Embeddings({
    'path': 'sentence-transformers/all-MiniLM-L6-v2'
})

embeddings.index(titles)
embeddings.save('embeddings.tar.gz')

result = embeddings.search('protector for cam', 5)

print(result)

actual_results = [titles[x[0]] for x in result]

print(actual_results)