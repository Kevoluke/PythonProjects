from tkinter import *
import random
from PIL import Image, ImageTk

root = Tk()
root.title('Card Deck')
#root.iconbitmap("C:\Users\User\OneDrive\Desktop\DATASCIENCE\gui")
root.geometry("900x500")
root.configure(background="green")


# Resize Cards
def resize_cards(card):
	#open the image
	our_card_img = Image.open(card)

	#resize the image
	our_card_resize_image = our_card_img.resize((150, 218))

	#output the card
	global our_card_image
	our_card_image = ImageTk.PhotoImage(our_card_resize_image)

	#Return the card
	return our_card_image


#Shuffle card function
def shuffle():
	#Define our deck
	suits = ["diamonds", "clubs", "hearts", "spades"]
	values = range(2, 15)
	#11 = Jack, 12 = Queen, 13 = King, 14 = Ace

	global deck
	deck = []

	for suit in suits:
		for value in values:
			deck.append(f'{value}_of_{suit}')
	print(deck)

	#Create our players
	global dealer, player
	dealer = []
	player = []

	#Grab a random card
	card = random.choice(deck)
	#remove card from deck
	deck.remove(card)
	#append card to dealer list
	dealer.append(card)
	#output card to screen

	global dealer_image
	dealer_image = resize_cards(f'images/cards/{card}.png')
	dealer_label.config(image=dealer_image)


	#Grab a random card for player
	card = random.choice(deck)
	#remove card from deck
	deck.remove(card)
	#append card to dealer list
	player.append(card)
	#output card to screen

	global player_image
	player_image = resize_cards(f'images/cards/{card}.png')
	player_label.config(image=player_image)


	#put number of remaining cards in title bar
	root.title(f'Card Deck - {len(deck)} Cards Left')

def deal_cards():
	try:
		#get dealer card
		card = random.choice(deck)
		#remove card from deck
		deck.remove(card)
		#append card to dealer list
		dealer.append(card)
		#output card to screen
		global dealer_image
		dealer_image = resize_cards(f'images/cards/{card}.png')
		dealer_label.config(image=dealer_image)



		#get player card
		card = random.choice(deck)
		#remove card from deck
		deck.remove(card)
		#append card to dealer list
		player.append(card)
		#output card to screen
		global player_image
		player_image = resize_cards(f'images/cards/{card}.png')
		player_label.config(image=player_image)

		#put number of remaining cards in title bar
		root.title(f'Card Deck - {len(deck)} Cards Left')

	except:
		#put number of remaining cards in title bar
		root.title(f'No Cards In Deck')




my_frame = Frame(root, bg="green")
my_frame.pack(pady=20)

#Create frames for cards
dealer_frame = LabelFrame(my_frame, text="Dealer", bd=0)
dealer_frame.grid(row=0, column=0, padx=20, ipadx=20)

player_frame = LabelFrame(my_frame, text="Player", bd=0)
player_frame.grid(row=0, column=1, padx=20, ipadx=20)

#put cards in frame
dealer_label = Label(dealer_frame, text='')
dealer_label.pack(pady=20)

player_label = Label(player_frame, text='')
player_label.pack(pady=20)

#Create Buttons
shuffle_button = Button(root, text="Shuffle Deck", font=("Helvetica", 14), command = shuffle)
shuffle_button.pack(pady=20)

card_button = Button(root, text="Get Cards", font=("Helvetica", 14), command = deal_cards)
card_button.pack(pady=20)



shuffle()

root.mainloop()
