import os
import re
from uuid import uuid4
from typing import List
import chromadb
from sentence_transformers import SentenceTransformer
from logger import log
import yaml
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

vector_db_path = config.get('vector_db_path',{})
inputs_path = config.get('inputs_path',{})
embedding_model = config.get('embedding_model',{})

def clean_text(text: str) -> str:
    """
    Cleans the input text by stripping extra whitespace and normalizing the spacing.
    
    Parameters:
        text (str): The text to clean.
        
    Returns:
        str: A cleaned version of the text.
    """
    # Remove leading/trailing whitespace and replace multiple spaces/newlines with a single space
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)
    return text

def split_text_to_chunks(text: str, chunk_size: int = 500, chunk_overlap: int = 50) -> List[str]:
    """
    Splits a given text into overlapping chunks.

    Parameters:
        text (str): The text to split.
        chunk_size (int): The maximum size of each chunk.
        chunk_overlap (int): The number of characters that overlap between consecutive chunks.
    
    Returns:
        List[str]: A list of text chunks.
    """
    if chunk_size <= chunk_overlap:
        raise ValueError("chunk_size must be greater than chunk_overlap")
    
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - chunk_overlap
    return chunks

def process_txt_file(file_path: str, chunk_size: int = 500, chunk_overlap: int = 50) -> List[str]:
    """
    Reads a TXT file and splits its content into chunks.

    Parameters:
        file_path (str): The path to the TXT file.
        chunk_size (int): The maximum size of each text chunk.
        chunk_overlap (int): The number of overlapping characters between chunks.

    Returns:
        List[str]: A list of text chunks.
    
    Raises:
        FileNotFoundError: If the file does not exist.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File does not exist: {file_path}")
    
    log("Chunking: " + file_path)

    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    
    # Clean the text before processing
    cleaned_text = clean_text(text)
 
    return split_text_to_chunks(text, chunk_size, chunk_overlap)

def store_chunks_in_chroma(chunks: List[str], source_file: str, collection_name: str = "txt_chunks", embedding_model_name: str = "all-MiniLM-L6-v2") -> None:
    """
    Stores text chunks into a ChromaDB collection using embeddings from a SentenceTransformer.

    Parameters:
        chunks (List[str]): List of text chunks to store.
        collection_name (str): Name of the ChromaDB collection.
        embedding_model_name (str): Name of the Sentence Transformer model to use.
    
    The function generates embeddings for each chunk, assigns unique IDs,
    and then adds them to the specified ChromaDB collection.
    """
    # Initialize the embedding model
    model = SentenceTransformer(embedding_model_name)
    
    # Generate embeddings for each chunk in a list comprehension
    embeddings = [model.encode(chunk) for chunk in chunks]
    
    # Initialize the ChromaDB client; you can pass additional parameters if needed
    client = chromadb.PersistentClient(path=vector_db_path) 
    collection = client.get_or_create_collection(name=collection_name)
     
    # Generate unique ids for each chunk
    ids = [str(uuid4()) for _ in chunks]
     
    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=ids 
    )
    log(f"Stored {len(chunks)} chunks from '{source_file}' into ChromaDB collection '{collection_name}'.")

def get_input_files():
    log("Searching in \'"+ inputs_path +"\'")
    input_files = [os.path.join(inputs_path, f) for f in os.listdir(inputs_path) if os.path.isfile(os.path.join(inputs_path, f))]
    log("Found " + str(len(input_files)) + " files")
    return input_files
   
def does_collection_exit(collection_name): 
    client = chromadb.PersistentClient(path=vector_db_path) 
    if collection_name in [c.name for c in client.list_collections()]:
        return True
    else:
        return False


if __name__ == "__main__":
    input_files = get_input_files()

    for file_path in input_files:
        # Try to add every file to ChromaDb
        try:
            file_name = os.path.basename(file_path)

            # Check if file is already stored stored as a ChromaDb collection
            collection_exists = does_collection_exit(file_path)
            if not collection_exists: 
                # Chunkatize me
                chunks = process_txt_file(file_path, chunk_size=1000, chunk_overlap=100)

                # Store the chunks in the specified ChromaDB collection
                store_chunks_in_chroma(chunks, file_name, collection_name=file_name)
            else:
                log(f"File '{file_path}' has already been processed. Skipping insertion.")

        except Exception as e:
            print(f"Error during processing: {e}")
    
