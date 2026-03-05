def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    # raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    # raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
    if(type(raw) == int):
         return raw 
    else: 
        return None, None, "Invalid input: Please enter a number."


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
    if(int(guess) == secret):
        return "Win"
    elif(int(guess) > secret):
            return "Too High"
    else: 
         return "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")

def reset_game_state(low: int, high: int) -> dict:
    """Return a fresh game state dict."""
    import random
    return {
        "attempts": 0,
        "secret": random.randint(low, high),
        "score": 0,
        "history": [],
        "status": "playing",
        "hint": None,
    }