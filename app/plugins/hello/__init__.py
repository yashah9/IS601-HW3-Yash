from app.commands import Command

class HelloCommand(Command):
    def execute(self):
        print("Hello")