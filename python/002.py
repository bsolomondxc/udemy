# Health potion game

# Imports section
import random

# Declarations section
int_start_health = 50
int_bonus_health = 0
int_current_health = 0
int_difficulty = 2

# Operations section
if int_difficulty == 1:
    int_bonus_health = random.randint(25,50)
else:
    if int_difficulty == 2:
        int_bonus_health = random.randrange(20,30)
    else:
        int_bonus_health = random.randrange(10,20)

int_current_health = int_start_health + int_bonus_health

#output section
print('Starting health = ', int_start_health)
print('Health bonus    = ', int_bonus_health)
print('New health      = ', int_current_health)