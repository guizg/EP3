# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 10:01:39 2016

@author: GuilhermeZaborowsky
"""

import numpy as np

class Jogo: # simula um jogo da velha
    
    def __init__(self):
        self.jogador = 1 # 1 = X e 2 = O
        self.rep_tabuleiro = np.zeros([3,3]) # Cria uma matriz de zeros 3x3 que vai representar o tabuleiro do jogo

    def recebe_jogada(self,linha,coluna): # troca o numero na matriz pelo numero do jogador e altera o jogador
        self.rep_tabuleiro[linha][coluna] = self.jogador
        if self.jogador == 1:
            self.jogador = 2
        else:
            self.jogador = 1
            
    def limpa_jogadas(self): # reseta o jogo
        self.rep_tabuleiro = np.zeros([3,3])
        self.jogador = 1
    
    def verifica_ganhador(self): # checa se o jogo acabou. retorna 1 se o jogador 1 ganhar, 2 se o 2 ganhar, 0 se der velha, e -1 se o jogo nao tiver acabado
        for i in range(3): # checa as vitorias de linha inteira
            if self.rep_tabuleiro[i][0] == 1 and self.rep_tabuleiro[i][1]==1 and self.rep_tabuleiro[i][2]==1:
                return 1
            if self.rep_tabuleiro[i][0] == 2 and self.rep_tabuleiro[i][1]==2 and self.rep_tabuleiro[i][2]==2:
                return 2
        for j in range(3): # checa as vitorias de coluna inteira
            if self.rep_tabuleiro[0][j]==1 and self.rep_tabuleiro[1][j]==1 and self.rep_tabuleiro[2][j]==1:
                return 1
            if self.rep_tabuleiro[0][j]==2 and self.rep_tabuleiro[1][j]==2 and self.rep_tabuleiro[2][j]==2:
                return 2
        
        # checa diagonal 1            
        if self.rep_tabuleiro[0][0]==1 and self.rep_tabuleiro[1][1]==1 and self.rep_tabuleiro[2][2]==1:
                return 1
        if self.rep_tabuleiro[0][0]==2 and self.rep_tabuleiro[1][1]==2 and self.rep_tabuleiro[2][2]==2:
                return 2
                
        # checa diagonal 2
        if self.rep_tabuleiro[0][2]==1 and self.rep_tabuleiro[1][1]==1 and self.rep_tabuleiro[2][0]==1:
                return 1
        if self.rep_tabuleiro[0][2]==2 and self.rep_tabuleiro[1][1]==2 and self.rep_tabuleiro[2][0]==2:
                return 2
                
        # Depois de ver se alguem ganhou, ve se o jogo acabou ou nao
        for i in range(3):
            for j in range(3):
                if self.rep_tabuleiro[i][j] == 0:
                    return -1
        # se o jogo acabou e ninguem ganhou, empatou
        return 0
        
        