import openai
from random import randrange
from time import sleep

openai.api_key = 'sk-proj-oBGiB1JdyO4aXOM3DM2MT3BlbkFJDIzdv21tBSwMptrL08es'


def difficulty_easy():
    global user_input
    x = randrange(0, 2)
    if x == 0:
        user_input = "Create an algebraic equation about trigonometry for 7th grade students who have just begun unerstanding easy trigonometry, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    else:
        user_input = "Create a word problem about trigonometry for 7th grade students who have just begun unerstanding easy trigonometry, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    return user_input


def difficulty_medium():
    x = randrange(0, 2)
    if x == 0:
        global user_input
        user_input = "Create an algebraic equation about trigonometry for 8th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    else:
        user_input = "Create a word problem about trigonometry for 8th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    return user_input

def difficulty_hard():
    x = randrange(0, 2)
    if x == 0:
        global user_input
        user_input = "Create an algebraic equation about trigonometry for 9th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    else:
        user_input = "Create a word problem about trigonometry for 9th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    return user_input
def difficulty_difficult():
    x = randrange(0, 2)
    if x == 0:
        global user_input
        user_input = "Create an algebraic equation about trigonometry for 10th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    else:
        user_input = "Create a word problem about trigonometry for 10th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    return user_input

conversation = []

user_input = None

while True:
    choose = input("The level of difficulty (Easy, Medium, Hard, Difficult): ")
    if choose == "Easy":
        user_input = difficulty_easy()
    elif choose == "Medium":
        user_input = difficulty_medium()
    elif choose == "Hard":
        user_input = difficulty_hard()
    elif choose == "Difficult":
        user_input = difficulty_difficult()
    else: print("Try inputing the difficulty again, please.")

    for i in range(5):
        sleep(2)

        conversation.append({"role": "user", "content": user_input})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=conversation,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        conversation.append({"role": "system", "content": response['choices'][0]['message']['content']})

        print("Bot:", response['choices'][0]['message']['content'])

        user_input2 = input("User: ")

        if user_input2.lower() == "exit":
            print("Exiting Conversation. Good luck studying!")
            break

        conversation.append({"role": "user", "content": user_input2})

        response2 = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=conversation,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        conversation.append({"role": "system", "content": response2['choices'][0]['message']['content']})

        print("Bot:", response2['choices'][0]['message']['content'])
