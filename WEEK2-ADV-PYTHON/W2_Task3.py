# Task 3 — Simple Inheritance & Polymorphism
# Instructions
# 1. Create a base class Message.
# ○ It must have a method format(text) that returns the text unchanged.
# 2. Create two subclasses:
# ○ UppercaseMessage that returns the text in uppercase
# ○ SurroundMessage that returns the text surrounded by ### (e.g.
###hello###)
# 3. Create a list with instances of all three classes.
# 4. Loop through the list and print the formatted output of each using the same method
# call.
class Message:
    def format(self, text):
        return text
class UppercaseMessage(Message):
    def format(self, text):
        return text.upper()
class SurroundMessage(Message):
    def format(self, text):
        return f"###{text}###"
# Example usage
if __name__ == "__main__":
    messages = [
        Message(),
        UppercaseMessage(),
        SurroundMessage()
    ]
    text = "hello"
    for msg in messages:
        print(msg.format(text))
