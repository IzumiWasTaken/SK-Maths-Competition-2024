import openai
from random import randrange
from time import sleep
from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

user_input = None
topic = None
current_question = None
conversation = []

def generate_prompt(topic, difficulty):
    x = randrange(0, 2)
    if x == 0:
        return f"Do not hallucinate! Create an algebraic equation about {topic} for {difficulty.lower()} grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DON'T USE SENTENCES. DO NOT SAY THAT YOU UNDERSTOOD THE PROMPT, AND KEEP THE FEEDBACK SIMPLE AND STRAIGHT TO THE POINT. SEPARATE EACH NEW CHOICE BY PUTTING '\n' AT THE PREVIOUS CHOICE."
    else:
        return f"Do not hallucinate! Create a word problem about {topic} for {difficulty.lower()} grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DON'T USE SENTENCES. DO NOT SAY THAT YOU UNDERSTOOD THE PROMPT, AND KEEP THE FEEDBACK SIMPLE AND STRAIGHT TO THE POINT. SEPARATE EACH NEW CHOICE BY PUTTING '\n' AT THE PREVIOUS CHOICE."

def trig_difficulty_easy():
    topic = "Trig"
    difficulty = "Easy"
    return generate_prompt(topic, difficulty)

def trig_difficulty_medium():
    topic = "Trig"
    difficulty = "Medium"
    return generate_prompt(topic, difficulty)

def trig_difficulty_hard():
    topic = "Trig"
    difficulty = "Hard"
    return generate_prompt(topic, difficulty)

def trig_difficulty_difficult():
    topic = "Trig"
    difficulty = "Difficult"
    return generate_prompt(topic, difficulty)

def para_difficulty_easy():
    topic = "Para"
    difficulty = "Easy"
    return generate_prompt(topic, difficulty)

def para_difficulty_medium():
    topic = "Para"
    difficulty = "Medium"
    return generate_prompt(topic, difficulty)

def para_difficulty_hard():
    topic = "Para"
    difficulty = "Hard"
    return generate_prompt(topic, difficulty)

def para_difficulty_difficult():
    topic = "Para"
    difficulty = "Difficult"
    return generate_prompt(topic, difficulty)

def numbers_difficulty_easy():
    topic = "Numbers"
    difficulty = "Easy"
    return generate_prompt(topic, difficulty)

def numbers_difficulty_medium():
    topic = "Numbers"
    difficulty = "Medium"
    return generate_prompt(topic, difficulty)

def numbers_difficulty_hard():
    topic = "Numbers"
    difficulty = "Hard"
    return generate_prompt(topic, difficulty)

def numbers_difficulty_difficult():
    topic = "Numbers"
    difficulty = "Difficult"
    return generate_prompt(topic, difficulty)

def propor_difficulty_easy():
    topic = "Prop"
    difficulty = "Easy"
    return generate_prompt(topic, difficulty)

def propor_difficulty_medium():
    topic = "Prop"
    difficulty = "Medium"
    return generate_prompt(topic, difficulty)

def propor_difficulty_hard():
    topic = "Prop"
    difficulty = "Hard"
    return generate_prompt(topic, difficulty)

def propor_difficulty_difficult():
    topic = "Prop"
    difficulty = "Difficult"
    return generate_prompt(topic, difficulty)

def matric_difficulty_easy():
    topic = "Matrices"
    difficulty = "Easy"
    return generate_prompt(topic, difficulty)

def matric_difficulty_medium():
    topic = "Matrices"
    difficulty = "Medium"
    return generate_prompt(topic, difficulty)

def matric_difficulty_hard():
    topic = "Matrices"
    difficulty = "Hard"
    return generate_prompt(topic, difficulty)

def matric_difficulty_difficult():
    topic = "Matrices"
    difficulty = "Difficult"
    return generate_prompt(topic, difficulty)

def inequalities_difficulty_easy():
    topic = "Inequalities"
    difficulty = "Easy"
    return generate_prompt(topic, difficulty)

def inequalities_difficulty_medium():
    topic = "Inequalities"
    difficulty = "Medium"
    return generate_prompt(topic, difficulty)

