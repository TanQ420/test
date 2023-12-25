import streamlit as st
import os
import speech_recognition as sr
import tempfile

st.title('Speech to Text')

uploaded_files = st.file_uploader("Choose files", accept_multiple_files=True)

for uploaded_file in uploaded_files:
    with tempfile.NamedTemporaryFile(delete=False) as fp:
        fp.write(uploaded_file.getvalue())
    r = sr.Recognizer()

    try:
        with sr.AudioFile(fp.name) as source:
            audio = r.record(source)
            text = r.recognize_google(audio, language="ja-JP")

        st.write(f'File {uploaded_file.name}:')
        st.write(text)
        st.success('Finished processing')
        os.unlink(fp.name)  # remove temp file

    except Exception as e:
        st.write('Failed to process the audio')
        st.error(f'Error: {e}')

        if os.path.exists(fp.name): # if file still exists, remove it
            os.unlink(fp.name)
