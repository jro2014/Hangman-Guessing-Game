# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 09:58:22 2021

@author: JRO20
"""
# Saved a list of words from 'https://github.com/Xethron/Hangman/blob/master/words.txt'
#Open the file and save the words as a list to be used in the Hangman File
with open('words.txt') as f:
    WordList = f.read().split()
