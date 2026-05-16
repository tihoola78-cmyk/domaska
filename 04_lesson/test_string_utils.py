import pytest
from string_utils import StringUtils

utils = StringUtils()


# ---------- Позитивные тесты для capitalize ----------
class TestCapitalizePositive:
    def test_capitalize_standard_string(self):
        assert utils.capitalize("skypro") == "Skypro"

    def test_capitalize_one_word_lower(self):
        assert utils.capitalize("hello") == "Hello"

    def test_capitalize_one_word_upper(self):
        assert utils.capitalize("HELLO") == "Hello"

    def test_capitalize_with_numbers(self):
        assert utils.capitalize("123abc") == "123abc"

    def test_capitalize_with_russian_letters(self):
        assert utils.capitalize("привет") == "Привет"


# ---------- Негативные тесты для capitalize ----------
class TestCapitalizeNegative:
    def test_capitalize_empty_string(self):
        assert utils.capitalize("") == ""

    def test_capitalize_string_with_space(self):
        assert utils.capitalize(" ") == " "

    def test_capitalize_with_none(self):
        with pytest.raises(AttributeError):
            utils.capitalize(None)


# ---------- Позитивные тесты для trim ----------
class TestTrimPositive:
    def test_trim_one_space(self):
        assert utils.trim(" skypro") == "skypro"

    def test_trim_two_spaces(self):
        assert utils.trim("  skypro") == "skypro"

    def test_trim_tabs(self):
        assert utils.trim("\tskypro") == "skypro"

    def test_trim_no_spaces(self):
        assert utils.trim("skypro") == "skypro"

    def test_trim_spaces_inside(self):
        assert utils.trim("sky pro") == "sky pro"


# ---------- Негативные тесты для trim ----------
class TestTrimNegative:
    def test_trim_empty_string(self):
        assert utils.trim("") == ""

    def test_trim_string_with_only_spaces(self):
        assert utils.trim("   ") == ""

    def test_trim_with_none(self):
        with pytest.raises(AttributeError):
            utils.trim(None)


# ---------- Позитивные тесты для contains ----------
class TestContainsPositive:
    def test_contains_symbol_in_string(self):
        assert utils.contains("Skypro", "k") is True

    def test_contains_symbol_at_begin(self):
        assert utils.contains("Skypro", "S") is True

    def test_contains_symbol_at_end(self):
        assert utils.contains("Skypro", "o") is True

    def test_contains_numbers(self):
        assert utils.contains("12345", "3") is True


# ---------- Негативные тесты для contains ----------
class TestContainsNegative:
    def test_contains_symbol_not_in_string(self):
        assert utils.contains("Skypro", "z") is False

    def test_contains_with_empty_string(self):
        assert utils.contains("", "a") is False

    def test_contains_with_empty_symbol(self):
        assert utils.contains("Skypro", "") is True

    def test_contains_with_none_string(self):
        with pytest.raises(TypeError):
            utils.contains(None, "a")