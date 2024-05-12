# Use this file to process recursive faiss files found in the './faissRecursive' directory


# Loading tools
from langchain_community.llms import CTransformers
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS


# prepare the template we will use when prompting the AI
template = """Use the inputted data as templates to generate new lesson plan data pertaining to music and computer science based on the prompt.
The lesson plans should revolve around the use of block coding in a software called Music Blocks.
If you don't know the answer, just say that you don't know, don't try to make up an answer. 
Context: {context}
Question: {question}
Return the answer parsed in the following sections:

Introduction
Age
Lesson Duration
Part 1
Part 2
Part 3
Conclusion

answer:
"""

# load the language model
llm = CTransformers(model='./llama-2-7b-chat.ggmlv3.q2_K.bin',
                    model_type='llama',
                    config={'max_new_tokens': 512, 'temperature': 0.1, 'context_length': 1500})

# load the interpreted information from the local database
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={'device': 'cpu'})


db = FAISS.load_local("faissRecursive", embeddings, allow_dangerous_deserialization=True)

# prepare a version of the llm pre-loaded with the local content
retriever = db.as_retriever(search_kwargs={'k': 2})
prompt = PromptTemplate(
    template=template,
    input_variables=['context', 'question'])
qa_llm = RetrievalQA.from_chain_type(llm=llm,
                                     chain_type='stuff',
                                     retriever=retriever,
                                     return_source_documents=True,
                                     chain_type_kwargs={'prompt': prompt})

# ask the AI chat about information in our local files
topic = input("Give a topic related to music or computing for Llama2 to generate a lesson plan for: ")
prompt = "Create a detailed lesson plan about " + topic + "."
output = qa_llm({'query': prompt})

print("\nContent chunking: \n")
print("-----------------------\n")
print(output["result"])
