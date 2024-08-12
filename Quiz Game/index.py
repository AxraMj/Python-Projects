#--------------------------------------
def new_game():
    guesses=[]
    correct_gusses=0
    question_number=1

    for key in questions:
        print("--------------------------------------------------")
        print(key)

        for i in options[question_number-1]:
            print(i)

        guess=input("Enter your answer (a/b/c/d): ").lower()
        guesses.append(guess)


        correct_gusses += check_answer(questions.get(key),guess)
        question_number +=1

    display_score(correct_gusses,guesses)
#--------------------------------------
def check_answer(answer,guess):
    if answer==guess:
        print("CORRECT!!")
        return 1
    else:
        print("WRONG!!")
        return 0
    
#--------------------------------------
def display_score(correct_guesses,guesses):
    print("-------------------------------------------")
    print("RESULT")
    print("--------------------------------------------")
    print("Answers: ",end="")
    for i in questions:
        print(questions.get(i),end=" ")
    print()

    print("Guesses: ",end="")
    for i in guesses:
        print(i,end=" ")
    print()

    score=int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")
    
#--------------------------------------
def play_again():
    response=input("Do you want to play again? (yes/no): ")
    response=response.upper()

    if response == "YES":
        return True
    else:
        return False

questions={
    "What gets wetter as it dries?":"a",
    "If you drop a yellow hat in the Red Sea, what does it become?":"b",
    "What can you catch but not throw?":"c",
    "What has keys but can’t open locks?":"a",
    "What has a face and two hands but no arms or legs?":"a",
}

options=[["a.Towel","b.Sponge","c.Paper","d.Cloth"],
         ["a.Blue","b.Wet","c.Dry","d.Red"],
         ["a. A fish","b.A ball","c. A cold","d.A Frisbee"],
         ["a.piano","b.door","c.computer","d.map"],
         ["a.clock","b.robot","c.doll","d.painting"]
         ]

new_game()

while play_again():
    new_game()
    
print("Byeeee!!")
