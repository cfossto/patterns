# Command and plugin autoregistry

## Pattern
In this example i asked AI for some programming challanges.
This one dives deep into Python internals and dynamic registry of commands.

This module consists of mainly 3 parts:

1. Command contract/interface
2. Command registry
3. Actual commands.

Commands are constrained by forcing a run() method.
The commands are run through the CommandRegistry via CommandRegistry.run()
which means that it has to be a classmethod in Python.

AI suggested that we use a Greet and Add class as an example, but usage
is not limited to this.

### Python
To handle autoregistry of commands, we invoke a CommandMeta (metaclass via ABCMeta).
We invoke this for every newly created command, which eliminates the need for
explicit registry methods in each Command-type class.
