from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunking():
    loader = PyPDFLoader(
        r"D:\AI ChatBox\Conversational-AI-Exam-Chatbot-Virtual-Invigilator\backend\test\sample.pdf"
    )

    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )

    chunks = text_splitter.split_documents(documents)

    return chunks
