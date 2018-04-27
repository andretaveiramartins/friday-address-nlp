# Address NLP

This project uses google Geocoding API to parse a given address in the following formnat:

<code>{"street": "STREET NAME", "street_number": "STREET NUMBER}</code>

# Environment setup 

Download and install pip and python 3.6

# Optional : Create your own virtual environment

<code>python3 -m venv /path/to/new/virtual/environment</code>

# Install dependencies

<code>pip install -r requirements.txt</code>

# Running the server

To run the server just execute in the command line:

<code>python -m app</code>

# Running the server as a container

<code>docker build . -t address_nlp:latest</code>

<code>docker run -d -p 5000:5000 address_nlp</code>

# Using the API

Assuming you're running from your local computer, just open your browser and enter:

http://localhost:5000/address_nlp_process?address=ADDRESS_TO_BE_PARSED

# Known limitations

This project uses google Geocode API to parse a given address and output the street number and name. If the given address is not valid you'll receive an error. Google will associate the given address with a real address so if a fake address is given it is possible that the street name might differ due to google NLP/approximation algorith. For the cases where we have street numbers such as "123 B" or "b 23" google most times crop the letter out.
