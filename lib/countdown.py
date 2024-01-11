def countdown(start_number):
    while start_number > 0:
        print(f"{start_number} SECOND(S)!")
        start_number -= 1
        
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(start_number):
    while start_number > 0:
        print(f"{start_number} SECOND(S)!")
        start_number -= 1
        # No time.sleep() in this version
    
    print("HAPPY NEW YEAR!")

# Example usage:
countdown(5)  # Replace 5 with your desired starting number
countdown_with_sleep(5)  # Replace 5 with your desired starting number
