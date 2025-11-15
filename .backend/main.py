import google.generativeai as genai

genai.configure(api_key="AIzaSyB8YWnoZe-Ry3_eFp8yYlvRCgd6_aY1YoA")

model = genai.GenerativeModel("models/gemini-2.5-flash")

response = model.generate_content("Write a short paragraph about AI.")
print(response.text)


