

from random import shuffle
from tkinter import * 
from tkinter import messagebox as mb
import PIL.ImageTk, PIL.Image
import tkinter.font as font
import webbrowser


class card:
     
    def __init__(self,rank,suit,iD):
        self.rank = rank
        self.suit = suit
        self.iD = iD
        
    def getRank(self):
        return self.rank
    
    def getSuit(self):
        return self.suit
    
  

    
class hand:
    
    def __init__(self, currCards):
        self.currCards = currCards
        
    def addCard(self, newCard):
        self.currCards.append(newCard)
        
    def getValue(self):
        a = len(self.currCards)
        res = 0
        for i in range(0,a):
            temp = (self.currCards[i]).getRank()
            if(temp in [2,3,4,5,6,7,8,9,10]):
                res += temp
                
            elif(temp in [11,12,13]):
                res += 10
                
            else:
                res += 11 
                  
        return res
    

    def softValue(self):
        l = len(self.currCards)
        val = 0
        
        for i in range(l):
            temp = self.currCards[i].getRank()
            if(temp in [2,3,4,5,6,7,8,9,10]):
                val += temp
            elif(temp in [11,12,13]):
                val += 10
            else:
                val += 1
                
        return val
            


class Deck:

    def __init__(self):
        self.cards = [ 
                         1,2,3,4,5,6,7,8,9,10,11,12,13,
                        14,15,16,17,18,19,20,21,22,23,24,25,26,
                        27,28,29,30,31,32,33,34,35,36,37,38,39,
                        40,41,42,43,44,45,46,47,48,49,50,51,52  
                     ]
    
    def shufle(self):
        shuffle(self.cards)
        
    def dealCard(self):
        i = self.cards.pop()
        rnk = i % 13 
        if(i in [13,26,39,52]):
            rnk = 13
        if(i <= 13):
            suit = 'H'
        elif(i <= 26):
            suit = 'D'
        elif(i <= 39):
            suit = 'S'
        else:
            suit = 'C'
        c = card(rnk, suit, i)

        return c
    
 
    
 
class Play:
     
    def __init__(self):
        ply = []
        deal = []
        self.myDeck = Deck()
        self.myDeck.shufle()
        self.hPlayer = hand(ply)
        self.hDealer = hand(deal)
        self.inPlay = False
        self.aceP = 0
        self.aceD = 0
    
    
    def hit(self):
        a = self.myDeck.dealCard()
        #if(a.id in [1,14,27,40]):
                #self.aceP +=1
        
        self.hPlayer.addCard(a)
        
        
        if(self.hPlayer.softValue() > 21):
            print("busted")
        
        return
        
    
    def Check(self):
        
        if (self.aceP == 2 or self.aceP == 3 or self.aceP == 4) :
            if(self.hDealer.getValue() > self.hPlayer.softValue() + 10):
                return 0
            return 1

        elif(self.hDealer.softValue() > self.hPlayer.getValue() or 
            (self.hDealer.getValue() < 21  and self.hDealer.getValue() > self.hPlayer.getValue()) or 
            self.hDealer.getValue()==21  or (self.hPlayer.getValue() > 21 and (self.hDealer.softValue() > self.hPlayer.softValue() or ( self.hDealer.getValue() < 21 and self.hDealer.getValue() > self.hPlayer.softValue())))) :
            return 0
        

        return 1

        
    def checkBlackJack(self):
        if(self.hPlayer.getValue() == 21 or self.hPlayer.softValue() == 21):
            return True
        elif((self.aceP == 2 or self.aceP == 3 or self.aceP == 4) and self.hPlayer.softValue() + 10 == 21):
            return True
        else:
            return False
          
    def Restart(self):
        pass



#def newCard(play):
 #   play.hPlayer.addCard(play.myDeck.dealCard())
  #  index = len(start.hPlayer.currCards)-1
   # Label(cards,image=arr[start.hPlayer.currCards[index].iD - 1],padx=1,pady=1).grid(row=0, column=index)




# Result messegeboxes 
def Tie():
    mb.showinfo("Result","\t\tGame Tied!! \t\t")

def DealerWon():
    mb.showinfo("Result","\t\tDealer Won!!\n\tBetter luck NEXT Time\t")

def Blackjack():
    mb.showinfo("Result","\tBlackjack !! :\t \n \tYou Won !!")

def YouWon():
    mb.showinfo("Result","\tHurrah , Congratulations\n\t You Won!!")

