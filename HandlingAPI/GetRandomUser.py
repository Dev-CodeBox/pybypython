import requests
def getRandomUser():
    url = 'https://api.freeapi.app/api/v1/public/randomusers/user/random'
    response = requests.get(url)
    data = response.json()
    if data["success"] and "data" in data :
        userData = data["data"]
        userName = userData["login"]["username"]
        return userName
    else:
        raise Exception("Failed To Fetch User Data")

def main():
    try:
        randomUserName = getRandomUser()
        print(f"UserName -> {randomUserName}")
    except Exception as error:
        print(str(error))


if __name__ == "__main__":
    main()