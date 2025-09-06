import random

def render(exc_type, exc_value):
    haikus = {
        "ZeroDivisionError": [
            "Divide by nothing,\nThe void consumes your logic,\nNumbers fade away."
        ],
        "ValueError": [
            "Meanings clash badly,\nYour value refused to change,\nTruth stays undefined."
        ]
    }
    haiku = random.choice(haikus.get(exc_type.__name__, [
        "Error came today,\nSilent bug within the code,\nLearn and try again."
    ]))
    return f"{haiku}\n\n({exc_type.__name__}: {exc_value})"
