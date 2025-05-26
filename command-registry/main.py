"""
In this example i asked AI for some programming challanges.
This one dives deep into Python internals and dynamic registry of commands.

This module consists of mainly 3 parts:

1. Command contract/interface
2. Command registry
3. Actual commands.

Commands are constrained by forcing a run() method.
The commands are run through the CommandRegistry via CommandRegistry.run()
which means that it has to be a classmethod.

To handle autoregistry of commands, we invoke a CommandMeta (metaclass via ABCMeta).
We invoke this for every newly created command, which eliminates the need for
explicit registry methods in each Command-type class.

AI suggested that we use a Greet and Add class as an example, but usage
is not limited to this.
"""

from abc import ABC, abstractmethod, ABCMeta


class Command(ABC):
    """This contract makes sure that every Command-type class has at least a .run() method."""
    @abstractmethod
    def run(self):
        pass


class CommandRegistry:
    """
    The CommandRegistry stores all defined commands in _commands.
    When instantiated, we provide methods for running commands via the CommandRegistry.
    The register() method is invoked via Metaclasses further down the chains,
    where the Metaclass (ABCMeta, since we go for ABC for Commands) uses
    CommandRegistry for registration.
    """
    _commands = {}

    @classmethod
    def register(cls, name: str, command):
        """Registers commands. Strings for the key, command class for value."""
        cls._commands[name] = command

    @classmethod
    def run(cls, command_name, **kwargs):
        """
        Run method for running classes stored in _commands. Checks if commands exist in
        the registry and raises a ValueError if not found. If found, runs the native
        run() method for the class stored inside _commands.
        """
        if command_name not in cls._commands:
            raise ValueError("Command not in registry")
        return cls._commands[command_name](**kwargs).run()


class CommandMeta(ABCMeta):
    """
    This Metaclass handles autoregistration of commands. It is invoked when a new BaseCommand-type
    class is created. It takes in the class name and all its arguments and then
    sends both the Class name and the class to the Classregistry.
    """
    def __new__(mcs, class_name, bases, dct):
        cls = super().__new__(mcs, class_name, bases, dct)
        if class_name != "BaseCommand":
            CommandRegistry.register(class_name.lower(), cls)
        return cls


class BaseCommand(Command, metaclass=CommandMeta):
    """
    This is the base for all Command classes. It combines both the Command ABC
    and the CommandMeta. That means that we enforce behavior of each class to
    have a run() method and also makes sure that every class can autoregister
    via the internals worked on in CommandMeta.

    This should be implemented by all Command-type classes if you need both
    autoregistering and to be a Command-type class.
    """
    pass


class Greet(BaseCommand):
    """Simple Greet Command class."""
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f"Hello, {self.name}")


class Add(BaseCommand):
    """Simple Add Command class for adding numbers."""
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def run(self):
        print(f"Sum of {self.a} and {self.b} is { self.a + self.b }")


if __name__ == "__main__":
    CommandRegistry.run("greet", name="Alice")
    CommandRegistry.run("add", a= 2.5, b=3)
