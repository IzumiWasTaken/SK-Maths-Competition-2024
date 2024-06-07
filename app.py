import openai
from random import randrange
from time import sleep
from flask import Flask, render_template, request, jsonify
openai.api_key = 'sk-proj-oBGiB1JdyO4aXOM3DM2MT3BlbkFJDIzdv21tBSwMptrL08es'

app = Flask(__name__)

user_input = None
topic = None
current_question = None
conversation = []

def trig_difficulty_easy():
    topic = "Trig"
    difficulty = "Easy"
    x = randrange(0, 2)
    if x == 0:
        return "Create an algebraic equation about trigonometry for 7th grade students who have just begun understanding easy trigonometry, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    else:
        return "Create a word problem about trigonometry for 7th grade students who have just begun understanding easy trigonometry, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."

def trig_difficulty_medium():
    topic = "Trig"
    difficulty = "Medium"
    x = randrange(0, 2)
    if x == 0:
        return "Create an algebraic equation about trigonometry for 8th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    else:
        return "Create a word problem about trigonometry for 8th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."

def trig_difficulty_hard():
    topic = "Trig"
    difficulty = "Hard"
    x = randrange(0, 2)
    if x == 0:
        return "Create an algebraic equation about trigonometry for 9th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    else:
        return "Create a word problem about trigonometry for 9th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    
def trig_difficulty_difficult():
    topic = "Trig"
    difficulty = "Difficult"
    x = randrange(0, 2)
    if x == 0:
        return "Create an algebraic equation about trigonometry for 10th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    else:
        return "Create a word problem about trigonometry for 10th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."




def para_difficulty_easy():
    topic = "Para"
    difficulty = "Easy"
    x = randrange(0, 2)
    if x == 0:
        return "Create an algebraic equation about parabola for 7th grade students who have just begun understanding easy porabola, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    else:
        return "Create a word problem about parabola for 7th grade students who have just begun understanding easy parabola, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."

def para_difficulty_medium():
    topic = "Para"
    difficulty = "Medium"
    x = randrange(0, 2)
    if x == 0:
        return "Create an algebraic equation about parabole for 8th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    else:
        return "Create a word problem about parabola for 8th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."

def para_difficulty_hard():
    topic = "Para"
    difficulty = "Hard"
    x = randrange(0, 2)
    if x == 0:
        return "Create an algebraic equation about parabola for 9th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    else:
        return "Create a word problem about parabola for 9th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    
def para_difficulty_difficult():
    topic = "Para"
    difficulty = "Difficult"
    x = randrange(0, 2)
    if x == 0:
        return "Create an algebraic equation about parabola for 10th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    else:
        return "Create a word problem about parabola for 10th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."




def numbers_difficulty_easy():
    topic = "Numbers"
    difficulty = "Easy"
    x = randrange(0, 2)
    if x == 0:
        return "Create an algebraic equation about numbers for 7th grade students who have just begun understanding easy porabola, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    else:
        return "Create a word problem about numbers for 7th grade students who have just begun understanding easy parabola, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."

def numbers_difficulty_medium():
    topic = "Numbers"
    difficulty = "Medium"
    x = randrange(0, 2)
    if x == 0:
        return "Create an algebraic equation about numbers for 8th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    else:
        return "Create a word problem about numbers for 8th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."

def numbers_difficulty_hard():
    topic = "Numbers"
    difficulty = "Hard"
    x = randrange(0, 2)
    if x == 0:
        return "Create an algebraic equation about numbers for 9th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    else:
        return "Create a word problem about numbers for 9th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    
def numbers_difficulty_difficult():
    topic = "Numbers"
    difficulty = "Difficult"
    x = randrange(0, 2)
    if x == 0:
        return "Create an algebraic equation about numbers for 10th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    else:
        return "Create a word problem about numbers for 10th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."



def propor_difficulty_easy():
    topic = "Prop"
    difficulty = "Easy"
    x = randrange(0, 2)
    if x == 0:
        return "Create an algebraic equation about direct and inverse proportions for 7th grade students who have just begun understanding easy porabola, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    else:
        return "Create a word problem about direct and inverse proportions for 7th grade students who have just begun understanding easy parabola, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."

def propor_difficulty_medium():
    topic = "Prop"
    difficulty = "Medium"
    x = randrange(0, 2)
    if x == 0:
        return "Create an algebraic equation about direct and inverse proportions for 8th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    else:
        return "Create a word problem about direct and inverse proportions for 8th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."

