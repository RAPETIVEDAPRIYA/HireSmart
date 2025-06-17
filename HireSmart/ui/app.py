import streamlit as st
from HireSmart.HireSmart.Agents.interview_agent import MockInterviewAgent

agent = MockInterviewAgent()

st.title("HireSmart Mock Interviewer")

resume = st.file_uploader("Upload your resume (PDF)")
jd_text = st.text_area("Paste the job description")

if st.button("Start Mock Interview"):
    if resume and jd_text:
        resume_text = agent.run({"file_path": resume})["resume_text"]
        result = agent.run({"resume_text": resume_text, "jd_text": jd_text})
        st.session_state["question"] = result["question"]
        st.write("Question:", result["question"])
        answer = st.text_area("Your Answer")
        if st.button("Submit Answer"):
            feedback = agent.run({
                "resume_text": resume_text,
                "jd_text": jd_text,
                "question": st.session_state["question"],
                "user_answer": answer
            })
            st.write("Feedback:", feedback["feedback"])
