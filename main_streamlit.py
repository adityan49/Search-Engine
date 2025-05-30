import streamlit as st
import numpy as np
import pandas as pd
import txtai

def load_data_and_embeddings():
    np.random.seed(1)
    df = pd.read_csv('train.csv')
    titles = df.dropna().sample(100000).TITLE.values

    embeddings = txtai.Embeddings({
        'path': 'sentence-transformers/all-MiniLM-L6-v2'
    })

    embeddings.load('embeddings.tar.gz')

    return titles, embeddings

titles, embeddings = st.cache_data(load_data_and_embeddings)()

st.title('Amazon Item Search Engine')

query = st.text_input('Enter a search query:', '')

if st.button('search'):
    if query:
        result = embeddings.search(query, 5)

        actual_results = [titles[x[0]] for x in result]

        for res in actual_results:
            st.write(res)
    else:
        st.write('Please enter a query')
