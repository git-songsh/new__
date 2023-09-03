import sqlite3
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


#st.balloons()
tv_mg = st.chat_message("tv", avatar = '📺')
tv_mg.write("fff")


#제목
st.title("LooknTalk")
st.write("---")
st.write('이곳은 당신의 집 입니다.')

# 방 이미지
room_img = Image.open('livingroom2.jpg')
# 이미지 크기 조정
room_img = room_img.resize((650, int(650 * (room_img.height / room_img.width))))
st.image(room_img, width=650)

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", type="password")

# 초기 세션 상태 설정
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = {'AC': [], 'TV': [], 'HM': []}

# 메뉴 선택
selected_option = st.selectbox('선택할 기기를 바라보세요!', ['기기 선택', 'TV를 바라본다', '가습기를 바라본다', '에어컨을 바라본다'])


# 사용자가 선택한 옵션에 따라 다른 콘텐츠 표시
if selected_option == '기기 선택':
    st.write(" ")

elif selected_option == 'TV를 바라본다':

  tv_img = Image.open('person_TV.jpg')
  tv_img = tv_img.resize((100, 100))
  st.image(tv_img)
  
  st.success('당신은 *TV*를 선택하였습니다!')
  st.header('📺TV :sunglasses:',divider='rainbow')

  tv_question = st.text_input('TV에게 질문을 입력하세요')
  if st.button('TV에게 질문하기', key='tv_button'):
      with st.spinner('Wait for it...'):
          llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
          qa_chain = RetrievalQA.from_chain_type(llm, retriever=db_tv.as_retriever())
          result = qa_chain({"query": tv_question})
          st.session_state.chat_history['TV'].append({"question": tv_question, "answer": result["result"]})

  for chat in st.session_state.chat_history.get('TV', []):
      st.text(f"📺 TV - 🤔 {wrap_text(chat['question'])}")
      st.text(f"📺 TV - 😊 {wrap_text(chat['answer'])}")
      st.write("---")

elif selected_option == '가습기를 바라본다':

  st.success('당신은 가습기를 선택하였습니다!')
  st.header('💧가습기 :sunglasses:',divider='rainbow')

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


elif selected_option == '에어컨을 바라본다':
    ac_img = Image.open('person_AC.jpg')
    ac_img = ac_img.resize((100, 100))
    st.image(ac_img)
    
    st.success('당신은 에어컨을 선택하였습니다!')
    st.header('❄️에어컨',divider='rainbow')

    ac_question = st.text_input('에어컨에게 질문을 입력하세요!')
    st.caption('ENTER로 입력')
    

