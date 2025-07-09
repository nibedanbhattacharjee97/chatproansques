import streamlit as st
import pandas as pd

st.set_page_config("Anudip Chatbot", page_icon=":book")
st.image("AnudipLogoWithGit_Update_3.png")

# Adding BookslotDetails Form link
SPOC_SLOT_BOOK_LINK = "[CLICK HERE TO BOOK SPOC SLOT](https://bookslotapp.streamlit.app/)"
st.markdown(SPOC_SLOT_BOOK_LINK, unsafe_allow_html=True)

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

def load_datacerti():
    # Load the CSV file
    df = pd.read_csv("datacerti.csv")
    return df

def certificate():
    st.title("Certificate")
    # Load data from CSV
    data = load_datacerti()
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

def load_datafi():
    # Load the CSV file
    df = pd.read_csv("datafi.csv")
    return df

def FinanceDepartment():
    st.title("Finance Department")
    # Load data from CSV
    data = load_datafi()
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
    st.title("Reports")
    # Load data from CSV
    data = load_datalink()
    # User input
    user_question = st.selectbox("TYPE / SELECT YOUR QUESTION :", data['Question'].unique())

    if st.button("Get Answer"):
        # Find the corresponding link for the given question
        link_row = data[data['Question'] == user_question]
        if not link_row.empty:
            report_link = link_row.iloc[0]['Link']
            # Display the link as clickable
            st.markdown(f"[View Report]({report_link})", unsafe_allow_html=True)
        else:
            st.warning("No link available for this question.")

# Department selection
department = st.selectbox("Select Department :", ("M&E Department",))

# If ME Department is selected, show the options Placement, Enrollment, M&E SPOC, Certificate, and Reports
if department == "M&E Department":
    selection = st.selectbox("Select Option :", ("Placement Parameters", "Enrollment Parameters", "M&E SPOC Details", "Certificate Process", "Reports"))
    if selection == "Placement Parameters":
        Placement()
    elif selection == "Enrollment Parameters":
        Enrollment()
    elif selection == "M&E SPOC Details":
        spoc()
    elif selection == "Certificate Process":
        certificate()
    elif selection == "Reports":
        link()
    

# Adding Google Form links
google_form_link_retention = "[Retention Data](https://docs.google.com/spreadsheets/d/12vmZRZMWVuaqysaSRS0qVPAun53W6EsSztx9uUSiWzw/edit?usp=sharing)"
st.markdown(google_form_link_retention)

google_form_link_query = "[For Other Query Please Fill This Form](https://forms.gle/zsf1S146zbaaHuiWA)"
st.markdown(google_form_link_query)
