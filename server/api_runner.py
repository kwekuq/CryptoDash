class Runner():
    coins = ['BTC', 'LTC', 'ETH']
    URL = "https://chain.so/api/v2/get_price/"
    CURRENCY = "USD"


    def fetch_data(self,coin):
        import requests
        import json
        from datetime import datetime
        callresult = requests.get(self.URL+str(coin)+"/"+self.CURRENCY)
        if callresult.status_code == requests.codes.ok:
            jsonresult = json.loads(callresult.text)
            for price in jsonresult['data']['prices']:
                print(str(coin) + " \t " + str(datetime.now()) + " \t " + self.CURRENCY + price['price'] + " \t \t" + price['exchange'])

if __name__ == '__main__':
    runner = Runner()
    import time


    print("Coin \t DateTime \t \t \t \t \t \t Price \t \t Exchange")
    while True:
        for i in runner.coins:
            runner.fetch_data(i)
        time.sleep(20)
