# List of uppercase and lowercase letters
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
           "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Corresponding points for each letter
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10,
          1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Using a list comprehension and zip, create a dictionary called letter_to_points
# that maps the elements of letters as the keys and the elements of points as the values.
letter_to_points = {key:value for key, value in zip(letters, points)}

# Add an element to the letter_to_points dictionary that has a key of " " and a point value of 0.
letter_to_points[" "] = 0

# Define a function called score_word that takes in a parameter word.
# This function calculates the total points for the given word.
def score_word(word):
  point_total = 0
  # Iterate through each letter in the word
  for letter in word:
    # Add the point value of the letter to point_total
    point_total += letter_to_points.get(letter, 0)
  return point_total

# Test the score_word function with the word "BROWNIE"
# brownie_points = score_word('BROWNIE')
# print(brownie_points)

# Create a dictionary called player_to_words that maps players to a list of the words they have played.
# Create a dictionary called player_to_words that maps players to a list of the words they have played.
player_to_words = {
  'player1': ['BLUE', 'TENNIS', 'EXIT'],
  'wordNerd': ['EARTH', 'EYES', 'MACHINE'],
  'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'],
  'Prof Reader': ['ZAP', 'COMA', 'PERIOD']
}

# Check the player_to_words dictionary
# print(player_to_words)

# Create an empty dictionary called player_to_points to store the total points for each player
player_to_points = {}

# Iterate through each player and their list of words in the player_to_words dictionary
for player, words in player_to_words.items():
  # Initialize player_points to 0 for each player
  player_points = 0
  # Iterate through each word in the player's list of words
  for word in words:
    # Add the points for the word to player_points
    player_points += score_word(word)
  # After calculating the total points, add the player and their points to the player_to_points dictionary
  player_to_points[player] = player_points

# Print the player_to_points dictionary to see the current standings
print(player_to_points)

# Define a function called play_word that takes in a player and a word
# This function adds the word to the list of words the player has played
def play_word(player, word):
  # Check if the player exists in the player_to_words dictionary
  if player in player_to_words:
    # If the player exists, append the word to their list of words
    player_to_words[player].append(word)
  else:
    # If the player does not exist, create a new entry for the player with the word in a list
    player_to_words[player] = [word]
