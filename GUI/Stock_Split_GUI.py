import tkinter as tk
import tkinter.messagebox
import yfinance as yf


# Main Window
master = tk.Tk()

# Labels
tk.Label(master, text="Cash", font=(None, 10, "bold")).grid(row=0, column=1)
tk.Label(master, text="Tickers", font=(None, 10, "bold")).grid(row=2, column=1)

# Entry Fields
entry_cash = tk.Entry(master, justify="center")
entry_1 = tk.Entry(master, justify="center")
entry_2 = tk.Entry(master, justify="center")
entry_3 = tk.Entry(master, justify="center")
entry_4 = tk.Entry(master, justify="center")
entry_5 = tk.Entry(master, justify="center")

# Grid Placement For Entry Fields
entry_cash.grid(row=1, column=1)
entry_1.grid(row=4, column=1)
entry_2.grid(row=5, column=1)
entry_3.grid(row=6, column=1)
entry_4.grid(row=7, column=1)
entry_5.grid(row=8, column=1)

# Insert Default Data
entry_cash.insert(0, "0")
entry_1.insert(0, "DPZ")
entry_2.insert(0, "TSLA")
entry_3.insert(0, "BP")
entry_4.insert(0, "ENB")
entry_5.insert(0, "AAPL")

tickers = []


# Grabs data from filled entry fields
def get_data():
    cash = int(entry_cash.get())
    tickers.append(entry_1.get())
    tickers.append(entry_2.get())

    # Checking lengths of returned entry's
    if len(entry_3.get()) == 0:
        pass
    else:
        tickers.append(entry_3.get())
        if len(entry_4.get()) == 0:
            pass
        else:
            tickers.append(entry_4.get())
            if len(entry_5.get()) == 0:
                pass
            else:
                tickers.append(entry_5.get())

    return cash


# Calculates split and returns in a message box
def calculate():
    cash = get_data()

    # Splitting available cash by how many tickers were given
    cash /= len(tickers)

    stocks = []
    buy_amount = []
    total_cost = []

    # Getting ticker prices
    for i in range(len(tickers)):
        ticker_data = yf.Ticker(tickers[i])
        stock_info = ticker_data.get_info()
        price = (stock_info['previousClose'])
        stocks.append(price)

    # Checking if the user can afford to split the stocks evenly
    for i in range(len(tickers)):
        buying_check = cash / stocks[i]
        if buying_check <= 1:
            tkinter.messagebox.showinfo("Error", "You dont have enough to split these stocks.")
            exit()
        else:
            pass

        # Appending the amount of stocks needed to buy and the total cost of said stocks
        buy_amount.append(round(cash / stocks[i]))
        total_cost.append(round(buy_amount[i] * stocks[i], 2))

    # Preparing statements for messagebox
    message = ""
    for i in range(len(tickers)):
        current = "You need to buy " + str(buy_amount[i]) + " of " + str(tickers[i]) + " Totaling $" + str(total_cost[i])
        message = message + "\n" + current

    tkinter.messagebox.showinfo("Results", message)


# Button
tk.Button(master, text="Calculate", command=calculate).grid(row=9, column=1)

master.mainloop()
