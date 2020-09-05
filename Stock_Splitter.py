# This program is designed to take a set of stock tickers and return share prices to make an even split across all of them
# Still needs commenting

import time
import yfinance as yf

def stock_split():
    stock_num = 0
    while True:
        try:
            stock_num = int(input("How many stocks total would you like to split evenly?\n"))
            if stock_num == 1:
                print("Well that kind of defeats the purpose, doesn't it?")
                time.sleep(4)
                exit()
            if stock_num == 0 or stock_num < 0:
                print("Very Funny, hope your happy with yourself.")
                time.sleep(5)
                exit()
            else:
                print("Great, well split " + str(stock_num) + " Stocks!\n")
                break
        except(ValueError, TypeError):
            print("That doesn't seem right...")

    time.sleep(1)
    cash = int(input("Now how much money are you investing?\n")) / stock_num
    time.sleep(1)
    print("Perfect!, now we just need the tickers for your stocks!\n Please use all caps (EX: DPZ or TSLA)\n")
    print("Please enter your stock tickers now.")

    stocks = []
    tickers = []
    for i in range(stock_num):
        ticker = input(str(i + 1) + " : ")
        tickers.append(ticker)
        ticker_data = yf.Ticker(ticker)
        stock_info = ticker_data.get_info()
        price = (stock_info['previousClose'])
        stocks.append(price)

    buy_amount = []
    Total_Cost = []
    for i in range(stock_num):
        Buying_Check = cash / stocks[i]
        if Buying_Check <= 1:
            print("It looks like you dont have enough Cash to evenly split these stocks.")
            exit()
        else:
            pass

        buy_amount.append(round(cash / stocks[i]))
        Total_Cost.append(round(buy_amount[i] * stocks[i], 2))

    for i in range(stock_num):
        print("You need to buy", buy_amount[i], "of", tickers[i], "Totaling $", Total_Cost[i])


stock_split()

while True:
    retry = input('Hit enter to retry or type "exit" to exit.')
    if retry == "exit":
        exit()
    elif retry == "":
        stock_split()
    else:
        print("That didnt seem right...")
