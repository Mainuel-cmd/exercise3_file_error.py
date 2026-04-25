def get_age():
    while True:
        try:
            age = int(input("Enter age: "))
            if age < 0:
                print("Age cannot be negative. Please enter a valid age.")
                continue
            return age
        except ValueError:
            print("Invalid input! Please enter a whole number for age.")

def main():
    try:
        username = input("Enter username: ").strip()
        if not username:
            print("Username cannot be empty.")
            return

        age = get_age()

        with open("users.txt", "a") as f:
            f.write(f"{username} - {age}\n")

        print("User data saved successfully.")

        print("\n--- Saved Users ---")
        with open("users.txt", "r") as f:
            lines = f.readlines()
            if not lines:
                print("No users saved yet.")
            else:
                for line in lines:
                    print(line.strip())

    except PermissionError:
        print("Error: Cannot write to users.txt. Check file permissions or folder access.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("\nSystem complete.")

if __name__ == "__main__":
    main()
