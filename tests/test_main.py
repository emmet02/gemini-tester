from src.main import greet


def test_greet():
    assert greet("World") == "Hello, World!"
    assert greet("Gemini") == "Hello, Gemini!"
