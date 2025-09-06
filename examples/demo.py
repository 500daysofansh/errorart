import errorart

# choose error art style
errorart.set_mode("haiku")  # ascii / haiku / sarcasm

print("Triggering errors to test ErrorArt...\n")

# Trigger ZeroDivisionError
print(1 / 0)

# Trigger ValueError
num = int("oops")

# Trigger KeyError
d = {}
print(d["missing"])