def inequalities_difficulty_hard():
    topic = "Inequalities"
    difficulty = "Hard"
    return generate_prompt(topic, difficulty)

def inequalities_difficulty_difficult():
    topic = "Inequalities"
    difficulty = "Difficult"
    return generate_prompt(topic, difficulty)

def probabilities_difficulty_easy():
    topic = "Probabilities"
    difficulty = "Easy"
    return generate_prompt(topic, difficulty)

def probabilities_difficulty_medium():
    topic = "Probabilities"
    difficulty = "Medium"
    return generate_prompt(topic, difficulty)

def probabilities_difficulty_hard():
    topic = "Probabilities"
    difficulty = "Hard"
    return generate_prompt(topic, difficulty)

def probabilities_difficulty_difficult():
    topic = "Probabilities"
    difficulty = "Difficult"
    return generate_prompt(topic, difficulty)

def Percentage_difficulty_easy():
    topic = "Percentage"
    difficulty = "Easy"
    return generate_prompt(topic, difficulty)

def Percentage_difficulty_medium():
    topic = "Percentage"
    difficulty = "Medium"
    return generate_prompt(topic, difficulty)

def Percentage_difficulty_hard():
    topic = "Percentage"
    difficulty = "Hard"
    return generate_prompt(topic, difficulty)

def Percentage_difficulty_difficult():
    topic = "Percentage"
    difficulty = "Difficult"
    return generate_prompt(topic, difficulty)

def Sequences_difficulty_easy():
    topic = "Number Sequences"
    difficulty = "Easy"
    return generate_prompt(topic, difficulty)

def Sequences_difficulty_medium():
    topic = "Number Sequences"
    difficulty = "Medium"
    return generate_prompt(topic, difficulty)

def Sequences_difficulty_hard():
    topic = "Number Sequences"
    difficulty = "Hard"
    return generate_prompt(topic, difficulty)

def Sequences_difficulty_difficult():
    topic = "Number Sequences"
    difficulty = "Difficult"
    return generate_prompt(topic, difficulty)

def ratio_difficulty_easy():
    topic = "Ratio"
    difficulty = "Easy"
    return generate_prompt(topic, difficulty)

def ratio_difficulty_medium():
    topic = "Ratio"
    difficulty = "Medium"
    return generate_prompt(topic, difficulty)

def ratio_difficulty_hard():
    topic = "Ratio"
    difficulty = "Hard"
    return generate_prompt(topic, difficulty)

def ratio_difficulty_difficult():
    topic = "Ratio"
    difficulty = "Difficult"
    return generate_prompt(topic, difficulty)

