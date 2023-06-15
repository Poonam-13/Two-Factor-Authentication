import random

def generate_verification_code():
    """Generates a random 6-digit verification code."""
    return str(random.randint(100000, 999999))

def send_verification_code(user):
    """Simulates sending the verification code to the user (e.g., via email or SMS)."""
    verification_code = generate_verification_code()
    print(f"Sending verification code {verification_code} to {user}...")

def authenticate_user():
    """Authenticates the user using two-factor authentication."""
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Simulate verifying username and password
    if username == "example_user" and password == "example_password":
        send_verification_code(username)
        verification_code = input("Enter the verification code: ")

        # Simulate verifying the verification code
        if verification_code == generate_verification_code():
            print("Authentication successful!")
        else:
            print("Authentication failed. Invalid verification code.")
    else:
        print("Authentication failed. Invalid username or password.")

# Usage
authenticate_user()
