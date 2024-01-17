import streamlit as st
import requests
#from requests_toolbelt.multipart.encoder import MultipartEncoder



st.title('An end to end text to speech  model')



def process():
  with st.spinner(text='In progress'):
    
    
    r = requests.post (backend , data={"text": text}, stream = True)
    st.audio(r.raw.read() , format="audio/wav", start_time=0, sample_rate=48000)
    st.write(r.text)  
    st.success('Done')



language = st.selectbox("Pick the text language", ['English' , "German" , "spanish" ,"french"] , key ="language")
opt_text = st.radio('Pick one', ['type text', 'upload text'] , key ="opt_text" )
if opt_text == 'type text' :
  text = st.text_area('Type Text to record here')
  
elif opt_text == 'upload text':
  text = st.file_uploader("Or simply Upload a text file" , type = ["txt" , "py"])
  if not text == None : text = text.read() ;

st.button("submit", key=None, help=None, on_click=process)
backend = f"http://fastapi:8000/{language.lower()}"


st.write("Citations")

st.code(r"""@misc{Silero Models,
  author = {Silero Team},
  title = {Silero Models: pre-trained enterprise-grade STT / TTS models and benchmarks},
  year = {2021},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/snakers4/silero-models}},
  commit = {insert_some_commit_here},
  email = {hello@silero.ai}
}""" , language ="markdown")



