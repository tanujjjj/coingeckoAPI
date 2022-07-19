import requests
import sys


def missing_params(host):
    response = requests.get(host + "/exchange")
    content = response.json()
    assert content.get('error'), "Error field is not present in JSON"


def invalid_coin(host):
    response = requests.get(host + "/exchange?coin=xrrrp&amount=200")
    content = response.json()
    assert content.get('error'), "Error field is not present in JSON"


def amount_lower_bound_check(host):
    response = requests.get(host + "/exchange?coin=btc&amount=0")
    content = response.json()
    assert content.get('error'), "Error field is not present in JSON"


def amount_upper_bound_check(host):
    response = requests.get(host + "/exchange?coin=btc&amount=9999999")
    content = response.json()
    assert content.get('error'), "Error field is not present in JSON"


def correct_case_btc(host):
    response = requests.get(host + "/exchange?coin=btc&amount=9")
    content = response.json()
    assert not content.get('error'), "'error' field is present for the success test case"
    assert content.get("usd_amount"), "'usd_amount' field is not present in JSON or has an invalid value"
    assert int(content.get("usd_amount")) > 0, "'usd_amount' field is not present in JSON or has an invalid value"


def correct_case_eth(host):
    response = requests.get(host + "/exchange?coin=eth&amount=9")
    content = response.json()
    assert not content.get('error'), "'error' field is present for the success test case"
    assert content.get("usd_amount"), "'usd_amount' field is not present in JSON or has an invalid value"
    assert int(content.get("usd_amount")) > 0, "'usd_amount' field is not present in JSON or has an invalid value"


def correct_case_xrp(host):
    response = requests.get(host + "/exchange?coin=xrp&amount=9")
    content = response.json()
    assert not content.get('error'), "'error' field is present for the success test case"
    assert content.get("usd_amount"), "'usd_amount' field is not present in JSON or has an invalid value"
    assert int(content.get("usd_amount")) > 0, "'usd_amount' field is not present in JSON or has an invalid value"


def mixed_case_input_handling(host):
    response = requests.get(host + "/exchange?coin=BtC&amount=100")
    content = response.json()
    assert content.get("usd_amount"), "'usd_amount' field is not present in JSON or has an invalid value"
    assert int(content.get("usd_amount")) > 0, "'usd_amount' field is not present in JSON or has an invalid value"


test_cases = (missing_params,
              invalid_coin,
              amount_lower_bound_check,
              amount_upper_bound_check,
              correct_case_btc,
              correct_case_eth,
              correct_case_xrp,
              mixed_case_input_handling)


def run_tests(host):
    for case in test_cases:
        try:
            print("Testing " + case.__name__, end="")
            case(host)
            print("... Success!")
        except Exception as err:
            print("... Failed! ({})".format(err))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        host = sys.argv[1]
    else:
        host = "http://127.0.0.1:6001/"

    print('Targeting ' + host)

    print('\nRunning test cases...')
    run_tests(host)
