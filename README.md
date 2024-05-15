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


### Mitigation Plan
1. Microservice created for Laci Monsrud
2. Microservice is completed.
3. Code can be accessed on Github where it can be downloaded and run locally.
4. Should Laci have any problems getting the microservice working, I am available every evening after 5:30 PST, and all day Mondays. She can reach out via discord to workout a time to meet
5. If there are issues getting the microservice working, she should let me know as soon as possible so that we can work to get it running sooner rather than later. 
6. 
