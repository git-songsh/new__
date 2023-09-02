import streamlit as st

#제목
st.title("SightnSpeak")
st.write("---")

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", type="password")

# 메뉴 선택을 위한 사이드바
selected_option = st.sidebar.selectbox('선택할 기기를 바라보세요', ['TV', '가습기', '에어컨'])

# 사용자가 선택한 옵션에 따라 다른 콘텐츠 표시
if selected_option == 'TV':
    st.header('TV :sunglasses:',divider='rainbow')
    # 페이지 1의 내용을 표시

elif selected_option == '가습기':
    st.title('가습기')
    # 페이지 2의 내용을 표시

elif selected_option == '에어컨':
    st.title('에어컨')
    # 페이지 3의 내용을 표시
