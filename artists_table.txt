import sqlite3
conn = sqlite3.connect('tattoo_convention.db')

def main():
	c.execute('''CREATE TABLE artists
             (artist text, hourly_rate float, minimum_rate float, number_of_tattoos_done real)''')