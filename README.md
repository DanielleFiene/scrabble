# Scrabble scorekeeper
Scrabble anyone?


This project is a Scrabble scorekeeper implemented in Python. It uses dictionaries to keep track of players, the words they have played, and their corresponding scores. The project demonstrates the use of Python dictionaries, list comprehensions, and functions.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Further Practice](#further-practice)

## Introduction
This project processes data from a group of friends playing Scrabble. It calculates the total points for each player based on the words they have played. The project also includes a function to add new words for players and update their scores.

## Features
- Calculate the total points for each player based on the words they have played.
- Add new words for players and update their scores.
- Handle both uppercase and lowercase letters for scoring.

## Usage
1. Clone the repository or download the script.
2. Run the script using Python:
   ```bash
   python scrabble.py

The script will print the current standings for the game.

Code Explanation

Dictionaries

letter_to_points: Maps each letter to its corresponding point value.
player_to_words: Maps each player to a list of words they have played.
player_to_points: Maps each player to their total points.

Functions

score_word(word): Takes a word as input and returns the total points for that word.
play_word(player, word): Takes a player and a word as input, adds the word to the player’s list of words, and updates their score.
Example


