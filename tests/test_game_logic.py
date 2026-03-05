from logic_utils import check_guess, reset_game_state

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_guess_too_low2():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 100)
    assert result == "Too Low"


def test_new_game_resets_state():
    state = reset_game_state(1, 100)
    assert state["attempts"] == 0
    assert state["score"] == 0
    assert state["history"] == []
    assert state["status"] == "playing"
    assert state["hint"] is None
    assert 1 <= state["secret"] <= 100