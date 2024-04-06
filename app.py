# from dotenv import load_dotenv
import streamlit as st
from streamlit_option_menu import option_menu
# import os
import google.generativeai as genai

# load_dotenv()
# api = os.getenv("GOOGLE_API_KEY")
api = st.secrets["GOOGLE_API_KEY"]

genai.configure(api_key=api)

model = genai.GenerativeModel('gemini-pro')

with st.sidebar:
    selected = option_menu(
        menu_title = "Main Menu",
        options = ["About Sarthak", "ATS Resume Matcher", "Application Question Help", "Cover Letter Help", "Referral Message Help", "Interview Prep Assistant"],
        icons = ["person-circle", "file-earmark-person", "question-circle", "file-earmark-text-fill", "chat-dots", "file-earmark-text-fill"],
        menu_icon = "cast"
    )

if selected == "About Sarthak":

    st.title("Career Crafter")

    st.header("Discover four essential sections designed to supercharge your job application process:")

    st.divider()

    st.header("📑ATS Resume Matcher")
    st.subheader("Tailor your resume to beat Applicant Tracking Systems and get noticed.")

    st.divider()
    
    st.header("❓Application Question Help")
    st.subheader("Get expert tips on impressing recruiters with your answers.")
    
    st.divider()
    
    st.header("📝Cover Letter Help")
    st.subheader("Craft compelling cover letters to set yourself apart.")
    
    st.divider()

    st.header("💌Referral Message Help")
    st.subheader("Land interviews with effective networking messages.")

    st.divider()

    st.header("🎙️Interview Prep Assistant")
    st.subheader("Get tailored interview questions and suggested answers to ace your next interview with confidence.")

    st.divider()

    st.subheader("Navigate effortlessly through each section using the sidebar menu, and let our app empower you on your journey to career success! 🌟")

    st.divider()

    st.subheader("About Sarthak")

    st.image('me.jpg', caption='Sarthak Mishra', width=200)
    
    st.write("MS CS graduate from University at Buffalo | Front End Development, AI, Data Analysis, UI/UX")

    linkedin_url = "https://www.linkedin.com/in/sarthakmishraa/"
    github_url = "https://github.com/sarthakmishraa"
    portfolio_url = "http://sarthakmishra.lovestoblog.com/?i=2"

    st.write("[LinkedIn](%s)" % linkedin_url)
    st.write("[GitHub](%s)" % github_url)
    st.write("[Digital Portfolio](%s)" % portfolio_url)

    st.divider()

if selected == "ATS Resume Matcher":

    st.title("ATS Resume Matcher using Gemini")

    st.subheader("Enter your resume:")

    resume = st.text_area(label=" ", value="", height=400, key=1)

    st.subheader("Enter job description:")
    job_desc = st.text_area(label=" ", value="", height=400, key=2)

    prompt = f'''
    I know you are an LLM but you have to act like a skilled or experienced ATS(Application Tracking System)
    with a deep understanding of tech field,software engineering and data analyst. Your task is to evaluate the resume based on the given job description.
    You must consider the job market is very competitive and you should provide 
    best assistance for improving the resumes. Assign the percentage Matching based 
    on Jd and the missing keywords with high accuracy
    resume:{resume}
    description:{job_desc}

    I want the response in the below format, put JD match, missing keywords and profile summary in an new line
    Job Description Match: %
    MissingKeywords: []
    Profile Summary: ""
    '''

    if st.button(label="Go"):
        result = model.generate_content(prompt)
        st.write(result.text)
    
    st.divider()
    
if selected == "Application Question Help":

    st.title("Application question help using Gemini")

    st.subheader("Enter your application question:")

    app_ques = st.text_area(label=" ", value="", height=100, key=3)

    st.subheader("Enter your resume:")

    resume = st.text_area(label=" ", value="", height=400, key=1)

    st.subheader("Enter job description:")

    job_desc = st.text_area(label=" ", value="", height=400, key=2)

    prompt = f'''
    I know you are an LLM but you have to act like a skilled or experienced professional
    with a deep understanding of tech field,software engineering and data analyst.
    Your task is to answer a question for the job application I am filling based on the given job description.
    You must consider the job market is very competitive and you should provide 
    best assistance for improving the resumes.
    
    Application question: {app_ques}
    resume:{resume}
    job description:{job_desc}

    I want the response in a paragraph.
    '''

    if st.button(label="Go"):
        result = model.generate_content(prompt)
        st.write(result.text)
    
    st.divider()

if selected == "Cover Letter Help":

    st.title("Cover letter generator using Gemini")

    st.subheader("Enter your resume:")

    resume = st.text_area(label=" ", value="", height=400, key=1)

    st.subheader("Enter job description:")

    job_desc = st.text_area(label=" ", value="", height=400, key=2)

    prompt = f'''
    Write a cover letter for my resume and job description given below.

    resume: {resume}
    job description: {job_desc}

    I want the response in three paragraphs.
    '''

    if st.button(label="Go"):
        result = model.generate_content(prompt)
        st.write(result.text)
    
    st.divider()

if selected == "Referral Message Help":

    st.title("Referral message generator using Gemini")

    st.subheader("Enter the role you're applying for:")

    job_role = st.text_area(label=" ", value="", height=100, key=4)

    st.subheader("Enter your resume:")

    resume = st.text_area(label=" ", value="", height=400, key=1)

    st.subheader("Enter job description:")

    job_desc = st.text_area(label=" ", value="", height=400, key=2)

    prompt = f'''
    Write a very short message to ask for a referral for the role, my resume and job description given below.

    Job role: {job_role}
    resume: {resume}
    job description: {job_desc}

    I want the response in three paragraphs.
    '''

    if st.button(label="Go"):
        result = model.generate_content(prompt)
        st.write(result.text)
    
    st.divider()

if selected == "Interview Prep Assistant":

    st.title("Interview Prep Assistant using Gemini")

    st.subheader("Enter your resume:")

    resume = st.text_area(label=" ", value="", height=400, key=1)

    st.subheader("Enter job description:")

    job_desc = st.text_area(label=" ", value="", height=400, key=2)

    prompt = f'''
    Write 15 interview questions and their answers, my resume and job description given below.

    resume: {resume}
    job description: {job_desc}
    '''

    if st.button(label="Go"):
        result = model.generate_content(prompt)
        st.write(result.text)
    
    st.divider()