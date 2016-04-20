# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 11:34:04 2016

@author: bvbit
"""

import jogo
import tkinter as tk

class Tabuleiro:
    
    def _init_ (self):
        self.jogo_tabuleiro = jogo.Jogo()
        self.window = tk.Tk()
        self.window.title("Jogo da Velha")
        
                
