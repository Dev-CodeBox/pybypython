import requests
def getRandomJoke():
    url = 'https://api.freeapi.app/api/v1/public/quotes/quote/random'
    response = requests.get(url)
    data = response.json()
    if data.get("success") and ("data") in data:
        quoteData = data.get("data")
        quote = quoteData.get("content")
        return quote
    else:
        raise Exception("Failed To Fetch Quote")
def main():
    try:
        randomQuote = getRandomJoke()
        print(f"Random Quote -> {randomQuote}")
    except Exception as error:
        print(str(error))

if __name__ == "__main__":
    main()