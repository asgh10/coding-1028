import streamlit as st
import time
import datetime 

st.title("사용자 정보")

message_placeholder = st.empty()

with st.form(key="my_infrom"):

    name = st.text_input("이름", placeholder= "이름을 입력해주세요 (예: 김현빈)")
    
    age = st.text_input(
        "나이",max_chars=4 ,placeholder= "나이를 입력해주세요 (숫자만 입력 해주세요)"
    ).replace(" ", "").replace("살", "")

    job = st.text_input("직업", placeholder="직업을 입력해주세요 (예: 학생)")
    
    phone_number = st.text_input(
        "전화번호", value="", max_chars=13, placeholder="전화번호를 입력 해주세요 ('-' 없이 입력 해주세요)"
    ).replace(" ", "").replace("-", "")

    submitted = st.form_submit_button("제출")

if submitted:
    message_placeholder.info(f"이름: {name}  \n"
                             f"나이: {age}  \n"
                             f"직업: {job}  \n"
                            f"전화번호: {phone_number}"
                            )
    time.sleep(15)
    message_placeholder.empty()

    






