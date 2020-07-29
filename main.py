import requests_with_caching

print("Hey, This program is going to help you find the movies or games or TV shows or music: \n")
y="continue"
while y == "continue":
    q=input("So what do you want to get reccommended about:\n ")
    parameters["q"]=