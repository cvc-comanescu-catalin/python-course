# Assignment 2: Number Guessing Game 🎮

## 🎯 Objective

Build an interactive number guessing game that uses loops, conditionals, and the `random` module. This assignment practices control flow, while loops, if/elif/else, and user input validation.

---

## 📋 Requirements

### Part 1 — Generate a Secret Number
- Use `import random` at the top of your file
- Generate a **random integer between 1 and 100** (inclusive)
- The user should NOT see this number

```python
import random
secret_number = random.randint(1, 100)
```

### Part 2 — Game Loop
- Use a `while` loop to keep asking for guesses until the player is correct
- Each iteration: read the user's guess, convert to int, and compare

### Part 3 — Give Hints
After each incorrect guess, tell the player:
- **"Too high! Try a lower number."** if the guess is above the secret
- **"Too low! Try a higher number."** if the guess is below the secret

### Part 4 — Count Attempts
- Keep a counter that increments with each guess
- When the player guesses correctly, display:

```
🎉 Correct! The number was 42. You guessed it in 5 attempts!
```

---

## ⭐ Bonus / Stretch Goals

### Bonus 1 — Maximum Attempts
Add a limit: if the player exceeds **10 attempts** without guessing correctly:
```
❌ Game over! You've used all 10 attempts. The number was 42.
```

### Bonus 2 — Difficulty Levels
Before the game starts, ask the player to choose:
```
Choose difficulty:
1. Easy   (1–50)
2. Medium (1–100)
3. Hard   (1–500)
```
Adjust the random range based on their choice.

### Bonus 3 — Play Again
After the game ends (win or lose), ask:
```
Play again? (yes/no): 
```
If "yes", start a new game. If "no", print total stats.

---

## 💡 Hints

- `random.randint(a, b)` returns a random integer **inclusive** of both ends
- Use `int(input(...))` to read the guess — but be careful if the user types a non-number!
- The game loop pattern:
  ```python
  while True:
      guess = int(input("Your guess: "))
      if guess == secret:
          print("Correct!")
          break
      elif guess > secret:
          print("Too high!")
      else:
          print("Too low!")
  ```
- For the maximum attempts bonus, add an `attempts` counter and check it in the loop condition

---

## 📟 Example Session

```
🎮 Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

Your guess: 50
Too high! Try a lower number.

Your guess: 25
Too low! Try a higher number.

Your guess: 37
Too high! Try a lower number.

Your guess: 31
Too low! Try a higher number.

Your guess: 34
🎉 Correct! The number was 34. You guessed it in 5 attempts!
```

With difficulty bonus:
```
Choose difficulty:
1. Easy   (1–50)
2. Medium (1–100)
3. Hard   (1–500)
Enter choice (1-3): 2
```

---

## ✅ Checklist

Before submitting, make sure your program:

- [ ] Imports `random` at the top
- [ ] Generates a random number between 1 and 100
- [ ] Asks the user to guess in a loop
- [ ] Prints "Too high!" when the guess is above the secret
- [ ] Prints "Too low!" when the guess is below the secret
- [ ] Counts the number of attempts
- [ ] Prints the success message with attempt count
- [ ] Exits the loop when the guess is correct

**Bonus:**
- [ ] Limits to 10 attempts and reveals the answer on failure
- [ ] Offers difficulty level selection
- [ ] Asks to play again after each game

---

## 📤 Submission Instructions

1. Open `starter-code/assignment2_starter.py`
2. Fill in all the `TODO` sections
3. Test your program — play it a few times to make sure it works
4. Save your completed file as `assignment2_yourname.py`
5. Submit via the course platform or share the GitHub link

---

*💡 Tip: Test edge cases — what happens if the user types a letter instead of a number?*
