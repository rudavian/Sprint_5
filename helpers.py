from random import choice, randint
from string import ascii_lowercase, digits

from data import MIN_PASSWORD_LENGTH, VALID_NAME


def generate_email() -> str:
    random_digits = randint(100, 999)
    return f"IvanRudavin44{random_digits}@yandex.ru"


def generate_password(length: int = MIN_PASSWORD_LENGTH) -> str:
    if length < 1:
        raise ValueError("Password length must be positive")

    alphabet = ascii_lowercase + digits
    return "".join(choice(alphabet) for _ in range(length))


def generate_user_data(name: str = VALID_NAME, password_length: int = MIN_PASSWORD_LENGTH) -> dict[str, str]:
    return {
        "name": name,
        "email": generate_email(),
        "password": generate_password(password_length),
    }
