import streamlit as st

def count_characters(text):
    return len(text)

def split_by_length(text, split_length):
    return [text[i:i + split_length] for i in range(0, len(text), split_length)]

def main():
    st.title("文字数カウンター & 分割ツール")
    input_text = st.text_area("文章を入力してください")
    
    # Split length input
    split_length = st.number_input("分割する文字数を入力してください", min_value=1, step=1)

    if st.button("カウント"):
        character_count = count_characters(input_text)
        st.write("入力された文章の文字数は", character_count, "です")

    if st.button("分割"):
        split_text = split_by_length(input_text, split_length)
        st.write("入力された文章を", split_length, "文字で分割した結果は以下のとおりです:")
        for i, text_chunk in enumerate(split_text):
            st.write(f"チャンク {i+1}: {text_chunk}")

if __name__ == "__main__":
    main()
