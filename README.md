# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: _"How do I keep a variable from resetting in Streamlit when I click a button?"_
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
  - The game's purpose was to learn how to cooperate with AI rather than rely on it. The tool I used for this project was Claude.
  - To cooperate with Claude, I would conduct some tests on the game, doing observations on any bugs that I found, comparing it to what the game should actually do, listing it down and getting screenshots.
  - Then, I would consult the AI, giving the sceenshots and explaining my situation and narrowing down which file and which line the code was located.
  -
- [x] Detail which bugs you found.
  - When I enter a guess lower than the secret, it would say that the guess was "too high", and when I enter a guess higher than the secret, it would say the guess was "too low".
  - When I completed a game and clicked "new game", it does not start the new game. The attempts aren't reset, the secret isn't, and I can't submit any new guesses. It relies on me to reload the entire page.On a related note, when I change difficulty it doesn't change the ranges/secret to fit within the range.
  - "Off by 1" bug: The game ends if the number of attempts displayed is 1, saying I am out of attempts.
- [x] Explain what fixes you applied.
  - [x] Hints were backwards (line 37-41)
    - The original code returned "Go LOWER" when the guess was too low, and "Go HIGHER" when too high — the opposite of correct. Fix: swapped the messages so guess > secret returns "Go LOWER" and guess < secret returns "Go HIGHER". Verified by running test_guess_too_high() and test_guess_too_low() in pytest. -[X] Reset attempts, secret. (line 146-149)
  - [x] The "New Game" button had random.randint(1, 100) hardcoded, so clicking it always picked a secret from 1–100 even if you were playing on Easy (1–20). The difficulty setting was ignored entirely on reset. Fix: extracted the reset logic into reset_game_state(low, high) in logic_utils.py so the correct range is passed in, then called it from the button handler in app.py. Verified with test_new_game_resets_state() in pytest — it asserts 1 <= state["secret"] <= 100 for a given range, and the same pattern confirms the range is respected. Also verified manually by switching to Easy and pressing New Game, then checking the Developer Debug Info panel to confirm the secret stayed within 1–20.
  - [x] Bug: Game ended one attempt too early (line 196) - The original code used > instead of >= on the attempt limit check: if st.session_state.attempts > attempt_limit: - If st.session_state.attempts >= attempt_limit:
        With >, after your 8th guess on Normal difficulty, attempts equaled 8 and attempt_limit was 8 — so 8 > 8 is False, and the game kept going. You got a free 9th guess before it finally ended. Changing to >= makes 8 >= 8 evaluate to True, ending the game exactly when the last allowed attempt is used. Verified by playing through all 8 attempts on Normal and confirming the game ended on guess 8, not guess 9. - Lines 203 and 205 I added rerun to process the attempts being changed.

## 📸 Demo

- [X] [Insert a screenshot of your fixed, winning game here]
- [X] Properly displays whether guess is too low or high, can toggle difficulty range, and can reset the game. 
   -  ![GlitchInvestigator](https://github.com/user-attachments/assets/f0bbe2d6-63bb-485b-b06f-c6614e57833c)

- [X] The game ends if all attempts are used up instead of stopping at 1 attempt.
   -      ![AttemptsDecrement](https://github.com/user-attachments/assets/bdd04aad-569d-45b9-bb60-dd378dcf989e)



## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
