# System Security Class — Password Cracking & Trust CTF

Solutions for a student CTF exercise on password cracking and trust cues in a mock captive portal. All hashes and wordlists are synthetic, supplied by the instructor for this exercise only.

## Contents
- `dictionary.py` — SHA-256 dictionary attack against `targets.txt`
- `pin.py` — brute-force of a 4-digit PIN against `pin_target.txt`
- `targets.txt`, `wordlist.txt`, `pin_target.txt` — challenge input data
- `WRITEUP.md` — results, reasoning, and the portal trust-cue notes

## Usage
```
python3 dictionary.py
python3 pin.py
```