def propor_difficulty_hard():
    topic = "Prop"
    difficulty = "Hard"
    x = randrange(0, 2)
    if x == 0:
        return "Create an algebraic equation about direct and inverse proportions for 9th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    else:
        return "Create a word problem about direct and inverse proportions for 9th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    
def propor_difficulty_difficult():
     topic = "Prop"
     difficulty = "Difficult"
     x = randrange(0, 2)
     if x == 0:
        return "Create an algebraic equation about direct and inverse proportions for 10th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
     else:
        return "Create a word problem about direct and inverse proportions for 10th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."





def matric_difficulty_easy():
    topic = "Matrices"
    difficulty = "Easy"
    x = randrange(0, 2)
    if x == 0:
        return "Create an algebraic equation about matrices for 7th grade students who have just begun understanding easy porabola, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    else:
        return "Create a word problem about matrices for 7th grade students who have just begun understanding easy parabola, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."

def matric_difficulty_medium():
    topic = "Matrices"
    difficulty = "Medium"
    x = randrange(0, 2)
    if x == 0:
        return "Create an algebraic equation about matrices for 8th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    else:
        return "Create a word problem about matrices for 8th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."

def matric_difficulty_hard():
    topic = "Matrices"
    difficulty = "Hard"
    x = randrange(0, 2)
    if x == 0:
        return "Create an algebraic equation about matrices for 9th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    else:
        return "Create a word problem about matrices for 9th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    
def matric_difficulty_difficult():
     topic = "Matrices"
     difficulty = "Difficult"
     x = randrange(0, 2)
     if x == 0:
        return "Create an algebraic equation about matrices for 10th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
     else:
        return "Create a word problem about maatrices for 10th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."




def inequalities_difficulty_easy():
    topic = "Inequalities"
    difficulty = "Easy"
    x = randrange(0, 2)
    if x == 0:
        return "Create an algebraic equation about inequalities for 7th grade students who have just begun understanding easy porabola, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    else:
        return "Create a word problem about inequalities for 7th grade students who have just begun understanding easy parabola, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."

def inequalities_difficulty_medium():
    topic = "Inequalities"
    difficulty = "Medium"
    x = randrange(0, 2)
    if x == 0:
        return "Create an algebraic equation about inequalities for 8th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    else:
        return "Create a word problem about inequalities for 8th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."

def inequalities_difficulty_hard():
    topic = "Inequalities"
    difficulty = "Hard"
    x = randrange(0, 2)
    if x == 0:
        return "Create an algebraic equation about inequalities for 9th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    else:
        return "Create a word problem about inequalities for 9th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    
def inequalities_difficulty_difficult():
     topic = "Inequalities"
     difficulty = "Difficult"
     x = randrange(0, 2)
     if x == 0:
        return "Create an algebraic equation about inequalities for 10th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
     else:
        return "Create a word problem about maatrices for inequalities for 10th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."




def probabilities_difficulty_easy():
    topic = "Probabilities"
    difficulty = "Easy"
    x = randrange(0, 2)
    if x == 0:
        return "Create an algebraic equation about probabilities for 7th grade students who have just begun understanding easy porabola, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    else:
        return "Create a word problem about probabilities for 7th grade students who have just begun understanding easy parabola, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."

def probabilities_difficulty_medium():
    topic = "Probabilities"
    difficulty = "Medium"
    x = randrange(0, 2)
    if x == 0:
        return "Create an algebraic equation about probabilities for 8th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    else:
        return "Create a word problem about probabilities for 8th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."

def probabilities_difficulty_hard():
    topic = "Probabilities"
    difficulty = "Hard"
    x = randrange(0, 2)
    if x == 0:
        return "Create an algebraic equation about probabilities for 9th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    else:
        return "Create a word problem about probabilities for 9th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    
def probabilities_difficulty_difficult():
     topic = "Probabilities"
     difficulty = "Difficult"
     x = randrange(0, 2)
     if x == 0:
        return "Create an algebraic equation about probabilities for 10th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
     else:
        return "Create a word problem about maatrices for probabilities for 10th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."