@app.route('/')    
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    global user_input, conversation, current_question

    topic = request.form.get('topic')
    difficulty = request.form.get('difficulty')
    
    if not topic or not difficulty:
        return jsonify({"error": "Topic and difficulty are required"}), 400
    
    if topic == "Trig":
        if difficulty == "Easy":
            user_input = trig_difficulty_easy()
        elif difficulty == "Medium":
            user_input = trig_difficulty_medium()
        elif difficulty == "Hard":
            user_input = trig_difficulty_hard()
        elif difficulty == "Difficult":
            user_input = trig_difficulty_difficult()
        else:
            return jsonify({"error": "Invalid difficulty level"}), 400
        
    if topic == "Para":
        if difficulty == "Easy":
            user_input = para_difficulty_easy()
        elif difficulty == "Medium":
            user_input = para_difficulty_medium()
        elif difficulty == "Hard":
            user_input = para_difficulty_hard()
        elif difficulty == "Difficult":
            user_input = para_difficulty_difficult()
        else:
            return jsonify({"error": "Invalid difficulty level"}), 400
                    
    if topic == "Numbers":
        if difficulty == "Easy":
            user_input = numbers_difficulty_easy()
        elif difficulty == "Medium":
            user_input = numbers_difficulty_medium()
        elif difficulty == "Hard":
            user_input = numbers_difficulty_hard()
        elif difficulty == "Difficult":
            user_input = numbers_difficulty_difficult()
        else:
            return jsonify({"error": "Invalid difficulty level"}), 400
                    
    if topic == "Prop":
        if difficulty == "Easy":
            user_input = propor_difficulty_easy()
        elif difficulty == "Medium":
            user_input = propor_difficulty_medium()
        elif difficulty == "Hard":
            user_input = propor_difficulty_hard()
        elif difficulty == "Difficult":
            user_input = propor_difficulty_difficult()
        else:
            return jsonify({"error": "Invalid difficulty level"}), 400
                    
    if topic == "Matrices":
        if difficulty == "Easy":
            user_input = matric_difficulty_easy()
        elif difficulty == "Medium":
            user_input = matric_difficulty_medium()
        elif difficulty == "Hard":
            user_input = matric_difficulty_hard()
        elif difficulty == "Difficult":
            user_input = matric_difficulty_difficult()
        else:
            return jsonify({"error": "Invalid difficulty level"}), 400
                    
    if topic == "Inequalities":
        if difficulty == "Easy":
            user_input = inequalities_difficulty_easy()
        elif difficulty == "Medium":
            user_input = inequalities_difficulty_medium()
        elif difficulty == "Hard":
            user_input = inequalities_difficulty_hard()
        elif difficulty == "Difficult":
            user_input = inequalities_difficulty_difficult()
        else:
            return jsonify({"error": "Invalid difficulty level"}), 400
                    
    if topic == "Probabilities":
        if difficulty == "Easy":
            user_input = probabilities_difficulty_easy()
        elif difficulty == "Medium":
            user_input = probabilities_difficulty_medium()
        elif difficulty == "Hard":
            user_input = probabilities_difficulty_hard()
        elif difficulty == "Difficult":
            user_input = probabilities_difficulty_difficult()
        else:
            return jsonify({"error": "Invalid difficulty level"}), 400
                    
    if topic == "Percentages":
        if difficulty == "Easy":
            user_input = Percentage_difficulty_easy()
        elif difficulty == "Medium":
            user_input = Percentage_difficulty_medium()
        elif difficulty == "Hard":
            user_input = Percentage_difficulty_hard()
        elif difficulty == "Difficult":
            user_input = Percentage_difficulty_difficult()
        else:
            return jsonify({"error": "Invalid difficulty level"}), 400
                    
    if topic == "Number Sequences":
        if difficulty == "Easy":
            user_input = Sequences_difficulty_easy()
        elif difficulty == "Medium":
            user_input = Sequences_difficulty_medium()
        elif difficulty == "Hard":
            user_input = Sequences_difficulty_hard()
        elif difficulty == "Difficult":
            user_input = Sequences_difficulty_difficult()
        else:
            return jsonify({"error": "Invalid difficulty level"}), 400
                    
    if topic == "Ratio":
        if difficulty == "Easy":
            user_input = ratio_difficulty_easy()
        elif difficulty == "Medium":
            user_input = ratio_difficulty_medium()
        elif difficulty == "Hard":
            user_input = ratio_difficulty_hard()
        elif difficulty == "Difficult":
            user_input = ratio_difficulty_difficult()
        else:
            return jsonify({"error": "Invalid difficulty level"}), 400
        
    user_input += f" Topic: {topic}."
    conversation = [{"role": "system", "content": user_input}]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=conversation,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        current_question = response['choices'][0]['message']['content']
        print(current_question)
        return jsonify({"response": current_question})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
def format_choices(question):
    # Assuming choices are separated by \n
    if "\n" in question:
        parts = question.split('\n')
        question_text = parts[0]
        choices = parts[1:]
        formatted_choices = '\n'.join(choices)
        return f"{question_text}\n{formatted_choices}"
    return question

@app.route('/respond', methods=['POST'])
def respond():
    global conversation, current_question
    
    user_response = request.form.get('response')
    
    if not user_response:
        return jsonify({"error": "Response is required"}), 400

    conversation.append({"role": "assistant", "content": f"Question: {current_question} Here's my Answer: {user_response} Is it correct?"})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=conversation,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        feedback = response['choices'][0]['message']['content']
        
        # Prepare for the next question
        current_question = None
        conversation = []

        return jsonify({"response": feedback})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=8080)
