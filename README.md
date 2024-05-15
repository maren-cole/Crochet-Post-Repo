### Requesting and Receiving Data from the Microservice

To request data from the microservice, you can use an HTTP GET request. Below are the clear instructions:

1. Make an HTTP GET request to the endpoint `/random-pattern` of the microservice.
2. The microservice will generate a random crochet pattern and return it as a JSON response.
3. Parse the JSON response to extract the pattern data.

Example call using Python requests library:

```python
import requests

# Make a GET request to the microservice endpoint
response = requests.get('http://localhost:5000/random-pattern')

# Extract the JSON response
pattern_data = response.json()

```
