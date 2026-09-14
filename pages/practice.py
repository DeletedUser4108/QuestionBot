import streamlit as sl
import time
#if sl.button("Go back to Setup Page", icon=":material/arrow_back:", type="tertiary", use_container_width=False, help="Click to go back to the Setup page to change your selections"):
#    sl.switch_page("pages/setup.py")
sl.toast("Welcome to the Practice Page! Here you can practice questions generated from your selected topics and difficulty levels.", icon=":material/quiz:", duration="long")
sl.title("Practice Page", icon=":material/target:", text_alignment="center", help="This page allows you to practice questions generated from your selected topics and difficulty levels.", anchor=False)

sub = sl.session_state.get("subject", "Please select a subject in the Setup page.")
topic = sl.session_state.get("topic", "Please enter a topic in the Setup page.")
diff = sl.session_state.get("difficulty", "Please select a difficulty level in the Setup page.")
num_ques = sl.session_state.get("number_questions", "Please select the number of questions in the Setup page.")
book = sl.session_state.get("book", "Please select a book in the Setup page.")
upload = sl.session_state.get("upload", "Please upload a file in the Setup page.")

#sl.info(f":green[**Subject:**] {sub}")
#sl.info(f":red[**Topic:**] {topic}")
#sl.info(f":yellow[**Difficulty:**] {diff}")
#sl.info(f":orange[**Number of Questions:**] {num_ques}")
#if upload==None:
#    sl.info(f":yellow[**Book:**] {book}")
#else:
#    sl.info(f":gray[**Uploaded File:**] {upload}")
#
#time.sleep(0.1)
#sl.empty()

plh=sl.empty()
plh.info(f":green[**Subject:**] _{sub}_")
time.sleep(1.25)
plh.info(f":red[**Topic:**] _{topic}_")
time.sleep(1.25)
plh.info(f":yellow[**Difficulty:**] _{diff}_")
time.sleep(1.25)
plh.info(f":orange[**Number of Questions:**] _{num_ques}_")
time.sleep(1.25)
if upload==None:
    plh.info(f":yellow[**Book:**] _{book}_")
else:
    plh.info(f":gray[**Uploaded File:**] _{upload}_")
time.sleep(1.25)
plh.empty() 


qno =1
while qno <= num_ques:
    sl.markdown(f"### Question {qno} of {num_ques}")
    sl.markdown("This is a Sample Question?")
    opts = ["Option A", "Option B", "Option C", "Option D"]
    answer = sl.radio("Select the correct answer:", opts, horizontal=True)
    qno += 1