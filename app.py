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

def load_datalink():
    # Load the CSV file
    df = pd.read_csv("datali.csv")
    return df

def link():
    st.title("Report Link")

    # Load data from CSV
    data = load_datalink()

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



# Department selection
department = st.selectbox("Select Department :", ("M&E Department", "Finance Department", "HR Depertment"))

# If ME Department is selected, show the options Placement, Enrollment, and M&E SPOC
if department == "M&E Department":
    selection = st.selectbox("Select Option :", ("Placement", "Enrollment", "M&E SPOC", "Report Link"))
    if selection == "Placement":
        Placement()
    elif selection == "Enrollment":
        Enrollment()
    elif selection == "M&E SPOC":
        spoc()
    elif selection == "Report Link":
        link()
    
elif department == "Finance Department":
    st.image("upcoming.png")

elif department == "HR Depertment":
    st.image("upcoming.png")

# Adding Google Form link
google_form_link = "[For Other Questions](https://forms.gle/zsf1S146zbaaHuiWA)"
st.markdown(google_form_link)
