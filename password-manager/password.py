import streamlit as st
import re

st.set_page_config(page_title="Password Checker" , page_icon=":lock:", layout="wide")
 
st.title("🔒Password Checker")
st.markdown("""
## 👋 Welcome to the password strenghth checker!
Enter a password to check its strength.
     We will provide you with expert tips to help you create an **unbreakable password🔒** """)


password = st.text_input("Enter your password", type="password")

feedback = []

score = 0

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("⚔ Password must be at least 8 characters long.")

    if re.search(r'[A-Z]', password) and re.search (r'[a-z]' , password):
        score += 1  
    else:
        feedback.append("⚔ Password must contain at least one uppercase letter.")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("⚔ Password must contain at least one number.")

    if re.search(r'[!@#$%&*]', password):
        score += 1    
    else:
        feedback.append("⚔ Password must contain at least one special character (!@#$%&*).") 
    if score ==4:
            feedback.append("✅ Your password is strong!🔒")
    elif score == 3:
            feedback.append("⚠ Your password is medium. Consider adding more complexity.")
    else:
            feedback.append("⚠ Your password is weak. Consider adding more complexity.")
               
    if feedback:
        st.markdown("### Feedback")
        for tip in feedback:
            st.write(tip)   
else:
         st.info("Please enter a password to check its strength.")              

   






