# Task 6 — Decorator Pattern (Object-oriented, NOT
# @syntax)
# 
# Instructions
# 1. Create a class Writer with a method write(message) that prints the message
# as-is.
# 
# 2. Create a decorator class TimestampedWriter that:
#    Accepts a Writer (or another decorator) instance
#    Its write(message) method must:
#       1. Print the current time (HH:MM format)
#       2. Call the wrapped writer’s write method
# 3. Create a second decorator class StarredWriter that:
#   Wraps any writer
#   Surrounds the message with *** before delegating
# 4. Demonstrate decorator stacking, e.g.:
#       w = StarredWriter(TimestampedWriter(Writer()))
#       w.write("hello")
from datetime import datetime
from typing import Protocol

class Writer:
    def write(self, message: str) -> None:
        print(message)

class WriterProtocol(Protocol):
    def write(self, message: str) -> None: ...

class TimestampedWriter:
    def __init__(self, writer: WriterProtocol) -> None:
        self._writer = writer
    def write(self, message: str) -> None:
        current_time = datetime.now().strftime("%H:%M")
        print(f"[{current_time}] ", end="")
        self._writer.write(message)

class StarredWriter:
    def __init__(self, writer: WriterProtocol) -> None:
        self._writer = writer
    def write(self, message: str) -> None:
        starred_message = f"*** {message} ***"
        self._writer.write(starred_message)
# Example usage
if __name__ == "__main__":
    w = StarredWriter(TimestampedWriter(Writer()))
    w.write("hello")
   