def PlayerBusted():
    mb.showinfo("Result","\tOOPS Busted : You Lost !!\n\tBetter luck NEXT Time")




#Main function contains algorithm for the game
def main():

        root = Tk()
        root.title("BLACKJACK")
        root.iconbitmap("icon.ico")
        arr = []
        arr.append(PIL.ImageTk.PhotoImage(PIL.Image.open("uf.png")))
        for i in range(1,53):
            bg = PIL.ImageTk.PhotoImage(PIL.Image.open(str(i)+".png"))
            arr.append(bg)
        

        root.geometry("1200x1200")


        #placing background image
        bg = PIL.ImageTk.PhotoImage(PIL.Image.open("casino22.jpg")) #cbg.jpg
        labelb = Label(root, image=bg)
        labelb.place(x=0,y=0)


        #frame for displaying cards of player
        cards = LabelFrame(root, padx=2, pady=4)
        cards.grid(row=0,column=0, padx = 85, pady = 10)


        #frame for displaying cards of dealer
        cards2 = LabelFrame(root, padx=2, pady=4)
        cards2.grid(row=2,column=0,padx = 85, pady = 10)


        #unfolded image
        img3 = PIL.ImageTk.PhotoImage(PIL.Image.open("uf.png"))


        #Players image
        playr = PIL.ImageTk.PhotoImage(PIL.Image.open("dealer111.png"))
        Label(cards2,image=playr,padx=1,pady=1).grid(row=0, column=0)


        #Dealers Image
        deal = PIL.ImageTk.PhotoImage(PIL.Image.open("playr12.png"))
        Label(cards,image=deal,padx=1,pady=1).grid(row=0, column=0)
        
        
        #displaying cards unfolded for  player
        for i in range(1,10):
            Label(cards,image=img3,padx=1,pady=1).grid(row=0, column=i)

        #displaying cards unfolded for dealer
        for i in range(1,10):
            Label(cards2,image=img3,padx=1,pady=1).grid(row=0, column=i)  


        #event when new game button is pressed
        def startGame() :

            #intialising cards again(folding cards)
            for i in range(1,10):
                Label(cards,image=img3,padx=1,pady=1).grid(row=0, column=i)  

            for i in range(1,10):
                Label(cards2,image=img3,padx=1,pady=1).grid(row=0, column=i)   
            
            #creating instance of play class
            start = Play()
            

            #dealing 2 cards to player
            start.hPlayer.addCard(start.myDeck.dealCard())
            start.hPlayer.addCard(start.myDeck.dealCard())


            for i in start.hPlayer.currCards :
                if (i.rank == 1):
                    start.aceP += 1

            Label(cards,image=arr[(start.hPlayer.currCards[0]).iD ],padx=1,pady=1).grid(row=0, column=1)
            Label(cards,image=arr[start.hPlayer.currCards[1].iD],padx=1,pady=1).grid(row=0, column=2)

            
            #dealing cards to dealer
            start.hDealer.addCard(start.myDeck.dealCard())
            start.hDealer.addCard(start.myDeck.dealCard())

            for i in start.hDealer.currCards :
                if (i.rank == 1):
                    start.aceD += 1

            Label(cards2,image=arr[start.hDealer.currCards[0].iD ],padx=1,pady=1).grid(row=0, column=1)


            """ Stand function : Called when player wants to stays
                It unfolds all cards one by one
                It also calculates sum of player and dealer and then compare,
                scores of each to decide the winner """

            def stand():
                Label(cards2,image=arr[start.hDealer.currCards[1].iD ],padx=1,pady=1).grid(row=0, column=2)
                flag = 0
                while(start.hDealer.softValue() < 17 and start.Check()):

                    if(start.hDealer.getValue() == 21):
                        break

                    flag = 0
                    if(start.aceD == 2):
                        if(start.aceP == 2):
                            if(start.hDealer.softValue() + 10 < 21 and (start.hDealer.softValue() + 10 > start.hPlayer.softValue() + 10)):
                                flag = 1
                                break
                        elif(start.hDealer.softValue() + 10 < 21 and start.hDealer.softValue() + 10 > start.hPlayer.getValue()):
                            flag = 1
                            break

                    if(start.aceD == 3):
                        if(start.hDealer.softValue() + 10 < 21 and ((start.hDealer.softValue() + 10 > start.hPlayer.softValue() + 10) or (start.hDealer.softValue() + 10 > start.hPlayer.getValue()))):
                                flag = 1
                                break
                                
                    
                    a = start.myDeck.dealCard()
                    #if(a.iD in [1,14,27,40]):
                        #start.aceP +=1
                    if(a.rank == 1):
                        start.aceD += 1

                    start.hDealer.addCard(a)

                    ind = len(start.hDealer.currCards) - 1
                    Label(cards2,image=arr[start.hDealer.currCards[ind].iD ],padx=1,pady=1).grid(row=0, column=ind+1)

                if(flag):
                    DealerWon()
                    print("Dealer Wins")
                
                if(start.aceP == 2):
                    if( start.hDealer.getValue() <= 21):
                        if(start.hDealer.getValue() < start.hPlayer.softValue() + 10):
                            YouWon()
                            print("Player Won")
                        else:
                            DealerWon()
                    elif (start.hDealer.softValue() < start.hPlayer.softValue() + 10):
                        YouWon()
                        print("Player Won")
                    else:
                        YouWon()
                        print("Player Win")

                elif(start.hDealer.getValue() == start.hPlayer.getValue() or 
                    start.hDealer.softValue() == start.hPlayer.getValue() or 
                    start.hDealer.getValue() == start.hPlayer.softValue() or 
                    start.hDealer.softValue() == start.hPlayer.softValue() ) :

                    Tie()
                    print("tie")

                elif(not start.Check()  and (start.hDealer.softValue() <= 21 or start.hDealer.getValue() == 21)):
                    DealerWon()
                    print("Dealer wins")

                elif (start.checkBlackJack()):
                    Blackjack()
                    print("Player Wins : Blackjack")
                else:
                    YouWon()
                    print("player wins")  



            #checking if blackjack
            if(start.checkBlackJack()):
                stand()


            #if player want to hit
            def callOnHit():                
                start.hPlayer.addCard(start.myDeck.dealCard())
                index = len(start.hPlayer.currCards)-1

                if(start.hPlayer.currCards[index].iD == 1):
                        start.aceP += 1
                
                Label(cards,image=arr[start.hPlayer.currCards[index].iD],padx=1,pady=1).grid(row=0, column=index+1)

                if(start.hPlayer.softValue() > 21):
                    PlayerBusted()
                    print("Dealer Wins and Player Busted")
                elif(start.checkBlackJack()):
                    stand()
                


            #Frame containing stand and hit button    
            actions = LabelFrame(root, bg="#fcce03")
            actions.grid(row=4,column=0, padx=10,pady=10)
            
            #Font style for text in stand and hit
            myFont = font.Font(size=20)

            #Hit button
            hit = Button(actions,text="HIT",command=callOnHit,activeforeground="white",
                activebackground="black",bg="grey",fg="white",width="8" ,relief="raised") ##d203fc
            hit['font'] = myFont
            hit.grid(sticky="W",row=0,column=0)


            #Stand Button
            stan= Button(actions,text="STAND", command=stand,activeforeground="white",
                activebackground="black",bg="grey",fg="white",width="8" ,relief="raised")
            stan['font'] = myFont
            stan.grid(sticky="W",row=0,column=1)

                       

        #Frame showing options
        options = LabelFrame(root, bg="black") 
        options.grid(row=5,column=0, padx=10,pady=10) 

        #Button for new game
        im =  PIL.ImageTk.PhotoImage(PIL.Image.open("bothn.jpeg"))
        ngl = Button(options, image=im,command=startGame,relief="raised")
        ngl.grid(sticky="W",row=0,column=0) 


        #Function call when user wants to quit
        def quit():
            result = mb.askquestion("Quit","Do you really want to quit the game?")
            if result == "yes":
                root.destroy()
            else:
                mb.showinfo("Return","Returning to the game")
        

        #Button for quitting
        Q =  PIL.ImageTk.PhotoImage(PIL.Image.open("bothq.jpeg"))
        qt = Button(options, image=Q,command=quit,relief="raised")
        qt.grid(sticky="W",row=0,column=1) 



        #button for instruction
        mFont = font.Font(size=15)
        url = "https://en.wikipedia.org/wiki/Blackjack"

        def openweb():
            webbrowser.open(url,new=1)

        Btn = Button(root, text="HOW TO PLAY",bg="red", fg="white",command=openweb)
        Btn['font'] = mFont
        Btn.grid(row=6,column=0,padx=10,pady=10)

        root.mainloop()  
        


#calling main function    
if __name__ == "__main__" :
    main()
    



