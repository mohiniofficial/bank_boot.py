import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import os
import base64

# आपकी फ्री API Key
genai.configure(api_key="AIzaSyDWDKzHdWcuVFccHwi5430TSVlnW4twiaQ")
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="बैंकिंग डायरी AI", page_icon="👩‍💼")

# --- लड़की का अवतार (Avatar) ---
# यहाँ हम एक फ्री AI इमेज का लिंक इस्तेमाल कर रहे हैं
st.markdown("<h1 style='text-align: center;'>👩‍💼 आपकी बैंकिंग असिस्टेंट</h1>", unsafe_allow_html=True)
st.image("https://img.freepik.com/free-photo/view-3d-business-woman-working-laptop_23-2150709971.jpg", width=300)

st.write("---")

# बोलकर या लिखकर हिसाब डालें
user_input = st.text_area("नमस्ते! आज का क्या हिसाब है? यहाँ लिखें या बोलें...", height=100)

if st.button("📊 हिसाब बताओ और सुनाओ"):
    if user_input:
        with st.spinner('मैं हिसाब लगा रही हूँ...'):
            prompt = f"आप एक बैंकिंग एक्सपर्ट हैं। इस हिसाब का सारांश बहुत ही सरल हिंदी में दें: {user_input}"
            response = model.generate_content(prompt)
            answer = response.text
            
            st.subheader("मेरा जवाब:")
            st.write(answer)
            
            # आवाज़ पैदा करना (TTS) - बिल्कुल फ्री
            tts = gTTS(text=answer, lang='hi')
            tts.save("response.mp3")
            
            # आवाज़ को ऑटोमैटिक बजाना
            audio_file = open("response.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mp3", autoplay=True)
            st.info("🔊 मैं बोलकर सुना रही हूँ...")
    else:
        st.warning("कृपया पहले कुछ हिसाब लिखें।")