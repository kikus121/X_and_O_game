# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 15:13:36 2018

@author: Kamil
"""

from tkinter import *
 

def rowCheck(matrix):
    winner=0
    for i in range(0,3):
        if ((matrix[i][0]==matrix[i][1]) and (matrix[i][1]==matrix[i][2])):
            winner=matrix[i][0]
            return winner

        elif i==2 and not winner  >0:
            winner=0
            return winner
           
def columnCheck(matrix):
    winner=0
    for i in range(0,3):
        if ((matrix[0][i]==matrix[1][i]) and (matrix[1][i]==matrix[2][i])):
            winner=matrix[0][i]
            return winner

        elif i==2 and not winner >0:
            winner=0
            return winner  

def diognalCheck(matrix):
    winner=0
    if ((matrix[0][0]==matrix[1][1]) and (matrix[1][1]==matrix[2][2])or(matrix[0][2]==matrix[1][1]) and (matrix[1][1]==matrix[2][0])):
        winner=matrix[1][1]
        return winner

    else:
        winner=0
        return winner  




def ticTackToeWinner(matrix):
    
    row=rowCheck(matrix)    
    column=columnCheck(matrix)
    diognal=diognalCheck(matrix)

    if 2==row or 2==column or 2==diognal:
        return 2

    elif 1==row or 1==column or 1==diognal:
        return 1
    
    else:
         return 0


  
def updateGameMatrix(playerTurn,gameMatrix,x,y):
    gameMatrix[x][y]=playerTurn
    return gameMatrix
        
def updateTurn(turn):
    Turn=turn
    return Turn


       
class Buton:
    
    
    
    gameMatrix=[[0,0,0],[0,0,0],[0,0,0]]
    turn=0
    
    
    def __init__(self, master,x,y):
        self.master = master
        self.x = x
        self.y = y
        mark = "  "
        self.greet_button = Button(master, text=mark, command=self.change)
        self.greet_button.grid(row=y,column=x,sticky=N+S+E+W)

        
    def change(self):
       
            
            
        if (self.turn%2==0):
            self.mark = str(" X ")
            self.greet_button = Button(self.master, text=self.mark, command=self.change)
            self.greet_button.grid(row=self.y,column=self.x,sticky=N+S+E+W)
            Buton.turn=Buton.turn+1
            updateGameMatrix(1,Buton.gameMatrix,self.x,self.y)
            if ticTackToeWinner(Buton.gameMatrix)==1:
                print("X wins")
                self.reset()
            elif Buton.turn==9:
                 print("Draw")
                 self.reset()
     
                
            
        else:
            self.mark = str(" O ")
            self.greet_button = Button(self.master, text=self.mark, command=self.change)
            self.greet_button.grid(row=self.y,column=self.x,sticky=N+S+E+W)
            Buton.turn=Buton.turn+1
            updateGameMatrix(2,Buton.gameMatrix,self.x,self.y)
            if ticTackToeWinner(Buton.gameMatrix)==2:
                print("O wins")
                self.reset()
            elif Buton.turn==9:
                print("Draw")
                self.reset()
            
    def reset(self):
         Buton.turn=0
         Buton.gameMatrix=[[0,0,0],[0,0,0],[0,0,0]]
         self.master.quit()
        

              

