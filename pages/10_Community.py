import streamlit as st

st.markdown("# Comment Section 🧑‍💻")
st.sidebar.markdown("Community")




# Initialize session state variables
if "comments" not in st.session_state:
    st.session_state.comments = []
if "user_info" not in st.session_state:
    st.session_state.user_info = {}
if "verified" not in st.session_state:
    st.session_state.verified = False

# Function to handle email verification
def verify_email(email, username):
    if email not in st.session_state.user_info:
        st.session_state.user_info[email] = username
        st.session_state.verified = True
        st.success("Email verified successfully! You can now comment.")
        return True
    elif st.session_state.user_info[email] == username:
        st.session_state.verified = True
        st.info("Welcome back!")
        return True
    else:
        st.error("This email is already associated with a different username.")
        return False

# User input for email verification
with st.sidebar:
    st.header("Verify Your Email")
    email = st.text_input("Email Address")
    username = st.text_input("Username")
    if st.button("Verify"):
        if email and username:
            verify_email(email, username)
        else:
            st.error("Please enter both email and username.")

# Comment section
if st.session_state.verified:
    st.header("Comment Section")
    comment = st.text_input("Write a comment:")
    if st.button("Submit"):
        if comment:
            st.session_state.comments.append({"username": username, "comment": comment})
            st.success(f"Thank you for your comment, {username}!")
        else:
            st.error("Comment cannot be empty.")

    # Display all comments
    st.subheader("Comments")
    for entry in st.session_state.comments:
        st.write(f"**{entry['username']}**: {entry['comment']}")
else:
    st.warning("Please verify your email to participate in the comments.")
