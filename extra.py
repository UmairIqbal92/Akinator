import pyttsx3
import wikipedia
import os
import webbrowser
import akinator

import datetime
# from text_to_speech import speak

# def aki():
#     aki = akinator.Akinator()

#     q = aki.start_game()

#     while aki.progression <= 80:
#         speak(q)
#         print(q)
#         a = takecommand().lower()
#         if a == "b":
#             try:
#                 q = aki.back()
#             except akinator.CantGoBackAnyFurther:
#                 pass
#         else:
#             if "no" in a:
#                 q = aki.answer(1)
#             elif "yes" in a:
#                 q = aki.answer(0)
#             else:
#                 print("Error")

#     aki.win()

#     correct = input(f"It's {aki.first_guess['name']} ({aki.first_guess['description']})! Was I correct?\n{aki.first_guess['absolute_picture_path']}\n\t")
#     if correct.lower() == "yes" or correct.lower() == "y":
#         print("Yay\n")
#     else:
#         print("Oof\n")







# def take_query():
#     hello()
#     while(True):
#         query=takecommand().lower()
#         if "from wikipedia" in query:
#             speak("Checking Wikipedia")
#             query=query.replace("wikipedia","")
#             result=wikipedia.summary(query,sentences=4)
#             speak("According to wikipedia")
#             speak(result)
#             print(result)



def take_query():
    # calling the Hello function for
    # making it more interactive
    hello()

    # This loop is infinite as it will take
    # our queries continuously until and unless
    # we do not say bye to exit or terminate
    # the program
    while (True):

        # taking the query and making it into
        # lower case so that most of the times
        # query matches and we get the perfect
        # output

        query = takecommand().lower()
        if "open geeksforgeeks" in query:
            speak("Opening GeeksforGeeks ")

            # in the open method we just to give the link
            # of the website and it automatically open
            # it in your default browser
            webbrowser.open("www.geeksforgeeks.com")
            continue

        elif "open google" in query:
            speak("Opening Google ")
            webbrowser.open("www.google.com")
            continue

        elif "which day it is" in query:
            tellDay()
            continue

        elif "tell me the time" in query:
            tellTime()
            continue

        elif "open youtube" in query:
            speak("Opening Youtube ")
            webbrowser.open("www.youtube.com")
            continue

        # this will exit and terminate the program
        elif "bye" in query:
            speak("Bye. Check Out GFG for more exicting things")
            exit()

        elif "from wikipedia" in query:

            # if any one wants to have a information
            # from wikipedia
            speak("Checking the wikipedia ")
            query = query.replace("wikipedia", "")

            # it will give the summary of 4 lines from
            # wikipedia we can increase and decrease
            # it also.
            result = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            speak(result)
            print(result)

        elif "tell me your name" in query:
            speak("I am Jarvis. Your deskstop Assistant")





if __name__ == '__main__':
    speak("I am Akinator. Let's play guessing")
    aki()
