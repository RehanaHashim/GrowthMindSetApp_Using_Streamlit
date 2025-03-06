#streamlit

import streamlit as st

st.set_page_config(page_title= "growth mindset project", page_icon="★")
st.title("Growth Mindset Challenge app with Streamlit")
st.header("🚀 Welcome to your Growth Gourney!")
st.write ("Embrace chalenge, learn from mistake , and unlock your full potential. This AI-powered app helps you build a growth mindset with reflection , challenges and achievments! 🌟")

#quote section 
st.header("💡 Today's Growth Mindset Quotes")
st.write("Success is not final, failure is not fatal: it is the courage to continue that counts. -Wisnton Churchill")

st.header("🔧 What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing: ")

#condition 
if user_input:
    st.success(f"💪 You're facing: {user_input}. Keep pushing forward towords your goal! 🚀")
else:
    st.warning("Tell us about your challenge to get started!")

#reflexing
st.header("Reflect On Your Learning ")
reflection = st.text_area("Write your reflection here:")

if reflection:
    st.success( f"👌Great Insight: Your reflection :{reflection}")
else:
    st.info("Reflection on past experience help you grow! Share your difficulties")

# Achievments  
st.header("🎉Celebrate your Wins!")
acheivment = st.text_input("Share something you've recently accomplished:")     

if acheivment:
    st.success( f"Amazing! Your aceivment: {acheivment}")
else: 
    st.info("Big or small, every acheivemnt count! Share one now 😍") 

#footer
st.write("- - -") 
st.write("🚀 Keep believing in yourself. Growth is a journey, not a destination! ✨ ") 
st.write("***Created by Rehana Hashim***") 
