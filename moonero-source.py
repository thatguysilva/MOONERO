import pandas_datareader as web
import matplotlib.pyplot
from tkinter import * 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import datetime as dt
from PIL import ImageTk, Image
import yfinance as yf

#setting start date as monero launch date
start = dt.datetime(2014,4,18)
end = dt.datetime.now()

#collecting data from btc, eth and xmr
xmr = web.DataReader("XMR-USD", "yahoo",start,end)
btc = web.DataReader("BTC-USD", "yahoo", start, end)
eth = web.DataReader("ETH-USD", "yahoo",start,end)

#placing figure on screen and setting yscale to logarithmic
fig=Figure(figsize=(8,4),dpi=100)
plot1=fig.add_subplot(111)
plot1.set_yscale('log')



plot1.plot(xmr['Close'], label="XMR")
plot1.plot(btc['Close'], label="BTC")
plot1.plot(eth['Close'], label="ETH")
plot1.legend(loc="upper left")



window = Tk()
  

window.title('MOONERO')
  

window.geometry("800x680")


graphFrame = Frame(window, width=600, height= 300, bg='white')
graphFrame.grid(row=1, column=0, padx=10, pady=5)
bottomFrame = Frame(window, width=600, height= 275)
bottomFrame.grid(row=0, column=0, padx=10, pady=5)



canvas = FigureCanvasTkAgg(fig,
                               master = graphFrame)  
canvas.draw()
  
#placing the canvas on the Tkinter window
canvas.get_tk_widget().grid(row=0,column=0)

#placing logo
image = Image.open("moonero-logo.png")
photo = ImageTk.PhotoImage(image.resize((700,200),Image.ANTIALIAS))

label = Label(bottomFrame,image=photo)
label.image=photo
label.grid()

#creating the Matplotlib toolbar

toolbarFrame = Frame(master=window,width=800, height= 275)
toolbarFrame.grid(row=2,column=0,sticky=E,ipadx=80)
toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)



#live price
def get_current_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0]

var = DoubleVar()
var.set(get_current_price('XMR-USD'))

var2 = StringVar()
var2.set("Current XMR price is:")

label2 = Label(window, textvariable=var)
label2.place(x=150,y=640)

label3 = Label(window, textvariable=var2)
label3.place(x=20,y=640)
  
#run the GUI
window.mainloop()
