# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 22:56:44 2016

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
        
        self.window.rowconfigure(0, minsize=100, weight=1)
        self.window.rowconfigure(1, minsize=100, weight=1)
        self.window.rowconfigure(2, minsize=100, weight=1)
        self.window.rowconfigure(3, minsize=50, weight=1)
        self.window.columnconfigure(0, minsize=100, weight=1)
        self.window.columnconfigure(1, minsize=100, weight=1)
        self.window.columnconfigure(2, minsize=100, weight=1)
        
                     
        self.botão00 = tk.Button(self.window)
        self.botão00.grid(row=0, column=0, sticky="nsew")
        self.botão00.configure(command=self.apertou_botao00)
                
        self.botão01 = tk.Button(self.window)
        self.botão01.grid(row=0, column=1, sticky="nsew")
        self.botão01.configure(command=self.apertou_botao01)

        self.botão02 = tk.Button(self.window)
        self.botão02.grid(row=0, column=2, sticky="nsew")
        self.botão02.configure(command=self.apertou_botao02)        

        self.botão10 = tk.Button(self.window)
        self.botão10.grid(row=1, column=0, sticky="nsew")
        self.botão10.configure(command=self.apertou_botao10)

        self.botão11 = tk.Button(self.window)
        self.botão11.grid(row=1, column=1, sticky="nsew")
        self.botão11.configure(command=self.apertou_botao11)

        self.botão12 = tk.Button(self.window)
        self.botão12.grid(row=1, column=2, sticky="nsew")
        self.botão12.configure(command=self.apertou_botao12)

        self.botão20 = tk.Button(self.window)
        self.botão20.grid(row=2, column=0, sticky="nsew")
        self.botão20.configure(command=self.apertou_botao20)

        self.botão21 = tk.Button(self.window)
        self.botão21.grid(row=2, column=1, sticky="nsew")
        self.botão21.configure(command=self.apertou_botao21)

        self.botão22 = tk.Button(self.window)
        self.botão22.grid(row=2, column=2, sticky="nsew")
        self.botão22.configure(command=self.apertou_botao22)
                
        self.botão30 = tk.Button(self.window)
        self.botão30.grid(row=3, column=0, sticky="nsew", columnspan=3)
        self.botão30.configure(text="Jogador: X")
        self.botão30.configure(command=self.apertou_botao30)


        
    def iniciar(self):
        self.window.mainloop()

    def arruma_jogador(self):
        if self.jogo_tabuleiro.jogador == 1:
            self.botão30.configure(text="Jogador: X")
        else:
            self.botão30.configure(text="Jogador: O")
            
    def apertou_botao30(self):
        self.jogo_tabuleiro.limpa_jogadas()
        self.botão00.configure(text="")
        self.botão01.configure(text="")
        self.botão02.configure(text="")
        self.botão10.configure(text="")
        self.botão11.configure(text="")        
        self.botão12.configure(text="")
        self.botão20.configure(text="")
        self.botão21.configure(text="")
        self.botão22.configure(text="")        
        self.botão30.configure(text="Jogador: X")
        
    def apertou_botao00(self):
                
            if self.jogo_tabuleiro.jogador == 1:
                self.botão00.configure(text="X")
            else:
                self.botão00.configure(text="O")

            self.jogo_tabuleiro.recebe_jogada(0,0)        
        
            self.arruma_jogador()        
        
            if self.jogo_tabuleiro.verifica_ganhador() == 1:
                self.botão30.configure(text="O Jogador X é vitorioso (aperte aqui para resetar)")
            elif self.jogo_tabuleiro.verifica_ganhador() == 2:
                self.botão30.configure(text="O Jogador O é vitorioso (aperte aqui para resetar)")
            elif self.jogo_tabuleiro.verifica_ganhador() == 0:
                self.botão30.configure(text="Deu velha (aperte aqui para resetar)")
        
    def apertou_botao01(self):
            if self.jogo_tabuleiro.jogador == 1:
                self.botão01.configure(text="X")
            else:
                self.botão01.configure(text="O")

            self.jogo_tabuleiro.recebe_jogada(0,1)        
        
            self.arruma_jogador()        
        
            if self.jogo_tabuleiro.verifica_ganhador() == 1:
                self.botão30.configure(text="O Jogador X é vitorioso (aperte aqui para resetar)")
            elif self.jogo_tabuleiro.verifica_ganhador() == 2:
                self.botão30.configure(text="O Jogador O é vitorioso (aperte aqui para resetar)")
            elif self.jogo_tabuleiro.verifica_ganhador() == 0:
                self.botão30.configure(text="Deu velha (aperte aqui para resetar)")
             
        
    def apertou_botao02(self):
            if self.jogo_tabuleiro.jogador == 1:
                self.botão02.configure(text="X")
            else:
                self.botão02.configure(text="O")

            self.jogo_tabuleiro.recebe_jogada(0,2)        
        
            self.arruma_jogador()        
        
            if self.jogo_tabuleiro.verifica_ganhador() == 1:
                self.botão30.configure(text="O Jogador X é vitorioso (aperte aqui para resetar)")
            elif self.jogo_tabuleiro.verifica_ganhador() == 2:
                self.botão30.configure(text="O Jogador O é vitorioso (aperte aqui para resetar)")
            elif self.jogo_tabuleiro.verifica_ganhador() == 0:
                self.botão30.configure(text="Deu velha (aperte aqui para resetar)")
             
        
    def apertou_botao10(self):
            if self.jogo_tabuleiro.jogador == 1:
                self.botão10.configure(text="X")
            else:
                self.botão10.configure(text="O")

            self.jogo_tabuleiro.recebe_jogada(1,0)        
        
            self.arruma_jogador()        
        
            if self.jogo_tabuleiro.verifica_ganhador() == 1:
                self.botão30.configure(text="O Jogador X é vitorioso (aperte aqui para resetar)")
            elif self.jogo_tabuleiro.verifica_ganhador() == 2:
                self.botão30.configure(text="O Jogador O é vitorioso (aperte aqui para resetar)")
            elif self.jogo_tabuleiro.verifica_ganhador() == 0:
                self.botão30.configure(text="Deu velha (aperte aqui para resetar)")
             
        
    def apertou_botao11(self):
            if self.jogo_tabuleiro.jogador == 1:
                self.botão11.configure(text="X")
            else:
                self.botão11.configure(text="O")

            self.jogo_tabuleiro.recebe_jogada(1,1)        
        
            self.arruma_jogador()        
        
            if self.jogo_tabuleiro.verifica_ganhador() == 1:
                self.botão30.configure(text="O Jogador X é vitorioso (aperte aqui para resetar)")
            elif self.jogo_tabuleiro.verifica_ganhador() == 2:
                self.botão30.configure(text="O Jogador O é vitorioso (aperte aqui para resetar)")
            elif self.jogo_tabuleiro.verifica_ganhador() == 0:
                self.botão30.configure(text="Deu velha (aperte aqui para resetar)")
             

    def apertou_botao12(self):
            if self.jogo_tabuleiro.jogador == 1:
                self.botão12.configure(text="X")
            else:
                self.botão12.configure(text="O")

            self.jogo_tabuleiro.recebe_jogada(1,2)        
        
            self.arruma_jogador()        
        
            if self.jogo_tabuleiro.verifica_ganhador() == 1:
                self.botão30.configure(text="O Jogador X é vitorioso (aperte aqui para resetar)")
            elif self.jogo_tabuleiro.verifica_ganhador() == 2:
                self.botão30.configure(text="O Jogador O é vitorioso (aperte aqui para resetar)")
            elif self.jogo_tabuleiro.verifica_ganhador() == 0:
                self.botão30.configure(text="Deu velha (aperte aqui para resetar)")

    def apertou_botao20(self):
            if self.jogo_tabuleiro.jogador == 1:
                self.botão20.configure(text="X")
            else:
                self.botão20.configure(text="O")

            self.jogo_tabuleiro.recebe_jogada(2,0)        
        
            self.arruma_jogador()        
        
            if self.jogo_tabuleiro.verifica_ganhador() == 1:
                self.botão30.configure(text="O Jogador X é vitorioso (aperte aqui para resetar)")
            elif self.jogo_tabuleiro.verifica_ganhador() == 2:
                self.botão30.configure(text="O Jogador O é vitorioso (aperte aqui para resetar)")
            elif self.jogo_tabuleiro.verifica_ganhador() == 0:
                self.botão30.configure(text="Deu velha (aperte aqui para resetar)")
             

    def apertou_botao21(self):
            if self.jogo_tabuleiro.jogador == 1:
                self.botão21.configure(text="X")
            else:
                self.botão21.configure(text="O")

            self.jogo_tabuleiro.recebe_jogada(2,1)        
        
            self.arruma_jogador()        
        
            if self.jogo_tabuleiro.verifica_ganhador() == 1:
                self.botão30.configure(text="O Jogador X é vitorioso (aperte aqui para resetar)")
            elif self.jogo_tabuleiro.verifica_ganhador() == 2:
                self.botão30.configure(text="O Jogador O é vitorioso (aperte aqui para resetar)")
            elif self.jogo_tabuleiro.verifica_ganhador() == 0:
                self.botão30.configure(text="Deu velha (aperte aqui para resetar)")

    def apertou_botao22(self):
            if self.jogo_tabuleiro.jogador == 1:
                self.botão22.configure(text="X")
            else:
                self.botão22.configure(text="O")

            self.jogo_tabuleiro.recebe_jogada(2,2)        
        
            self.arruma_jogador()        
        
            if self.jogo_tabuleiro.verifica_ganhador() == 1:
                self.botão30.configure(text="O Jogador X é vitorioso (aperte aqui para resetar)")
            elif self.jogo_tabuleiro.verifica_ganhador() == 2:
                self.botão30.configure(text="O Jogador O é vitorioso (aperte aqui para resetar)")
            elif self.jogo_tabuleiro.verifica_ganhador() == 0:
                self.botão30.configure(text="Deu velha (aperte aqui para resetar)")
             
        
app = Tabuleiro()
app.iniciar()


        
                
