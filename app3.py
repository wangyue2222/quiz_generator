import streamlit as st
import llm, json

def generate_questions(topic, num_questions):
    system_prompt = f"You are proficient quiz generator."
    # read user_prompt from prompt.txt
    with open("prompt.txt", "r") as f:
        user_prompt = f.read()
    ## replace the topic in the user_prompt with the topic from the text_input
    user_prompt = user_prompt.replace("{topic}", topic)
    user_prompt = user_prompt.replace("{num_questions}", str(num_questions))
    # display the user prompt
    print("User prompt:")
    print(user_prompt)
    results = llm.answer(system_prompt, user_prompt)
    return results
with st.sidebar:
    topic = st.text_input("Enter the topic to generate questions:")
    num_questions = st.selectbox("Select number of questions to generate:", [1, 2, 3])
    button = st.button("Generate Questions")
if button: # if the button is clicked
    results = generate_questions(topic, num_questions)
    print("LLM response:")
    print(results)
    st.write("LLM response:")
    st.json(results)
 # show questions
    st.markdown ("## Generated Questions")
    results_dict = json.loads(results) # convert results to python dictionary
    for question in results_dict["questions"]:
        question_text = question["question_text"]
        answer = question["answer"]
        st.write("*Question:*", question_text)
        with st.expander("Show Answer"): 
            st.info(answer) 