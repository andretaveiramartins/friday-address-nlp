# Python version

Python 3.6

# Environment setup 

Create your virtual environment inside the mock-server folder

<code>python3 -m venv /path/to/virtual/env<code>

To activate the virtual environment 

source ENV_NAME/bin/activate

# Install dependencies

<code>pip install -r requirements.txt</code>

# Running the server

To run the server just execute in the command line:

<code>python -m mock_server<code>

# Examples on how to run the tests:
To run the tests do:

python -m app.test.

To run all test cases go to the IngestOrders and run from there:

python -m unittest discover -p "*Test.py"
# Running the server as a container

Build the container running

<code>docker build . -t dw_sfdc_mock_server:latest</code>
<code>docker run -d -p 5000:5000 dw_sfdc_mock_server</code>

# What I considered 
Address – This package is an address parsing library, it takes the guesswork out of using addresses in your applications.
USAAddress – USAAddress is a python library for parsing unstructured address strings into address components, using advanced NLP methods. You can try their web interface at the link here.
Street Address – Used as a street address formatter and parser. Based on the test cases from http://pyparsing.wikispaces.com/file/view/streetAddressParser.py

