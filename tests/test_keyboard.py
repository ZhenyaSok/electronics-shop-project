from src import keyboard


def test_keyboard():
    kb = keyboard.Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"
    assert str(kb.language) == "EN"

    kb.change_lang()
    assert str(kb.language) == "RU"

    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"

