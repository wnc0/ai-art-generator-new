import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Artwork Generator")

# 从 Streamlit secrets 读取 API Key
OPENAI_KEY = st.secrets.get("OPENAI_API_KEY", "")
client = OpenAI(api_key=OPENAI_KEY)

st.title("🎨 AI Artwork Generator")
prompt = st.text_input("输入关键词，例如：wolf, city at night")

if st.button("生成图片"):
    if not prompt:
        st.warning("请输入关键词！")
    elif not OPENAI_KEY:
        st.error("未设置 OPENAI_API_KEY（在 Streamlit Secrets 中设置）。")
    else:
        with st.spinner("生成中，请稍候..."):
            try:
                resp = client.images.generate(
                    model="gpt-image-1",
                    prompt=prompt,
                    size="1024x1024"
                )
                image_url = resp.data[0].url
                st.image(image_url, caption=prompt)
            except Exception as e:
                st.error(f"出错了：{e}")
