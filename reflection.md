# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

---

- The first time I ran the game, I noticed that the secret number hints were backwards, the attempts counter was mismatched and I couldn't restart the game when I finished a round.
  - For the secret numbers issue, if I entered a number **lower** than the secret, it would give an error message saying "GO LOWER!" and if a number I entered was **higher** than the secret, the error message would say "GO HIGHER!"
    - ![alt text](<Screenshot 2026-03-15 at 3.43.45 PM.jpg>)
    - ![alt text](<Screenshot 2026-03-15 at 3.43.59 PM.jpg>)
  - When I went through the attempts to find the secret, I noticed that if I didn't get any of the attempts correct and I had 1 attempt left, the application would say "Out of attempts!" It should only trigger the message if I have 0 attempts left.
    - ![alt text](<Screenshot 2026-03-15 at 3.43.59 PM-1.jpg>)
  - Even if I successfully got the secret number and it prompted me to try another round, if I clicked the "New game" button, the secret, history and score were not changed; I needed to reload the entire page.

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

- I used Claude, ChatGPT to assist me on the project. Claude would help to understand the logic of how the project runs (what files are needed), ChatGPT was used occasionally as a sort of second opinion to see if there were any differences from Claude's suggestions.
- AI suggestions that were correct were the parts where I was trying to pinpoint areas that the code was bugged. What I would do is that I would note down the bugs I found, and then ask the AI tool where in the app.py file would I find the logic relating to features such as responding to an entered number. The following screenshot is one such example: -![alt text](<Screenshot 2026-03-15 at 3.53.58 PM.jpg>)
  - I didn't completely rely on AI to solve my problems for me. I would pinpoint where in app.py the bug was happening, and in this case, all I needed to do was swap the error messages.
- An AI suggestion that was incorrect/misleading was when I was handling the "new game" button bug. I had left some comments marking a spot for Claude to fix, and it assumed it was just comments noting a bug. What I had to do was to explicitly enter it, but in the chat for Claude to implement meaningful changes.
  - ![alt text](<Screenshot 2026-03-15 at 3.06.39 PM.jpg>)
  - ![alt text](<Screenshot 2026-03-15 at 3.06.43 PM.jpg>)
- Verification:
  - - [x] Properly displays whether guess is too low or high, can start new game (and change difficulty).
    - ![GlitchInvestigator](https://github.com/user-attachments/assets/f0bbe2d6-63bb-485b-b06f-c6614e57833c)

  - [x] The game ends if all attempts are used up instead of stopping at 1 attempt.
    - ![AttemptsDecrement](https://github.com/user-attachments/assets/1f06ce27-9b6f-46e7-8cde-478c484e0977)

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

- I determined that a bug was really fixed in two ways: First, I would try the same conditions that caused me to experience said bug to begin with (the number hint problem I would intentionally enter guesses smaller/higher and see if the messages matched, the start new game bug I would try clicking the start new game button, and the attempts bug I would go through all my guesses and see if the error message would only run if attempts = 0). Also for the changes where applicable, I ran pytest.
- I ran a series of tests on the number guessing bug (screenshot shown below), and they all passed. It shows that my code has considered all possible situations. Additionally, I ran a pytest for the "new game" logic Claude helped to add, the success condition was if the number of attempts were 0, my status was "playing", etc.
  - ![alt text](<Screenshot 2026-03-15 at 3.10.15 PM.jpg>)
  - ![alt text](<Screenshot 2026-03-15 at 3.09.02 PM.jpg>)
- AI helped me understand how to use the pytest command. In addition, AI helped put to code how to return whether or not output I wanted matched output I got.

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

- Every time I interact with a Streamlit app, it reruns the entire script from top to bottom. If random.randint() was called at the top level, it generated a brand new number on every rerun. So each button click or keystroke would silently replace the secret the player was trying to guess.
- Streamlit is like a whiteboard that gets erased and redrawn whenever someone touches it. Session state is a sticky note that keeps track of important information that need to survive being erased. So when I write the secret to st.session_state, it will stay there across reruns so the app can remember important variables.
- The solution was to only generate the secret number once by checking if it already exists in st.session_state before creating it (this is relevant to if I press the "reload" button, will generate a new secret). Something like if "secret" not in st.session_state: st.session_state.secret = random.randint(...). After that, every rerun reads the stored value instead of rolling a new one.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
    - I would like to reuse the habit of first pinpointing the code of projects I work on, that way I can understand the workflow, add test debugs, which would help to understand the cause of the bug better.
    - I should always provide context to the AI, it doesn't understand my thought process or intentions.
    - Check in in study hall more.
- What is one thing you would do differently next time you work with AI on a coding task?
  - Try to make my first response have as much context and be as direct and concise as possible. Otherwise if I make a mistake the first time it would be a hassle to check what was changed and what to undo. I should also put the problems I have across different chat sessions, because I have noticed (not specifically in this project but previous times I've used AI for problem-solving) occasions where the agent mistakenly thinks my question is in the context of a previous question.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - AI generated code isn't a be all end all, having another perspective and testing it is always preferable in order to spot any potential mistakes in the response or just to verify.
