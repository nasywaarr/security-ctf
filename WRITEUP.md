# Student CTF — Password Cracking & Trust

## Challenge 1 — Dictionary recovery (100 pts)

**Script:** `dictionary.py`

**Result:**

| Hash (SHA-256) | Recovered password |
|---|---|
| `280d44ab1e9f79b5cce2dd4f58f5fe91f0fbacdac9f7447dffc318ceb79f2d02` | `welcome` |
| `6a0436eecdad379345d804a9e4861a46e2135054879760acaf8d88534f871b26` | `summer2026` |

**Why a dictionary attack works well against common passwords:**
Most people don't pick passwords at random — they reuse a small set of
familiar patterns: real words, keyboard sequences, names, or a word
with a year stuck on the end (like `summer2026`). SHA-256 is fast and
deterministic, so hashing the same input always gives the same output.
That means an attacker doesn't need to brute-force every possible
string — they just need a list of passwords people actually use, and
they can check thousands of candidates in milliseconds. If a password
is anywhere on that list, it gets found almost instantly. This is also
why "word + number" isn't a strong password strategy: it shrinks the
effective search space down to something a dictionary attack can
cover easily, even though the full space of possible passwords is
enormous.

## Challenge 2 — Four-digit PIN (150 pts)

**Script:** `pin.py`

**Result:** PIN = `0427`, found in 428 attempts.

**Why leading zeros matter:**
A 4-digit PIN has to be treated as a string, not a number, because
`"0427"` and `427` hash to completely different values — `hashlib.
sha256(b"427")` and `hashlib.sha256(b"0427")` are hashing different
byte sequences. If the loop converts integers to strings without
zero-padding (`str(i)` instead of `f"{i:04d}"`), every PIN below
`1000` never gets tested in its correct 4-digit form, so a PIN like
`0427` would be missed entirely. Zero-padding is what guarantees all
10,000 combinations from `0000` to `9999` actually get checked.
