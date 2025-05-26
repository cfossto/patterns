import java.util.Map;
import java.util.HashMap;
import java.lang.Override;

public class Main {

    public static void main(String[] args) {

        // Create a GreetCommand and run it via the CommandRegistry.
        // As you can see, registration happens out of sight.
        new GreetCommand("greeter");
        CommandRegistry.run("greeter");

    }
}




// Define Command. Must have .run() method.
interface Command {
    void run();
}


// Command registry to hold all commands.
class CommandRegistry {

    // This map holds the name of the command and the command class.
    private static Map<String, Command> registry = new HashMap<>();

    // Registers it as CommandRegistry.register().
    public static void register(String command_name, Command command){
        registry.put(command_name, command);
    }

    // Lets you run the command from the CommandRegistry.run()
    public static void run(String command_name){
        Command command = registry.get(command_name);
        if (command_name == null){
            throw new RuntimeException("This is an illegal move!");
        }
        // Runs the command that is called.
        command.run();
    }
}


// A simple Greeter command, but could be any command.
// Implements Command.
class GreetCommand implements Command {

    // Command name
    private final String name;

    // Public constructor. Autoregisters on initialization.
    public GreetCommand(String command_name){
        this.name = command_name;
        CommandRegistry.register(this.name, this);
    }


    @Override
    public void run() {
        System.out.println(this.name);
    }
}


