import requests


oanda_url_to_work_on = "practice_url"
oanda_access_token = "1816a9d5b9499beab43c676a1f329525-de17d9cda518706af6b85740c8757372"
oanda_account = "101-004-10249052-003"
oanda_currency_pair = "EUR_USD"
oanda_url = {
    "practice_url": "https://api-fxpractice.oanda.com",
    "real_url": "https://api-fxtrade.oanda.com",
    }
oanda_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + oanda_access_token,
}
oanda_account_url = oanda_url[oanda_url_to_work_on] + "/v3/accounts/" \
                    + oanda_account + "/"


def oanda_generate_request(end_point, payload):
    oanda_account_url = oanda_url[oanda_url_to_work_on] + "/v3/accounts/" \
                    + oanda_account + "/"
    oanda_get_price_url = oanda_account_url + end_point
    response = requests.get(oanda_get_price_url,
                 params=payload, headers=oanda_headers)
    if response.status_code == 200:
        return response


def get_instruments_from(pair):
    payload = {
        "instruments": pair,
    }
    end_point = "/instruments/" + pair + "/candles"
    return oanda_generate_request(end_point, payload)


print(get_instruments_from(oanda_currency_pair).json())