import time

MIN_BRIGHTNESS = 0
MAX_BRIGHTNESS = 100
STEP_SIZE = 5  # Step size to increase or decrease brightness


current_brightness = 100 # Default starting brightness


def print_brightness_bar(brightness):
    bar = "█" * (brightness // 2)  
    spaces = " " * (50 - len(bar))
    print(f"[{bar}{spaces}] {brightness}%")

# Function to display instructions
def print_instructions():
    print("\nInstructions:")
    print("1. Type 'increase' to increase brightness.")
    print("2. Type 'decrease' to decrease brightness.")
    print("3. Type 'exit' to exit the program.")
    print("4. Brightness will be adjusted in steps of 5%.")
    print("5. The range of brightness is from 0% to 100%.")


while True:
    # Print the current brightness bar
    print_brightness_bar(current_brightness)
    
    # Ask for user input (command)
    print_instructions()
    command = input("Enter a command: ").strip().lower()

    if command == "increase":
        if current_brightness + STEP_SIZE <= MAX_BRIGHTNESS:
            current_brightness += STEP_SIZE
            print(f"Brightness increased by {STEP_SIZE}%")
        else:
            print(f"Cannot increase brightness above {MAX_BRIGHTNESS}%")

    elif command == "decrease":
        if current_brightness - STEP_SIZE >= MIN_BRIGHTNESS:
            current_brightness -= STEP_SIZE
            print(f"Brightness decreased by {STEP_SIZE}%")
        else:
            print(f"Cannot decrease brightness below {MIN_BRIGHTNESS}%")

    elif command == "exit":
        print("Exiting the program...")
        break  # Exit the loop

    elif command == "help":
        print_instructions()

    else:
        print("Invalid command. Please enter 'increase', 'decrease', or 'exit'.")
    
    # Wait a moment before prompting again
    time.sleep(1)
