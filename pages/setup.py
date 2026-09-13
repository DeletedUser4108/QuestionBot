import streamlit as sl
sl.title(":shimmer[:rainbow[Personal Question Bot]]",icon=":material/quiz:", text_alignment="center", help="This bot generates questions in JEE topics", anchor=False)
sl.subheader(":gray-background[Your Personal :red[Book-Based] :blue[Question Generator] :sunglasses:]", text_alignment="center",divider=True, anchor=False)

sl.markdown('''

📚 Generate questions from :color[your study material]{foreground='#ff5050'} 

🎯 Choose your :orange[difficulty]  

📊 Track your :violet[performance]''', text_alignment="center" )


p,c,m= "Physics", "Chemistry", "Mathematics"

sub = sl.pills("Select your subject", [p, c, m], selection_mode="single", help="Choose the subject for which you want to generate questions")#index=None,placeholder="Select the Subject", help="Choose the subject for which you want to generate questions"
##if sub:
##sl.info(f"📚 Subject selected: **{sub}**")
diff = sl.pills("Select the difficulty level", ["NCERT", "JEE MAINS", ":shimmer[JEE ADVANCED]"], selection_mode="single", help="Choose the difficulty level for the questions")
num_ques = sl.slider("Select the number of question required",1,25,6)
book=""

user_book_choice = sl.pills("Do you want to upload your study material?", ["Yes", "No"], selection_mode="single", help="Choose 'Yes' to upload a PDF file containing your study material or 'No' to proceed without uploading")
if user_book_choice == "Yes":
    book=None
    upload = sl.file_uploader("Upload your study material (PDF)", type=["pdf"], max_upload_size=50, accept_multiple_files=False, help="Upload a PDF file containing your study material to generate questions from it")
elif user_book_choice == "No":
    upload= None
    if diff == "NCERT":
        sl.info("For NCERT level questions, the questions will be generated from the NCERT textbooks.")
    if  diff == ":shimmer[JEE ADVANCED]" or diff =="JEE MAINS":
        
        if sub == "Physics":
            #book = sl.selectbox("Please choose the book out of the options:",["HC Verma", "IE Irodov", "Resnick Halliday"], help="Choose the book from which you want to generate questions")
            book = sl.pills("Please choose the book out of the options:",["HC Verma", "IE Irodov", "Resnick Halliday"], selection_mode="multi", help="Choose the book from which you want to generate questions")
        if sub == "Chemistry":
            book = sl.pills("Please choose the book out of the options:",["M.S Chouhan", "N. Avasthi", "V.K. Jaiswal"], selection_mode="single", help="Choose the book from which you want to generate questions")
            #book = sl.selectbox("Please choose the book out of the options:",["M.S Chouhan", "N. Avasthi", "V.K. Jaiswal"], help="Choose the book from which you want to generate questions")
        if sub == "Mathematics":
            #book = sl.selectbox("Please choose the book out of the options:",["Black Book", "Cengage", "Tata McGraw-Hill"], help="Choose the book from which you want to generate questions")
            book = sl.pills("Please choose the book out of the options:",["Black Book", "Cengage", "Tata McGraw-Hill"], selection_mode="multi", help="Choose the book from which you want to generate questions")
        
topic =sl.text_input("Enter the topic you want to generate questions from", placeholder="Example: Coordinate Geometry", help="Type the topic name here")
        

generate = sl.button("Generate Questions", type="primary", use_container_width=True, help="Click to generate questions based on your selections")

if generate:

    if sub is None:
        sl.warning("⚠️ Please select a subajaxr.")
    
    elif topic.strip() == "":
        sl.warning("⚠️ Please enter a topic.")
    
    elif diff is None:
        sl.warning("⚠️ Please select a difficulty level.")

    else:
        sl.success("✅ All inputs are valid!")
        #sl.write("### Your Question Settings")
        #sl.write("**Subject:**", sub)
        #sl.write("**Topic:**", topic)
        #sl.write("**Difficulty:**", diff)
        #sl.write("**Number of Questions:**", num_ques)
        sl.session_state.sub = sub
        sl.session_state.topic = topic
        sl.session_state.diff = diff
        sl.session_state.num_ques = num_ques
        sl.session_state.book = book
        sl.session_state.upload = upload
        sl.switch_page("pages/practice.py")

