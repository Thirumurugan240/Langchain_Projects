import streamlit as st
from summarizer import extract_video_id, fetch_transcript, summarize_transcript

st.set_page_config(page_title="Youtube summarizer", layout='centered')
st.title("Youtube Video Summarizer")

url = st.text_input("Enter video URL")

if st.button("summarize"):
    if not url.strip():
        st.warning("Please provide URL")
    else:
        with st.spinner("Fetching transcript..."):
            video_id = extract_video_id(url)
            try:
                transcript = fetch_transcript(video_id)
                with st.spinner("Summarizing"):
                    summary = summarize_transcript(transcript)
                st.subheader("Summary")
                st.write(summary)
            except Exception as e:
                st.error(f"Error :{e}")