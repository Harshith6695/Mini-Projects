# ATM PIN Verification Application

correct_pin = "1234"
attempts = 3

while attempts > 0:
    entered_pin = input("Enter your ATM PIN: ")

    if entered_pin == correct_pin:
        print("PIN Verified Successfully")
        print("Welcome to your ATM account!")
        break
    else:
        attempts -= 1
        print("Incorrect PIN")
        print("Attempts left:", attempts)

if attempts == 0:
    print("ATM Card Blocked. Please contact the bank.")
