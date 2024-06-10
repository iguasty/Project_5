import pytest
from main import number_found

def test_number_found():
    """Tests if values are being read correctly"""
    assert number_found("123", "123") == True
    assert number_found("456", "123") == False
    assert number_found("0", "0") == True
    assert number_found("", "87") == False


if __name__ == "__main__":
    pytest.main()
