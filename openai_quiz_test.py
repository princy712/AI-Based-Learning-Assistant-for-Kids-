import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyDjTWd67f5rnEH4ddyVpIaDt__FzqFUjYo")

# Use the latest model
model = genai.GenerativeModel("gemini-1.5-pro-latest")  # Updated model

def generate_quiz(topic):
    prompt = f"Generate 3 multiple-choice quiz questions for kids about {topic}."
    response = model.generate_content(prompt)
    return response.text  # Extracting text response

topic = input("Enter a topic for the quiz: ")
quiz_questions = generate_quiz(topic)

print("\n🎯 Generated Quiz:\n", quiz_questions)


