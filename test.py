import sys, tty, termios

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

menu = ["Option 1", "Option 2", "Option 3"]

print("Select an option:")
for i, item in enumerate(menu, 1):
    print(f"{i}. {item}")

print("\nPress a number key:")

char = getch()
print(f"\nYou pressed: {char}")
