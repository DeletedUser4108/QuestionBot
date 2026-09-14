import streamlit as sl
sl.title(":shimmer[:rainbow[Personal Question Bot]]",icon=":material/quiz:", text_alignment="center", help="This bot generates questions in JEE topics", anchor=False)
sl.subheader(":gray-background[Your Personal :red[Book-Based] :blue[Question Generator] :sunglasses:]", text_alignment="center",divider=True, anchor=False)

sl.markdown('''

📚 Generate questions from :color[your study material]{foreground='#ff5050'}        
🎯 Choose your :orange[difficulty]    
📊 Track your :violet[performance]''', text_alignment="center" )

with sl.container(border=True,):
    col1,col2 = sl.columns(2)

    p,c,m= "Physics", "Chemistry", "Mathematics"
    with col1:
        sub = sl.pills("Select your subject", [p, c, m], selection_mode="single", help="Choose the subject for which you want to generate questions")#index=None,placeholder="Select the Subject", help="Choose the subject for which you want to generate questions"  
    ncert,jm,ja="NCERT", "JEE MAINS", "JEE ADVANCED"
    with col2:
        diff = sl.pills("Select the difficulty level", [ncert, jm, ja], selection_mode="single", help="Choose the difficulty level for the questions")
    num_ques = sl.slider("Select the number of question required",1,25,6)
    book=""
    user_book_choice = sl.pills("Do you want to upload your study material?", ["Yes", "No"], selection_mode="single", help="Choose 'Yes' to upload a PDF file containing your study material or 'No' to proceed without uploading")

    if user_book_choice == "Yes":
        book=None
        upload = sl.file_uploader("Upload your study material (PDF)", type=["pdf"], max_upload_size=50, accept_multiple_files=False, help="Upload a PDF file containing your study material to generate questions from it")
    elif user_book_choice == "No":
        upload= None
        if diff == ncert:
            sl.info("For NCERT level questions, the questions will be generated from the NCERT textbooks.")
            if sub == p:
                book = "NCERT_Phy_File"
            if sub == c:
                book = "NCERT_Chem_File"
            if sub == m:
                book = "NCERT_MATH_File"
        if  diff == ja or diff == jm:
        
            if sub == p:
            #book = sl.selectbox("Please choose the book out of the options:",["HC Verma", "IE Irodov", "Resnick Halliday"], help="Choose the book from which you want to generate questions")
                book = sl.pills("Please choose the book out of the options:",["HC Verma", "IE Irodov", "Resnick Halliday"], selection_mode="multi", help="Choose the book from which you want to generate questions")
            if sub == c:
                book = sl.pills("Please choose the book out of the options:",["M.S Chouhan", "N. Avasthi", "V.K. Jaiswal"], selection_mode="single", help="Choose the book from which you want to generate questions")
            #book = sl.selectbox("Please choose the book out of the options:",["M.S Chouhan", "N. Avasthi", "V.K. Jaiswal"], help="Choose the book from which you want to generate questions")
            if sub == m:
            #book = sl.selectbox("Please choose the book out of the options:",["Black Book", "Cengage", "Tata McGraw-Hill"], help="Choose the book from which you want to generate questions")
                book = sl.pills("Please choose the book out of the options:",["Black Book", "Cengage", "Tata McGraw-Hill"], selection_mode="multi", help="Choose the book from which you want to generate questions")
        
    topic =sl.text_input("Enter the topic you want to generate questions from", placeholder="Example: Coordinate Geometry", help="Type the topic name here")
        

    generate = sl.button("Generate Questions", type="primary", use_container_width=True, help="Click to generate questions based on your selections")

    if generate:

        if sub is None:
            sl.warning("⚠️ Please select a subject.")
    
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
            sl.session_state.subject = sub
            sl.session_state.topic = topic
            sl.session_state.difficulty = diff
            sl.session_state.number_questions = num_ques
            sl.session_state.book = book
            sl.session_state.upload = upload
            sl.switch_page("pages/practice.py")

