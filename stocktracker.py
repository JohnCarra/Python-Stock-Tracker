import pandas as pd  # data manipulation and analysis package
# enables data pull from Alpha Vantage
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt  # if you want to plot your findings
import time
import smtplib  # enables you to send emails

# Getting the data from alpha_vantage
ts = TimeSeries(key='CZK4PSW4EWOIOSUG', output_format='pandas')
data, meta_data = ts.get_intraday(
    symbol='AAPL', interval='1min', outputsize='full')

# We are currently interested in the latest price
close_data = data['4. close']  # The close data column
# Selecting the last price from the close_data column
last_price = close_data[0]

# Check if you're getting a correct value
print(last_price)

# Set the desired message you want to see once the stock price is at a certain level
sender_email = "someone@gmail.com"  # The sender email
rec_email = "someone2@gmail.com"  # The receiver email
password = ("password")  # The password to the sender email
message = "AAPL STOCK ALERT!!! The stock is at above price you set " + \
    "%.6f" % last_price  # The message you want to send
target_sell_price = 220  # enter the price you want to sell at

if last_price > target_sell_price:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)  # logs into your email account
    print("Login Success")  # confirms that you have logged in succesfully
    # send the email with your custom mesage
    server.sendmail(sender_email, rec_email, message)
    print("Email was sent")  # confirms that the email was sent
