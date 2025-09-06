def render(exc_type, exc_value):
    jokes = {
        "ZeroDivisionError": "Divide by zero again? Math teachers everywhere are crying.",
        "ValueError": "Tried turning nonsense into a number? Brilliant plan."
    }
    joke = jokes.get(exc_type.__name__, "Wow, you really broke it this time.")
    return f"{exc_type.__name__}: {exc_value}\n→ {joke}"
