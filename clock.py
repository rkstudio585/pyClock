import time
import pyfiglet
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def display_clock():
    try:
        while True:
            # Get the current time
            current_time = time.strftime("%H : %M : %S")
            
            # Create ASCII art for the current time using pyfiglet
            ascii_time = pyfiglet.figlet_format(current_time, font="big")

            # Wrap the ASCII time in a rich panel for styling
            clock_panel = Panel(Text(ascii_time, justify="center"), title="🕰 Real-Time Clock by RK 🕰", border_style="bold green")

            # Clear the console and display the updated clock
            console.clear()
            console.print(clock_panel)
            
            # Pause for a second before updating
            time.sleep(1)

    except KeyboardInterrupt:
        console.print("Clock stopped.", style="bold red")

# Run the real-time clock display
display_clock()
