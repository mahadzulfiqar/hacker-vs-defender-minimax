import random

def hacker_attack():
    attacks = ["SQL Injection", "Phishing", "Brute Force", "DDoS"]
    return random.choice(attacks)

def defender_response():
    defenses = ["Firewall", "Anti-virus", "Encryption", "2FA"]
    return random.choice(defenses)

def play_round():
    attack = hacker_attack()
    defense = defender_response()
    print(f"💻 Hacker tries: {attack}")
    print(f"🛡️ Defender uses: {defense}")

    if attack == "SQL Injection" and defense == "Firewall":
        print("✅ Defender blocked the attack!\n")
    elif attack == "Phishing" and defense == "2FA":
        print("✅ Defender blocked the attack!\n")
    elif attack == "Brute Force" and defense == "Encryption":
        print("✅ Defender blocked the attack!\n")
    elif attack == "DDoS" and defense == "Anti-virus":
        print("✅ Defender blocked the attack!\n")
    else:
        print("⚠️ Hacker succeeded!\n")

if __name__ == "__main__":
    print("=== Hacker vs Defender Game ===\n")
    for round in range(3):
        print(f"Round {round+1}")
        play_round()

