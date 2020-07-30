import requests
import json



def input_tastedive():
    baseurl="https://tastedive.com/api/similar"
    parameters=dict()
    parameters["limit"]=5
    parameters["k"]="380419-AmoghBij-Q7Q6O068"
    temp=input("Which genre is it: \n")
    if temp=="movies"or temp=="movie" or temp=="Movies" or temp=="Movies":
        parameters["type"]="movies"
    elif temp=="games"or temp=="Game" or temp=="game" or temp=="Games":
        parameters["type"]="games"
    elif temp=="music" or temp=="Music":
        parameters["type"]="music"


    if parameters["type"]=="music":
        parameters["q"]=input("Give me the song. I will find something similar.\n")
    elif parameters["type"]=="movies":
        parameters["q"]=input("Give me the movie. I will find something similar.\n")
    elif parameters["type"]=="games":
        parameters["q"]=input("Give me the game. I will find something similar.\n")
    response=requests.get(baseurl,params=parameters).json()
    return response

def recommend():
    JSON_return=input_tastedive()
    lst_names=list()
    for i in JSON_return["Similar"]["Results"]:
        lst_names.append(i["Name"])
    if len(lst_names)!=0:
        print("The results I have found similar to is:")
        for i in lst_names:
            print("     #",i)
    else:
        print("Sorry, couldnt find anything similar... Why dont we try to check something else?")
    return None


def input_omdb():
    apiKey="546c6742"
    baseurl = 'http://www.omdbapi.com/?apikey='+apiKey
    parameters=dict()
    parameters["r"]="json"
    parameters["type"]=input("So is it a series or a movie?\n")
    parameters["t"]=input("Give me the title\n")
    response=requests.get(baseurl,params=parameters).json()
    print(response)
    return response



def rating():
    response=input_omdb()
    print("\n\nTitle:",response["Title"])
    print("Year:",response["Year"])
    print("Runtime:",response["Runtime"])
    print("__________________________________________________\n")
    print("RATINGS")
    print("__________________________________________________")
    print("Rotten Tomatoes:",response["Ratings"][1]["Value"])
    print("Meta Critic:",response["Ratings"][2]["Value"],"\n\n")
    return None




print("Hey, This program is going to help you find the movies or games or TV shows or music similar to the ones you love\n or you could find the rating of the show or movie you love: \n")
y="continue"
while y == "continue":
    program=input("So what do you want:\n1. recommendation\n2. rating\n")

    if (program=="recommendation") or (program=="Recommendation") or (program=="1"):
        print("Starting recommendation system")
        recommend()
    elif (program=="rating") or (program=="Rating")or(program=="2"):
        print("Starting rating function")
        rating()


    y=input("Wanna continue? type continue if you want to....")

print("Thank you.See you later!")