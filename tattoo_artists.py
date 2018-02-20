import sqlite3
db_url = 'tattoo_convention.db' #assigns table name
from tkinter import * #imports tkinter tools


def add_tattoos_done(artist, price):

	if not artist:
		raise Exception('Provide an artist\'s name')
	if isinstance(price, float) or price < 0:
		raise Exception('Price should be positive and rounded.') #makes sure price is valid number
		
	conn = sqlite3.connect(db_url) #connects to SQL server
	cursor = con.cursor()
	rows_mod = cursor.execute('Price set total_price = total_price + ? WHERE artist = ?', (price, vehicle)) #calculates running total per artist
	if rows_mod.rowcount == 0:
		cursor.execute('Add to table (?,?)', (artist, price)) #adds data to table if not available
		
	return price +total_price
		
	conn.commit()
	conn.close() #closes connection to database
	
def add_artists(artist):
	hourly = float(input('How much does your artist charge by hour?')
	shop_min = float(input('What\'s the minimum amount for a tattoo by this artist?')
	c.execute("INSERT INTO artist VALUES (artist,hourly,shop_min")
	
def average_tattoo():
	average = running_total/artists[numbers_of_tattoos_done]
	return average
	
	
def main():
	while True: 
		window = Tk() #opens window
		window.title("Tattoo Convention") #prints title for tinkr
		artist = input('Enter your tattoo artist or enter to quit')
		if not artist:
			break
		price = float(input('Enter how much you paid for your piece by %s' % artist)) 
	
		running_total = add_tattoos_done(artist,price) #sends price and artist to function
		average_total = average_tattoo(artist,price)
		
		

		
		