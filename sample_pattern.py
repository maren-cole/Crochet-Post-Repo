import requests


def display_crochet_patterns():
    url = 'http://localhost:5000/random-pattern'
    response = requests.get(url)
    print(response)
    pattern = response.json()
    print(pattern)


if __name__ == '__main__':
    display_crochet_patterns()
