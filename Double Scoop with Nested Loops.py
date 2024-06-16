# Objective:
# The aim of this assignment is to practice using nested loops in Python. 
# You will correct a nested loop code snippet, simulate a mood tracker, and generate a multiplication table.
# Task 1: Your Mood Tracker
# Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening) for each day of the week. 
# Use nested loops to implement this: the outer loop should iterate over the days, and the inner loop should iterate over the times of the day. 
# For each time, randomly select a mood from a predefined list and print it.
# Example Outcome: An example would be "On Tuesday afternoon you were sad" "On Tuesday night you were happy" "On Wednesday morning you were tired"

mood = ["Happy", "Sad", "Energetic", "Calm", "Angry", "Excited", "Tired"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
times = ["morning", "afternoon", "evening"]

import random

for i in range(7):
    for j in range(3):
        print(f"On {days[i]} {times[j]} you were feeling {random.choice(mood)}.")