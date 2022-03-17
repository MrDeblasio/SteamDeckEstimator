# All code below is copyright and owned by Deblasio 2022
# Please contact for any questions about redistribution
# I do not mind if you make a fork of the repl, please do not
# copy the code into another repl however.

class threemilfigures():
	deck64 = 360000
	deck256 = 1140000
	deck512 = 1500000

class eightythousandfigures():
	deck64 = 102600
	deck256 = 324900
	deck512 = 427500

class program():
	eightyk = eightythousandfigures()
	threemil = threemilfigures()

	def getChosenFigureModel(self, figure):
		if(figure == "3"):
			return threemil
		if(figure == "855"):
			return eightyk

#These are my prefered production numbers, so what I think valve will use.
#I just divided the total production (say 100,000) by 3 (so 33,333)
#I made all three devices equal because I'm assuming that Valve can change
#production on demand.
productionnumbers = [16666, 33333, 50000, 66666]

threemil = threemilfigures()
eightyk = eightythousandfigures()

def main():
	global productionnumbers
	
	isrunning = True
	monthcounter = 0

	decksleft = 0

	print("I highly recommend checking out the Reddit post I made (in the comment on the repl) to get a better understanding this tool. Please also check the comments on the reddit post for any questions you have, as they might already be answered.")

	customProductionNumbers = input("If you want to input your own production numbers, you can do so now. If you don't, please press enter. Please make sure that your estimated production is already divided by 3, so that you can get the production for one model. The production numbers must be in the form of an array, like so: 10000 10000 10000. Press enter to skip.")

	if (customProductionNumbers == ""):
		pass
	else:
		productionnumbers = customProductionNumbers.split(" ")
		for i in range(len(productionnumbers)):
			productionnumbers[int(i)] = int(productionnumbers[int(i)])
	
	deckmodel = str(input("What model of the Steam Deck do you want data on? (Please only enter the number) "))
	
	ordersmodel = str(input("Do you want to use the 855k orders model or the 3 million orders model? If you don't know, I'd reccomend the 3 million for realistic answers, but 855k for a sugarcoated answer. (Please only enter 3 or 855) "))

	#Get instance of program class
	prgm = program()
	#Get the preferred figure model
	figuremodel = prgm.getChosenFigureModel(ordersmodel)

	#Check if DeckModel is valid
	if (deckmodel == "64" or deckmodel == "256" or deckmodel == "512"):
		print("\n")
	else:
		print("Please retry with a valid deck model.")
		return

	#While loop to run until code stops
	while (isrunning):
		if(deckmodel == "64"):
			#Check if the loop just started
			if (monthcounter <= 0):
				#get the base amount of decks from the preferred figure model
				decksleft = figuremodel.deck64
				print("Decks Left = " + str(decksleft) + ", Month counter = " + str(monthcounter))
				decksleft = decksleft - productionnumbers[0] #This would be 16666
				monthcounter = monthcounter + 1 #add a month to the counter
				print("Decks Left = " + str(decksleft) + ", Month counter = " + str(monthcounter))
			else:
				#how the code gets the last array item if its over
				#the array's item count
				if (monthcounter >= len(productionnumbers)):
					decksleft = decksleft - productionnumbers[len(productionnumbers) - 1]
				else:
					decksleft = decksleft - productionnumbers[monthcounter]
				monthcounter = monthcounter + 1

				#stop the code if there are no more decks in the queue
				if(decksleft <= 0):
					decksleft = 0
					isrunning = False
					print("Decks Left = " + str(decksleft) + ", Month counter = " + str(monthcounter))
				else:
					print("Decks Left = " + str(decksleft) + ", Month counter = " + str(monthcounter))

					
		if(deckmodel == "256"):
			if (monthcounter <= 0):
				decksleft = figuremodel.deck256
				print("Decks Left = " + str(decksleft) + ", Month counter = " + str(monthcounter))
				decksleft = decksleft - productionnumbers[0]
				monthcounter = monthcounter + 1
				print("Decks Left = " + str(decksleft) + ", Month counter = " + str(monthcounter))
			else:
				if (monthcounter >= len(productionnumbers)):
					decksleft = decksleft - productionnumbers[len(productionnumbers) - 1]
				else:
					decksleft = decksleft - productionnumbers[monthcounter]
				monthcounter = monthcounter + 1
				if(decksleft <= 0):
					decksleft = 0
					isrunning = False
					print("Decks Left = " + str(decksleft) + ", Month counter = " + str(monthcounter))
				else:
					print("Decks Left = " + str(decksleft) + ", Month counter = " + str(monthcounter))

					
		if(deckmodel == "512"):
			if (monthcounter <= 0):
				decksleft = figuremodel.deck512
				print("Decks Left = " + str(decksleft) + ", Month counter = " + str(monthcounter))
				decksleft = decksleft - productionnumbers[0]
				monthcounter = monthcounter + 1
				print("Decks Left = " + str(decksleft) + ", Month counter = " + str(monthcounter))
			else:
				if (monthcounter >= len(productionnumbers)):
					decksleft = decksleft - productionnumbers[len(productionnumbers) - 1]
				else:
					decksleft = decksleft - productionnumbers[monthcounter]
				monthcounter = monthcounter + 1
				if(decksleft <= 0):
					decksleft = 0
					isrunning = False
					print("Decks Left = " + str(decksleft) + ", Month counter = " + str(monthcounter))
				else:
					print("Decks Left = " + str(decksleft) + ", Month counter = " + str(monthcounter))
	print("\n\nThese estimated timings would be simultaneous with the other models' productions, as the production rate is for the specific model of the deck.")
	print("\n\nThis is all estimation, please take this with a grain of salt! Also, just because it may take 12 months to finish, this doesn't mean it will take 12 months to get your deck, as you are probably not at the back of the queue, so try to guess where you are in the provided months.")
				
if (__name__ == "__main__"):
	main()
