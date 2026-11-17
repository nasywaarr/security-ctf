"""
Challenge 2 - Four-digit PIN brute force
Reads a single SHA-256 hash (pin_target.txt) and tries every 4-digit
PIN from "0000" to "9999" (zero-padded) until it finds a match.
"""
import hashlib

PIN_TARGET_FILE = "pin_target.txt"


def sha256_hex(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main():
    with open(PIN_TARGET_FILE) as f:
        target = f.read().strip()

    for i in range(10000):
        pin = f"{i:04d}"  # zero-padded, e.g. 7 -> "0007"
        attempts = i + 1
        if sha256_hex(pin) == target:
            print(f"PIN found: {pin}")
            print(f"Attempts: {attempts}")
            return

    print("No PIN in 0000-9999 matched the target hash.")


if __name__ == "__main__":
    main()
