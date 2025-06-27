import chromadb
from chromadb.config import Settings

# Initialize the ChromaDB client with a persistent storage path.
client = chromadb.PersistentClient(path="./chroma_db") 

# Get or create a collection named "storyVersions".
collection = client.get_or_create_collection(name="storyVersions")

# Function that adds document it takes ID, content, and optional metadata.
def addDocument(docID,content,metadata=None):
    """
    Adds a document to the ChromaDB collection.
    
    Parameters:
    - docID: Unique identifier for the document.
    - content: The content of the document.
    - metadata: Optional metadata associated with the document.
    """
    collection.add(
        documents=[content],
        ids=[docID],
        metadatas=[metadata] if metadata else [None]
    )
    
#Function that searches the collection for documents matching the query text.
def search(queryText, top_k=3):
    try:
        return collection.query(query_texts=[queryText], n_results=top_k)
    
    except Exception as e:
        print(f"ChromaDB query failed: {e}")
        return {"documents": []}
    