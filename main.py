import streamlit as st
import tempfile
import os
from PIL import Image

#st.balloons()

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", type="password")

#제목
st.title("SightnSpeak")
st.write("---")

# 방 이미지
room_img = Image.open('livingroom.jpg')
# 이미지 크기 조정
room_img = cyworld_img.resize((650, int(650 * (cyworld_img.height / cyworld_img.width))))
st.image(cyworld_img, width=650)
st.write("---")

    
# 메뉴 선택
selected_option = st.selectbox('선택할 기기를 바라보세요', ['TV', '가습기', '에어컨'])


# 사용자가 선택한 옵션에 따라 다른 콘텐츠 표시
if selected_option == 'TV':
    tv_img = Image.open('person_TV.jpg')
    tv_img = tv_img.resize((100, 100))
    st.image(tv_img)
    
    st.success('당신은 TV를 바라보고 선택하였습니다!')
    st.header('TV :sunglasses:',divider='rainbow')

    tv_question = st.text_input('TV에게 질문을 입력하세요')
    
    st.button('TV에게 질문하기', key='tv_button')



elif selected_option == '가습기':

    st.success('당신은 가습기를 바라보고 선택하였습니다!')
    st.header('가습기 :sunglasses:',divider='rainbow')

elif selected_option == '에어컨':
    st.success('당신은 에어컨을 바라보고 선택하였습니다!')
    st.header('에어컨 :sunglasses:',divider='rainbow')
   
