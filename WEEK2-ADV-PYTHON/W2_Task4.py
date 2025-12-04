# Task 4 — Low Coupling & High Cohesion: Refactoring
# Exercise
# Instructions
# 1. You are given this badly designed class:
# class UserAccount:
# def __init__(self, name):
#     self.name = name
#     self.log = []
# def record(self, action):
#    self.log.append(action)
# def send_email(self, text):
# print("Email:", text)
# def generate_report(self):
 #    print("Report:", self.log)
# 2. Refactor it into at least TWO classes such that:
#   ○ Each class has one clear responsibility
#   ○ No class directly accesses internal details of another
#   ○ You use encapsulation (at least one _attribute)
# 3. Write 3–4 sentences explaining:
#   ○ Which concerns you separated
#   ○ How coupling was reduced
#   ○ How cohesion was increased
class ActivityLog:
    def __init__(self):
        self._log = []

    def record(self, action):
        self._log.append(action)

    def get_log(self):
        return self._log

class EmailService:
    def send_email(self, text):
        print("Email:", text)

class UserAccount:
    def __init__(self, name, email_service, activity_log):
        self.name = name
        self.email_service = email_service
        self.activity_log = activity_log

    def perform_action(self, action):
        self.activity_log.record(action)

    def send_email(self, text):
        self.email_service.send_email(text)

    def generate_report(self):
        print("Report:", self.activity_log.get_log())
# Explanation:
# 1. I separated the concerns of user account management, email sending, and activity logging
#    into three distinct classes: UserAccount, EmailService, and ActivityLog.
# 2. Coupling was reduced by ensuring that UserAccount does not directly access the internal
#    details of EmailService or ActivityLog. Instead, it interacts with them through their
#    public methods.
# 3. Cohesion was increased by ensuring that each class has a single, well-defined
#    responsibility, making the code easier to maintain and understand.
# Example usage
if __name__ == "__main__":
    email_service = EmailService()
    activity_log = ActivityLog()
    user = UserAccount("Alice", email_service, activity_log)
    user.perform_action("Logged in")
    user.send_email("Welcome to our service!")
    user.perform_action("Updated profile")
    user.generate_report()
