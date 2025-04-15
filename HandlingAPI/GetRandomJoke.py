import requests
def getRandomJoke():
    url = 'https://api.freeapi.app/api/v1/public/randomjokes/joke/random'
    response = requests.get(url)
    data = response.json()
    if data ["data"] and "data" in data:
        jokeData = data["data"]
        joke = jokeData["content"]
        return joke
    else:
        raise Exception("Failed To Fetch Joke")

def main():
    try:
        randomJoke = getRandomJoke()
        print(f"Joke -> {randomJoke}")
    except Exception as error:
        print(str(error))

if __name__ == "__main__":
    main()