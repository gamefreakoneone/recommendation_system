import requests
import json

def input_tastedive():
    baseurl="https://tastedive.com/api/similar"
    parameters=dict()
    parameters["limit"]=5
    parameters["k"]="380419-AmoghBij-Q7Q6O068"
    parameters["type"]=input("Which genre is it: \n")
    if parameters["type"]=="music":
        parameters["q"]=input("Give me the song. I will find something similar.")
    elif parameters["type"]=="movies":
        parameters["q"]=input("Give me the movie. I will find something similar.")
    elif parameters["type"]=="games":
        parameters["q"]=input("Give me the game. I will find something similar.")
    response=requests.get(baseurl,params=parameters)
def recommend():



print("Hey, This program is going to help you find the movies or games or TV shows or music: \n")
y="continue"
while y == "continue":
    program=input("So what do you want:\n# recommendation\n# scores ")
    if program=="recommendation" or program=="1":
        recommend()