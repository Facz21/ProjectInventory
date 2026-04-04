# Import system modules
import os
import time


# SCREEN UTILITIES

def clear_screen():
    """
    Clears the terminal screen based on the operating system.

    Uses:
    - 'cls' for Windows systems
    - 'clear' for Linux/macOS systems

    This improves user experience by keeping the interface clean
    during program execution.
    """
    
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # Linux / macOS
        os.system("clear")


# TIME UTILITIES

def pause(seconds):
    """
    Pauses the program execution for a given number of seconds.

    Args:
        seconds (int | float): Duration of the pause in seconds

    Useful for giving the user time to read output before continuing.
    """
    
    time.sleep(seconds)


# ALIASES

# Short aliases to simplify function calls in other modules
# Example: instead of clear_screen() → cs()
cs = clear_screen
p = pause