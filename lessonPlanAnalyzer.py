
#Interpretation tools
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import NLTKTextSplitter


text_loader_kwargs = {'autodetect_encoding': True}
loader = DirectoryLoader("./cleanedData", glob="*.txt", loader_cls=TextLoader, loader_kwargs=text_loader_kwargs)

documents = loader.load()
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2", model_kwargs={'device': 'cpu'})

option = input("Select a type of chunking algorithm to perform on the Music Blocks Lesson Plans (Answer 'Natural Language' OR 'Recursive'): ")

if (option.lower() == "natural language"):
    # NLTK
    import nltk
    nltk.download('punkt')
    natLangSplitter = NLTKTextSplitter()
    texts = natLangSplitter.split_documents(documents)
    db = FAISS.from_documents(texts, embeddings)
    db.save_local("faissNLTK")

elif (option.lower() == "recursive"):
    # Recursive splitter
    recursiveSplitter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=100)
    texts = recursiveSplitter.split_documents(documents)
    db = FAISS.from_documents(texts, embeddings)
    db.save_local("faissRecursive")





