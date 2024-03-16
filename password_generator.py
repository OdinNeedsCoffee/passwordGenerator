import string
import secrets


def createPW(pw_length):
    global password
    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation
    available_chars = string.ascii_letters + string.digits + string.punctuation

    pw_strong = False

    while not pw_strong:
        password = ""
        password += ''.join(secrets.choice(available_chars) for i in range(int(pw_length)))
        if any(char in punctuation for char in password) and (sum(char in digits for char in password) > 2):
            pw_strong = True
    return password


if __name__ == "__main__":
    print(createPW(input("Password length: ")))
