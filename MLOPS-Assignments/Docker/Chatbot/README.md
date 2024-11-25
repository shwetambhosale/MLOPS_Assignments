# Chatbot
Generative AI

# PDF Question Answering Chatbot

This is a Streamlit-based web application that allows users to upload PDF files and ask questions about their content. The app uses the Sentence Transformers for embedding generation, FAISS for similarity search, and a pre-trained DistilBERT model for question answering.

## Features

- Upload PDF files
- Extract and process text from the PDFs
- Ask questions about the PDF content
- Get answers from the relevant sections of the document

## Installation

### Step 1: Clone the Repository

### Step 2: Install Dependencies
Install the required Python packages using pip:
pip install streamlit PyPDF2 sentence-transformers faiss-cpu transformers nltk

### Step 3: Run the Application
Run the Streamlit app using the following command:
streamlit run chatbot.py