def Percentage_difficulty_easy():
    topic = "Percentage"
    difficulty = "Easy"
    x = randrange(0, 2)
    if x == 0:
        return "Create an algebraic equation about Percentage for 7th grade students who have just begun understanding easy porabola, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    else:
        return "Create a word problem about Percentage for 7th grade students who have just begun understanding easy parabola, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."

def Percentage_difficulty_medium():
    topic = "Percentage"
    difficulty = "Medium"
    x = randrange(0, 2)
    if x == 0:
        return "Create an algebraic equation about Percentage for 8th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    else:
        return "Create a word problem about Percentage for 8th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."

def Percentage_difficulty_hard():
    topic = "Percentage"
    difficulty = "Hard"
    x = randrange(0, 2)
    if x == 0:
        return "Create an algebraic equation about Percentage for 9th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    else:
        return "Create a word problem about Percentage for 9th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."

def Percentage_difficulty_difficult():
     topic = "Percentage"
     difficulty = "Difficult"
     x = randrange(0, 2)
     if x == 0:
        return "Create an algebraic equation about Percentage for 10th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
     else:
        return "Create a word problem about maatrices for Percentage for 10th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."




def Sequences_difficulty_easy():
    topic = "Number Sequences"
    difficulty = "Easy"
    x = randrange(0, 2)
    if x == 0:
        return "Create an algebraic equation about Number Sequences for 7th grade students who have just begun understanding easy porabola, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    else:
        return "Create a word problem about Number Sequences for 7th grade students who have just begun understanding easy parabola, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."

def Sequences_difficulty_medium():
    topic = "Number Sequences"
    difficulty = "Medium"
    x = randrange(0, 2)
    if x == 0:
        return "Create an algebraic equation about Number Sequences for 8th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    else:
        return "Create a word problem about Number Sequences for 8th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."

def Sequences_difficulty_hard():
    topic = "Number Sequences"
    difficulty = "Hard"
    x = randrange(0, 2)
    if x == 0:
        return "Create an algebraic equation about Number Sequences for 9th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    else:
        return "Create a word problem about Number Sequences for 9th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."

def Sequences_difficulty_difficult():
     topic = "Number Sequences"
     difficulty = "Difficult"
     x = randrange(0, 2)
     if x == 0:
        return "Create an algebraic equation about Number Sequences for 10th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
     else:
        return "Create a word problem about maatrices for Number Sequences for 10th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."



def ratio_difficulty_easy():
    topic = "Ratio"
    difficulty = "Easy"
    x = randrange(0, 2)
    if x == 0:
        return "Create an algebraic equation about ratio for 7th grade students who have just begun understanding easy porabola, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    else:
        return "Create a word problem about ratio for 7th grade students who have just begun understanding easy parabola, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."

def ratio_difficulty_medium():
    topic = "Ratio"
    difficulty = "Medium"
    x = randrange(0, 2)
    if x == 0:
        return "Create an algebraic equation about ratio for 8th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    else:
        return "Create a word problem about Number ratio for 8th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."

def ratio_difficulty_hard():
    topic = "Ratio"
    difficulty = "Hard"
    x = randrange(0, 2)
    if x == 0:
        return "Create an algebraic equation about ratio for 9th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
    else:
        return "Create a word problem about ratio for 9th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."

def ratio_difficulty_difficult():
     topic = "Ratio"
     difficulty = "Difficult"
     x = randrange(0, 2)
     if x == 0:
        return "Create an algebraic equation about ratio for 10th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."
     else:
        return "Create a word problem about maatrices for ratio for 10th grade students, and keep the answer for yourself. DON'T MENTION THAT YOU'VE BEEN PROMPTED TO KEEP THE ANSWER FOR YOURSELF. Then after I have provided my answer, you can tell me whether if I am right or wrong, and if I am wrong, provide me with the correct answer. PROVIDE 4 CHOICES FOR THE MULTIPLE CHOICE QUESTIONS, DONT USE SENTENCES."

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
    conversation = [{"role": "user", "content": user_input}]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=conversation,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        current_question = response['choices'][0]['message']['content']
        return jsonify({"response": current_question})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/respond', methods=['POST'])
def respond():
    global conversation, current_question
    
    user_response = request.form.get('response')

    if not user_response:
        return jsonify({"error": "Response is required"}), 400
    
    conversation.append({"role": "user", "content": f"Question: {current_question} Answer: {user_response}"})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=conversation,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        feedback = response['choices'][0]['message']['content']
        return jsonify({"response": feedback})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
