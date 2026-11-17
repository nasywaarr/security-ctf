"""
Challenge 1 - Dictionary recovery
Reads a list of SHA-256 hashes (targets.txt) and a wordlist (wordlist.txt),
hashes each candidate password, and reports any matches.
"""
import hashlib

TARGETS_FILE = "targets.txt"
WORDLIST_FILE = "wordlist.txt"


def load_lines(path):
    with open(path) as f:
        return [line.strip() for line in f if line.strip()]


def sha256_hex(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main():
    targets = load_lines(TARGETS_FILE)
    candidates = load_lines(WORDLIST_FILE)

    remaining = set(targets)
    found = {}

    for word in candidates:
        digest = sha256_hex(word)
        if digest in remaining:
            found[digest] = word
            remaining.discard(digest)

    print(f"Checked {len(candidates)} candidates against {len(targets)} target hash(es).\n")
    for target in targets:
        if target in found:
            print(f"MATCH  {target} -> {found[target]!r}")
        else:
            print(f"NO MATCH  {target}")


if __name__ == "__main__":
    main()
