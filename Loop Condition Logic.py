# Objective:
# The aim of this assignment is to explore the importance of the loop condition in while loops. 
# You will create loops with different conditions to see how they influence the behavior of the loop.
# Task 1: Loop Condition Exploration
# Write a while loop with a condition that will never be false (an infinite loop). 
# Inside the loop, print a statement. 
# Then, use a break statement to exit the loop after 5 iterations.


i = 0
while True:
    print("This is an infinite loop.")
    i += 1
    if i == 5:
        break

# Task 2: Conditional Exit
# Modify the infinite loop from Task 1 to include a condition that will eventually be true and remove the break statement. 
# The loop should terminate naturally once the condition is met.   

i = 0
while i < 5:
    print("This is a loop that will terminate naturally.")
    i += 1
    
    
    