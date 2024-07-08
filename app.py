from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain


CHROMA_PATH = "chroma"


embedding_function = OpenAIEmbeddings()
db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)
retriever=db.as_retriever()
llm = ChatGoogleGenerativeAI(model="gemini-pro")





prompt_template = """
  Please answer the question in as much detail as possible based on the provided context.
  Ensure to include all relevant details. If the answer is not available in the provided context,
  kindly respond with "The answer is not available in the context." Please avoid providing incorrect answers.
\n\n
  Context:\n {context}?\n
  Question: \n{question}\n

  Answer:
"""

prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
chain = load_qa_chain(llm, chain_type="stuff", prompt=prompt)
question="food options at campus?"

docs = db.similarity_search("question")


response = chain(
    {"input_documents":docs, "question": question}
    , return_only_outputs=True)
print(response)



