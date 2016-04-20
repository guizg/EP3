# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 11:34:04 2016

@author: bvbit
"""

import jogo
import tkinter as tk

class Tabuleiro:
    
    def __init__ (self):
        self.jogo_tabuleiro = jogo.Jogo()
        self.window = tk.Tk()
        self.window.title("Jogo da Velha")
        self.window.geometry("300x350")
        
    def iniciar(self):
        self.window.mainloop()
        
app = Tabuleiro()
app.iniciar()


        
                
