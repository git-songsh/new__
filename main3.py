import streamlit as st
import tempfile
import os
from PIL import Image
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

def pdf_to_document(uploaded_file):
    temp_dir = tempfile.TemporaryDirectory()
    temp_filepath = os.path.join(temp_dir.name, uploaded_file.name)
    with open(temp_filepath, "wb") as f:
        f.write(uploaded_file.getvalue())
    loader = PyPDFLoader(temp_filepath)
    pages = loader.load_and_split()
    return pages

#업로드 되면 동작하는 코드
if uploaded_file is not None:
    pages = pdf_to_document(uploaded_file)

    #Split
    text_splitter = RecursiveCharacterTextSplitter(
        # Set a really small chunk size, just to show.
        chunk_size = 300,
        chunk_overlap  = 20,
        length_function = len,
        is_separator_regex = False,
    )
    texts = text_splitter.split_documents(pages)

    #Embedding
    embeddings_model = OpenAIEmbeddings()

    persist_directory = 'db'
    # load it into Chroma
    db = Chroma.from_documents(documents=texts,
                                 embedding=embeddings_model,
                                 persist_directory=persist_directory)
    db.persist()
    db = None
    db = Chroma(persist_directory=persist_directory,
                  embedding_function=embeddings_model)

#st.balloons()

#제목
st.title("SightnSpeak")
st.write("---")

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", type="password")

# 초기 세션 상태 설정
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = {'AC': [], 'TV': [], 'HM': []}

    
# 메뉴 선택
selected_option = st.selectbox('선택할 기기를 바라보세요', ['TV', '가습기', '에어컨'])


# 사용자가 선택한 옵션에 따라 다른 콘텐츠 표시
if selected_option == 'TV':
  db_tv = document_to_db(tv_file)

  tv_img = Image.open('person_TV.jpg')
  tv_img = tv_img.resize((100, 100))
  st.image(tv_img)
  
  st.success('당신은 TV를 바라보고 선택하였습니다!')
  st.header('TV :sunglasses:',divider='rainbow')

  tv_question = st.text_input('TV에게 질문을 입력하세요')

  tv_question = st.text_input('TV에게 질문을 입력하세요')
  if st.button('TV에게 질문하기', key='tv_button'):
      with st.spinner('Wait for it...'):
          llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
          qa_chain = RetrievalQA.from_chain_type(llm, retriever=db_tv.as_retriever())
          result = qa_chain({"query": tv_question})
          st.session_state.chat_history['TV'].append({"question": tv_question, "answer": result["result"]})

  # 챗 기록 출력
  for chat in st.session_state.chat_history['TV']:
      st.text(f"🤔 {wrap_text(chat['question'])}")
      st.text(f"😊 {wrap_text(chat['answer'])}")
      st.write("---")

elif selected_option == '가습기':
  db_hm = document_to_db(hm_file, 300)

  st.success('당신은 가습기를 바라보고 선택하였습니다!')
  st.header('가습기 :sunglasses:',divider='rainbow')

  hm_question = st.text_input('가습기에게 질문을 입력하세요', key='hm')
  if st.button('가습기에게 질문하기'):
      with st.spinner('Wait for it...'):
          llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
          qa_chain = RetrievalQA.from_chain_type(llm, retriever=db_hm.as_retriever())
          result = qa_chain({"query": hm_question})
          st.session_state.chat_history['HM'].append({"question": hm_question, "answer": result["result"]})

  # 챗 기록 출력
  for chat in st.session_state.chat_history['HM']:
      st.text(f"🤔 {wrap_text(chat['question'])}")
      st.text(f"😊 {wrap_text(chat['answer'])}")
      st.write("---")

elif selected_option == '에어컨':
  db_ac = document_to_db(ac_file)

  st.success('당신은 에어컨을 바라보고 선택하였습니다!')
  st.header('에어컨 :sunglasses:',divider='rainbow')

  ac_question = st.text_input('에어컨에게 질문을 입력하세요', key='ac')
  if st.button('에어컨에게 질문하기'):
      with st.spinner('Wait for it...'):
          llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
          qa_chain = RetrievalQA.from_chain_type(llm, retriever=db_ac.as_retriever())
          result = qa_chain({"query": ac_question})
          st.session_state.chat_history['AC'].append({"question": ac_question, "answer": result["result"]})

  # 챗 기록 출력
  for chat in st.session_state.chat_history['AC']:
      st.text(f"🤔 {wrap_text(chat['question'])}")
      st.text(f"😊 {wrap_text(chat['answer'])}")
      st.write("---")


   
