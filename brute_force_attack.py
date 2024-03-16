import string
import itertools
import time


# Function to simulate a Brute Force attack in the main app

def bruteForceAttack(password):
    chars = string.ascii_letters + string.punctuation + string.digits
    attempts = 0
    start_time = time.time()
    timeout = 30  # Timelimit for the checkSecurity func in main app
    for i in range(1, len(password) + 1):
        for guess in itertools.product(chars, repeat=i):  # itertools.product creates all possible combinations
            attempts += 1
            guess = ''.join(guess)
            if guess == password:
                return attempts, guess
            if time.time() - start_time > timeout:
                return attempts, None
    return attempts, None
