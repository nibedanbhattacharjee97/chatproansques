import streamlit as st
import pandas as pd

st.set_page_config("Anudip Chatbot", page_icon=":book")
st.image("AnudipLogoWithGit_Update_3.png")
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

def Placement():
    st.title("Placement")

    # Load data from CSV
    data = load_data()

    # User input
    user_question = st.selectbox("TYPE / SELECT YOUR QUESTION :", data['Question'].unique())

    if st.button("Get Answer"):
        # Get the answer and picture path
        answer, picture_path = get_answer(user_question, data)

        # Display the answer
        st.markdown(f"**Answer:** {answer}")

        # Display the picture if available
        if picture_path:
            st.image(picture_path, caption='', use_column_width=True)
        else:
            st.warning("No picture available for this answer.")

def load_dataen():
    # Load the CSV file
    df = pd.read_csv("dataen.csv")
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


def Enrollment():
    st.title("Enrollment")

    # Load data from CSV
    data = load_dataen()

    # User input
    user_question = st.selectbox("TYPE / SELECT YOUR QUESTION :", data['Question'].unique())

    if st.button("Get Answer"):
        # Get the answer and picture path
        answer, picture_path = get_answer(user_question, data)

        # Display the answer
        st.markdown(f"**Answer:** {answer}")

        # Display the picture if available
        if picture_path:
            st.image(picture_path, caption='', use_column_width=True)
        else:
            st.warning("No picture available for this answer.")


def load_datasp():
    # Load the CSV file
    df = pd.read_csv("datasp.csv")
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


def spoc():
    st.title("M&E SPOC")

    # Load data from CSV
    data = load_datasp()

    # User input
    user_question = st.selectbox("TYPE / SELECT YOUR QUESTION :", data['Question'].unique())

    if st.button("Get Answer"):
        # Get the answer and picture path
        answer, picture_path = get_answer(user_question, data)

        # Display the answer
        st.markdown(f"**Answer:** {answer}")

        # Display the picture if available
        if picture_path:
            st.image(picture_path, caption='', use_column_width=True)
        else:
            st.warning("No picture available for this answer.")


#st.text('Select Option')
selection = st.selectbox("Select Option :", ("Placement", "Enrollment","M&E SPOC"))
if selection == "Placement":
    Placement()
elif selection == "Enrollment":
    Enrollment()
elif selection == "M&E SPOC":
    spoc()
