# Crypto investment
This project can analyze cryptocurrencies and find coins that are stable enough to invest.

First it finds coins with capitalization more than $1B

Second, it goes to Binance and find symbols to trade this coins.

Third, only symbols with 4 years history left (in general, crypto has 4 years economic cycles)

Next, it normalize data: adjust prices to logarythmic scale to analyze ability to multiply deposit, and normalizes it to range [0, 1] (to be compared with each other)

Finally, it compared with simple growing line (the best stable scenario of growing) and calculate the difference (rmsd)

After that it will print and draw all symbols that are better than Bitcoin

# Dependencies
To install all dependencies run 
`pip install -r requirements.txt`

# Run
`python3 main.py`
