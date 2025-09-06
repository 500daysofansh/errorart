import sys
from . import ascii_art, haiku, sarcasm

MODE = "ascii"

def set_mode(mode: str):
    """Set the ErrorArt mode (ascii, haiku, sarcasm)."""
    global MODE
    if mode in ["ascii", "haiku", "sarcasm"]:
        MODE = mode
    else:
        MODE = "ascii"

def error_handler(exc_type, exc_value, exc_traceback):
    if MODE == "ascii":
        msg = ascii_art.render(exc_type, exc_value)
    elif MODE == "haiku":
        msg = haiku.render(exc_type, exc_value)
    elif MODE == "sarcasm":
        msg = sarcasm.render(exc_type, exc_value)
    else:
        msg = f"{exc_type.__name__}: {exc_value}"
    print("\n=== ErrorArt ===\n" + msg)

# Override Python's default exception hook
sys.excepthook = error_handler
