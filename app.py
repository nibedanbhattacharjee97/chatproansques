import streamlit as st
import pandas as pd

st.image('Anudip logo.jpg', width=800)
st.set_page_config("Anudip Placement Chatbot", page_icon=":book")

def load_data():
    # Load the CSV file
    df = pd.read_csv("data.csv")
    return df

def get_answer(question, data):
    # Find the corresponding answer for the given question
    answer_row = data[data['Question'] == question]
    if not answer_row.empty:
        answer = answer_row.iloc[0]['Answer']
        picture_path = answer_row.iloc[0]['PicturePath']
        return answer, picture_path
    else:
        return "I'm sorry, I don't know the answer to that question.", None

def main():
    st.title("Placement Documents Chatbot")

    # Load data from CSV
    data = load_data()

    # User input
    user_question = st.selectbox("Ask a question:", data['Question'].unique())

    if st.button("Get Answer"):
        # Get the answer and picture path
        answer, picture_path = get_answer(user_question, data)

        # Display the answer
        st.markdown(f"**Answer:** {answer}")

        # Display the picture if available
        if picture_path:
            st.image(picture_path, caption='Answer Image', use_column_width=True)
        else:
            st.warning("No picture available for this answer.")

if __name__ == "__main__":
    main()
