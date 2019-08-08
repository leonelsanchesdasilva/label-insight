import pytest
import missing_letters

def test_invalid_phrase():
    with pytest.raises(ValueError) as info:
        missing_letters.getMissingLetters(1)
    assert "string value" in str(info.value)

def test_empty_string():
    assert missing_letters.getMissingLetters("") == "abcdefghijklmnopqrstuvwxyz"

def test_pangram():
    assert missing_letters.getMissingLetters("A quick brown fox jumps over the lazy dog") == ""

def test_pseudo_pangram():
    assert missing_letters.getMissingLetters("A slow yellow fox crawls under the proactive dog") == "bjkmqz"

def test_other_example_phrase():
    assert missing_letters.getMissingLetters("Lions, and tigers, and bears, oh my!") == "cfjklpquvwxz"