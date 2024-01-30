# QUESTION 1

"""
notes:
robot droid thing deliver packages (avoid abstacles)
+50 points 1 package delivered
-10 points collision obstacle
+bonus 500 points if delivery > collisions
determine final score!!!
"""
import time

P = int(input(""))
C = int(input(""))

start_time = time.time()

score = P*50 - C*10
if P > C:
    score = score + 500

print(score)

print("my program took", time.time() - start_time, "to run :)")