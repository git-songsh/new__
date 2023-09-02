import streamlit as st

st.balloons()

#제목
st.title("SightnSpeak")
st.write("---")

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", type="password")

    st.write("---")
    
    # 메뉴 선택을 위한 사이드바

selected_option = st.selectbox('선택할 기기를 바라보세요', ['TV', '가습기', '에어컨'])


# 사용자가 선택한 옵션에 따라 다른 콘텐츠 표시
if selected_option == 'TV':
    st.header('TV :sunglasses:',divider='rainbow')

    st.success('당신은 TV를 바라보고 선택하였습니다!')
    # 페이지 1의 내용을 표시

elif selected_option == '가습기':
    st.title('가습기')
    st.success('당신은 가습기를 바라보고 선택하였습니다!')
    # 페이지 2의 내용을 표시

elif selected_option == '에어컨':
    st.title('에어컨')
    st.success('당신은 에어컨을 바라보고 선택하였습니다!')
    # 페이지 3의 내용을 표시
