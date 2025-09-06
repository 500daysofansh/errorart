import pytest
import errorart

def test_set_mode():
    errorart.set_mode("ascii")
    assert errorart.core.MODE == "ascii"
    errorart.set_mode("haiku")
    assert errorart.core.MODE == "haiku"
