import requests, json, os, toml
import streamlit as st
 # Load API key from credentials.txt
file_path = 'credentials'
if os.path.exists(file_path):
    with open(file_path, 'r') as f:
        secrets = toml.load(f)
else:
    secrets =st.secrets
OPENROUTER_API_KEY =secrets['OPENROUTER']['OPENROUTER_API_KEY']
def answer(system_prompt, user_prompt): 
    msg= [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
 # models: mistralai/mistral-7b-instruct:free, openai/gpt-4o-mini-2024-07-18
 # json.dumps() is used to convert the dictionary to a string before sending the request
    response =requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={"Authorization": f"Bearer {OPENROUTER_API_KEY}"},
        data=json.dumps({ 
            "messages": msg,
            "model": "openai/gpt-4o-mini-2024-07-18"
        })
    )
 # extract the bot's response from the JSON
    if 'choices' in response.json():
        resp = response.json()['choices'][0]['message']['content']
    else:
        print("Key 'choices' not found in response")
    # 处理错误情况，例如设置默认值或抛出异常