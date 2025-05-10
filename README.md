# Amazon Product Search Engine

This project demonstrates a search engine built using the Amazon product dataset. It allows users to search for products by embedding product titles into vector space and retrieving similar items based on user queries.

## Project Overview

The core of the search engine uses `txtai`, an AI-powered search library that leverages embeddings to convert textual data (product titles) into vector space. By using similarity measures, the engine can retrieve products that are most relevant to a user's query. The application is deployed using Streamlit for an interactive user interface.

### Features

- **Product Search**: Users can input a query, and the search engine will return the most similar product titles from the dataset.
- **Vector-based Search**: The product titles are converted into embeddings for similarity-based searching, allowing for more accurate and context-aware results.
- **Interactive UI**: The search engine is presented with an easy-to-use web interface, powered by Streamlit.

### Technology Stack

- **Python**: The backend is written in Python.
- **txtai**: For vector-based search and embedding generation.
- **Streamlit**: A web framework for creating the interactive frontend.
- **Pandas**: For data manipulation and handling CSV files containing Amazon product information.

### Project Files

- `main.py`: The main script for setting up the vector store, generating embeddings, and performing search operations.
- `main.streamlit.py`: The Streamlit script responsible for the user interface, which allows users to interact with the search engine and view results.

## Setup Instructions

To run this project locally, follow these steps:

### Prerequisites

-Make sure you have Python 3.7 or higher installed.

### Download all the requirements
- Refer to Requirement.txt 

### Download the Amazon Dataset as csv file from Kaggle
https://www.kaggle.com/datasets/piyushjain16/amazon-product-data

