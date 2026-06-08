#!/usr/bin/env python3
import random

# From the wc-spreadsheet.xlsx
UPPER_TEAMS = [
    "Spain", "Argentina", "France", "England", "Brazil",
    "Portugal", "Colombia", "Netherlands", "Ecuador", "Croatia",
    "Germany", "Norway", "Japan", "Turkey", "Uruguay",
    "Switzerland", "Senegal", "Belgium", "Mexico", "Paraguay",
    "Austria", "Morocco", "Canada", "Australia",
]

LOWER_TEAMS = [
    "Scotland", "Iran", "South Korea", "Algeria", "Panama",
    "Uzbekistan", "Czechia", "United States", "Sweden", "Jordan",
    "Egypt", "Ivory Coast", "DR Congo", "Tunisia", "Iraq",
    "Bosnia and Herzegovina", "New Zealand", "Saudi Arabia", "Cape Verde", "Haiti",
    "South Africa", "Ghana", "Curaçao", "Qatar",
]

participants = [line.strip() for line in open("participants.txt") if line.strip()]

random.shuffle(participants)
random.shuffle(UPPER_TEAMS)
random.shuffle(LOWER_TEAMS)

print("\033[H\033[2J", end="")
print("+------------------------------------------------------------+")
print("|           APATA WORLD CUP 2026 DRAW                       |")
print("+------------------------------------------------------------+")
print("|  Upper 24: Top 24 FIFA ranked teams                       |")
print("|  Lower 24: Lower 24 FIFA ranked teams                     |")
print("+------------------------------------------------------------+")
print(f"\n  {len(participants)} participants\n")
input("  Press ENTER to start the draw...")

results = []
for i, person in enumerate(participants):
    print("\033[H\033[2J", end="") # Clears the terminal screen
    print(f"DRAW {i+1} of {len(participants)}\n")
    print(f"  {person}\n")
    print(f"  UPPER:  {UPPER_TEAMS[i]}")
    print(f"  LOWER:  {LOWER_TEAMS[i]}")
    results.append((person, UPPER_TEAMS[i], LOWER_TEAMS[i]))

    if i < len(participants) - 1:
        input("\n  Press ENTER for next person...")
    else:
        input("\n  Press ENTER to see final results...")

print("\033[H\033[2J", end="") # Clears the terminal screen again
print("🏆 FINAL RESULTS 🏆\n")
print(f"{'PARTICIPANT':<15} {'UPPER TEAM':<20} {'LOWER TEAM':<20}")
print("-" * 55)
for name, upper, lower in results:
    print(f"{name:<15} {upper:<20} {lower:<20}")
print("\nGood luck everyone! 🍀")
