import pytest
from string_utils import StringUtils

class TestStringUtils:

    def setup_method(self):
        self.utils = StringUtils()

    # Тесты для метода capitalize
    def test_capitalize_positive(self):
        assert self.utils.capitalize("skypro") == "Skypro"

    def test_capitalize_empty_string(self):
        assert self.utils.capitalize("") == ""

    def test_capitalize_single_char(self):
        assert self.utils.capitalize("a") == "A"

    def test_capitalize_already_capitalized(self):
        assert self.utils.capitalize("Skypro") == "Skypro"

    def test_capitalize_with_spaces(self):
        assert self.utils.capitalize("  hello") == "  hello"

    # Тесты для метода trim
    def test_trim_positive(self):
        assert self.utils.trim("   skypro") == "skypro"

    def test_trim_no_spaces(self):
        assert self.utils.trim("skypro") == "skypro"

    def test_trim_empty_string(self):
        assert self.utils.trim("") == ""

    def test_trim_only_spaces(self):
        assert self.utils.trim("    ") == ""

    def test_trim_multiple_spaces(self):
        assert self.utils.trim("    hello world") == "hello world"

    # Тесты для метода contains
    def test_contains_positive(self):
        assert self.utils.contains("SkyPro", "S") is True

    def test_contains_negative(self):
        assert self.utils.contains("SkyPro", "U") is False

    def test_contains_empty_string(self):
        assert self.utils.contains("", "a") is False

    def test_contains_empty_symbol(self):
        with pytest.raises(ValueError):
            self.utils.contains("test", "")

    def test_contains_substring(self):
        assert self.utils.contains("Hello World", "World") is True

    def test_contains_single_char_string(self):
        assert self.utils.contains("a", "a") is True
        assert self.utils.contains("a", "b") is False

    # Тесты для метода delete_symbol
    def test_delete_symbol_positive(self):
        assert self.utils.delete_symbol("SkyPro", "k") == "SyPro"

    def test_delete_symbol_substring(self):
        assert self.utils.delete_symbol("SkyPro", "Pro") == "Sky"

    def test_delete_symbol_not_found(self):
        assert self.utils.delete_symbol("SkyPro", "X") == "SkyPro"

    def test_delete_symbol_empty_string(self):
        assert self.utils.delete_symbol("", "a") == ""

    def test_delete_symbol_all_chars(self):
        assert self.utils.delete_symbol("aaaa", "a") == ""

    def test_delete_symbol_empty_symbol(self):
        assert self.utils.delete_symbol("test", "") == "test"
