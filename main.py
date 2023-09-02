import streamlit as st

#제목
st.title("SightnSpeak")
st.write("---")

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", type="password")

# 메뉴 선택을 위한 사이드바
selected_option = st.sidebar.selectbox('메뉴 선택', ['페이지 1', '페이지 2', '페이지 3'])

# 사용자가 선택한 옵션에 따라 다른 콘텐츠 표시
if selected_option == '페이지 1':
    st.title('페이지 1')
    # 페이지 1의 내용을 표시
elif selected_option == '페이지 2':
    st.title('페이지 2')
    # 페이지 2의 내용을 표시
elif selected_option == '페이지 3':
    st.title('페이지 3')
    # 페이지 3의 내용을 표시
