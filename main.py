# ScoreKeeper class is imported to make use of its functions which count the score and display it
from scorekeeper import ScoreKeeper

# player_1 is created as an instance of the ScoreKeeper class, and user is asked to enter a word
player_1 = ScoreKeeper(input("Please enter a word: "))
# score_count() function from parent class ScoreKeeper calculates the score
player_1.score_count()
# display_score() function from ScoreKeeper displays the score in a user friendly manner
player_1.display_score()

