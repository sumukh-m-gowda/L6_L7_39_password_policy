def first_character_type(pw):
    # Guard: None / non-string / empty string
    if not isinstance(pw, str) or len(pw) == 0:
        return 'invalid'
    ch = pw[0]
    if ch.isdigit():
        return 'digit'
    if ch.isalpha():
        return 'letter'
    return 'symbol'

def split_credentials(text):
    # Guard: None / non-string
    if not isinstance(text, str):
        return '', ''
    # Split on the FIRST ':' only, so passwords may contain ':'
    if ':' not in text:
        return '', ''          # malformed: no "user:password" separator
    user, password = text.split(':', 1)
    return user.strip(), password.strip()

def digit_ratio(pw):
    # Guard: None / non-string / empty string (avoids ZeroDivisionError)
    if not isinstance(pw, str) or len(pw) == 0:
        return 0.0
    return sum(c.isdigit() for c in pw) / len(pw)

def main():
    print("==== Running first_character_type ====")
    user_input = input("Enter a password: ")
    result = first_character_type(user_input)
    print("First Character Type:", result)

    print("\n==== Running split_credentials ====")
    user_input = input("Enter user:password (e.g. alice:Secret1): ")
    result = split_credentials(user_input)
    print("User and Password:", result)

    print("\n==== Running digit_ratio ====")
    user_input = input("Enter a password to measure: ")
    result = digit_ratio(user_input)
    print("Digit Ratio:", result)

if __name__ == "__main__":
    main()