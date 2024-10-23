import streamlit as st
import sqlite3
import bcrypt

# Database connection
conn = sqlite3.connect('user.db')
cur = conn.cursor()

# Check if table exists, create if not
cur.execute(
    '''CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, email TEXT, mobilenumber TEXT, password TEXT)''')
conn.commit()


def registration_page():
    """ Creates registration form and handles user data """
    st.title("Registration")
    st.markdown(f"<style>body {{background-color: black;}}</style>", unsafe_allow_html=True)  # Set background color to black

    username = st.text_input("Username")
    email = st.text_input("Email")
    mobilenumber = st.text_input("Mobile Number")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    # Basic validation
    if any(not field for field in [username, email, mobilenumber, password, confirm_password]):
        st.error("Please fill all fields!")
        return

    if password != confirm_password:
        st.error("Passwords do not match!")
        return

    # Hash password (secure hashing with bcrypt)
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Insert user data and check rowcount for successful insertion
    cur.execute("INSERT INTO users VALUES (?, ?, ?, ?)", (username, email, mobilenumber, hashed_password))
    if cur.rowcount > 0:
        conn.commit()
        st.success("Registration successful!")
    else:
        st.error("Registration failed!")




def login_page():
    """ Creates login form and handles authentication """
    st.title("Login")
    st.markdown(f"<style>body {{background-color: black;}}</style>", unsafe_allow_html=True)  # Set background color to black

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Validate user and password (use secure hashing comparison)
    cur.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cur.fetchone()
    if user and bcrypt.checkpw(password.encode('utf-8'), user[3]):
        st.success("Login successful!")
        # Call another Streamlit app here
        st.write("Redirecting to another app...")

        import subprocess
        subprocess.Popen(['streamlit', 'run', 'main.py'])  # Assuming 'main.py' is your other app
        st.stop()  # Stop rendering current app


    else:
        st.error("Invalid username or password.")




# Hide the sidebar (vertical navbar)
st.sidebar.visible = False
st.title("Recommendation System")
page = st.selectbox("Select Page", ["Registration", "Login"])  # Moved to main area for better visibility

if page == "Registration":
    registration_page()
elif page == "Login":
    login_page()

conn.close()



