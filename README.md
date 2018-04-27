# Address NLP

Python 3.6

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