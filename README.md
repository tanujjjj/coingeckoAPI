# YouGov Technical Exercise - Candidate Brief

As part of the YouGov recruitment process we would like you to complete a small coding exercise.
This gives you the opportunity to show off your technical skills and suitability for the role!
This task is made up scenario, but representative of a development task you may find yourself completing at YouGov.


## Briefing

As a new team member of a YouGov development team, you have been given the following request:
> A non-technical client that works with cryptocurrencies has a requirement to convert specific amounts of Bitcoin (BTC), Ethereum (ETH) or Ripple (XRP) into US Dollars (USD) in automated fashion. They have tried to use a free API available (https://www.coingecko.com/en/api/documentation), but are finding this difficult to understand and use. They have asked that you create a simple HTTP web server that is simple to use and serves their needs.

We have translated this briefing into a set of requirements. Create a Web Server that satisfies the following:
- The web server should have an endpoint `/exchange` that is reachable via a HTTP GET request
- This endpoint should take two URL parameters (e.g. `/exchange?coin=btc&amount=1.5`):
  - `coin`: The coin to exchange. The only valid inputs should be one of: "btc", "eth", "xrp". You should support any combination of upper/lower case characters.
  - `amount`: The amount to exchange into dollars. The only valid input should be a decimal number above 0 but below 10000 
- The endpoint should make a HTTP GET request to CoinGecko.com to obtain an up-to-date exchange rate for the desired `coin`. 
From this, convert the `amount` of `coin` into USD. 
Documentation can be found [here](https://www.coingecko.com/en/api/documentation), but your server should make a web request to one of the following to get the exchange rate:
  - https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd  
  - https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd 
  - https://api.coingecko.com/api/v3/simple/price?ids=ripple&vs_currencies=usd
- If all is correct, your HTTP server should respond with a JSON Response in the format of: `{"usd_amount": 12342}`. 
Note that the exchange rate is always changing, so don't expect the same value every time.
- For any malformed input or other errors, return a JSON string response with a useful message in an `error` field. Example: `{"error": "Invalid Amount."}`
- Upload your code to either GitHub or GitLab and provide the URL to your repository.

## Getting Started

We have also put some things together to help you get started. 
Specifically, we have:
- A basic HTTP server template that you can add your code to
- A set of acceptance tests that you can use to validate your technical solution

### Template Script

Inside `./currency_convert` you will find a `server.py` script. 
This script implements the HTTP endpoint you need (using the common Python HTTP framework [Flask](https://flask.palletsprojects.com/en/2.1.x/)). 
Your job is to add the code to request the exchange rate, perform the conversion and then return the value. 

**Before you get started please check that you can get this template working correctly by following the instructions below.**


At this point we assume that you already have Python installed on your computer.

For the server we need to install a few dependencies listed in the requirements file. 
From a Terminal/Command Prompt, execute:

```bash
% pip install -r requirements.txt
...
Installing collected packages: zipp, typing-extensions, urllib3, MarkupSafe, importlib-metadata, idna, charset-normalizer, certifi, Werkzeug, requests, Jinja2, itsdangerous, click, pycoingecko, flask
Successfully installed Jinja2-3.1.2 MarkupSafe-2.1.1 Werkzeug-2.1.2 certifi-2022.5.18.1 charset-normalizer-2.0.12 click-8.1.3 flask-2.1.2 idna-3.3 importlib-metadata-4.11.4 itsdangerous-2.1.2 pycoingecko-2.2.0 requests-2.27.1 typing-extensions-4.2.0 urllib3-1.26.9 zipp-3.8.0
```

Next check that you can launch the server correctly:
```bash
currency_convert % python server.py
 * Serving Flask app 'server' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses (0.0.0.0)
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:6001
 * Running on http://192.168.1.47:6001 (Press CTRL+C to quit)
```

Finally, check that you can make a successful web request to the server via the command line tool [curl](https://curl.se/docs/manual.html):
```bash
% curl "http://0.0.0.0:6001/exchange?coin=btc&amount=1.5"    
{"usd_amount":0}
%      
```
If you're working on Windows, it's possible you may need to change `0.0.0.0` to `127.0.0.1` depending on your network configuration.


### Acceptance Tests

A separate script has been provided that contain some quick tests that can be used to verify your solution works correctly.
These can be launched by running them as a Python script, passing in the server IP and Port to target:
```bash
% python acceptance_tests.py http://0.0.0.0:6001
Targeting http://0.0.0.0:6001

Running test cases...
Testing missing_params... Success!
Testing invalid_coin... Success!
Testing amount_lower_bound_check... Success!
Testing amount_upper_bound_check... Success!
Testing correct_case_btc... Success!
Testing correct_case_eth... Success!
Testing correct_case_xrp... Success!
Testing mixed_case_input_handling... Success!
```

This script assumes that your server is already running. They will all fail initially but should pass once your have implemented your code. 

**If you encounter issues getting the template or acceptance tests running then please reach out to the recruiter as someone can offer some assistance.**


## Other Notes
* We suggest that you spend no longer than 3 hours on this exercise. 
If you have time at the end, feel free to add some extra features to show off your skills, but this is not a requirement.
* The CoinGecko API is free and does not require any API key or authentication.
* For anything you would like to point out to the assessor, feel free to provide a README file with your solution.
* The acceptance tests only perform very basic checks, you are responsible for checking that your solution satisfies the requirements. 
* You are free to implement a server to the same requirements in a different language or framework if you choose. 
* However, since our backend services are mostly implemented in Python, our preference would be that you complete this exercise in Python.
* This is a trivial and useless API. 
However, this is a task is an opportunity to demonstrate your technical abilities, skills and knowledge, so code to the highest possible standard and show us how great you are!
