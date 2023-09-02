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

st.write('이곳은 당신의 집 입니다.')

# 방 이미지
room_img = Image.open('livingroom.jpg')
# 이미지 크기 조정
room_img = room_img.resize((650, int(650 * (room_img.height / room_img.width))))
st.image(room_img, width=650)

# 메뉴 선택
selected_option = st.selectbox('선택할 기기를 바라보세요!', ['기기 선택', 'TV를 바라본다', '가습기를 바라본다', '에어컨을 바라본다'])


# 사용자가 선택한 옵션에 따라 다른 콘텐츠 표시
if selected_option == '기기 선택':
    st.write(" ")
    
elif selected_option == 'TV를 바라본다':
    tv_img = Image.open('person_TV.jpg')
    tv_img = tv_img.resize((100, 100))
    st.image(tv_img)
    
    st.success('당신은 TV를 선택하였습니다!')
    st.header('TV :sunglasses:',divider='rainbow')

    tv_question = st.text_input('TV에게 질문을 입력하세요!')
    st.caption('ENTER로 입력')

elif selected_option == '가습기를 바라본다':
    hm_img = Image.open('person_HM.jpg')
    hm_img = hm_img.resize((100, 100))
    st.image(hm_img)
    
    st.success('당신은 가습기를 선택하였습니다!')
    st.header('가습기 :sunglasses:',divider='rainbow')

    hm_question = st.text_input('가습기에게 질문을 입력하세요!')
    st.caption('ENTER로 입력')
    
elif selected_option == '에어컨을 바라본다':
    ac_img = Image.open('person_AC.jpg')
    ac_img = ac_img.resize((100, 100))
    st.image(ac_img)
    
    st.success('당신은 에어컨을 선택하였습니다!')
    st.header('에어컨 :sunglasses:',divider='rainbow')

    ac_question = st.text_input('에어컨에게 질문을 입력하세요!')
    st.caption('ENTER로 입력')
