#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DiaaSuperCUPP v4.0 - Million Password Wordlist Generator
For Authorized Security Testing Only
Generates 1,000,000+ realistic passwords with deep name & date mutations.
"""

import itertools
import random
import os
from datetime import datetime
from collections import deque


# ██████████████████████████████████
# BANNER
# ██████████████████████████████████

def banner():
    print("=" * 70)
    print("   DiaaSuperCUPP v4.0 - MILLION PASSWORD GENERATOR")
    print("   For Authorized Security Testing Only")
    print("   1,000,000+ Passwords | Deep Name & Date Mutations")
    print("=" * 70)


# ██████████████████████████████████
# DATA COLLECTION
# ██████████████████████████████████

def get_user_data():
    print("\n[+] Enter target information (leave blank if unknown)\n")

    data = {
        'first': input("First Name           : ").strip(),
        'last': input("Last Name            : ").strip(),
        'nick': input("Nickname             : ").strip(),
        'bday': input("Birthdate (DD MM YYYY): ").strip(),
        'partner': input("Partner Name         : ").strip(),
        'pbday': input("Partner Birthdate    : ").strip(),
        'pet': input("Pet Name             : ").strip(),
        'company': input("Company/Work         : ").strip(),
        'keywords': input("Extra Keywords (comma separated): ").strip(),
        'phone': input("Phone Number (last 4+ digits)   : ").strip(),
        'address': input("Street/City Name     : ").strip(),
    }
    return data


# ██████████████████████████████████
# DEEP CASE MUTATIONS (EXPANDED)
# ██████████████████████████████████

def generate_all_case_variations(word):
    """
    Generate EVERY possible case variation of a word.
    Expanded version with more patterns for million-scale generation.
    """
    if not word or len(word) < 2:
        return [word] if word else []

    variations = set()
    word_lower = word.lower()
    word_upper = word.upper()
    word_len = len(word_lower)

    # 1. Standard cases
    variations.add(word_lower)  # all lower
    variations.add(word_upper)  # ALL UPPER
    variations.add(word_lower.capitalize())  # First capital
    variations.add(word_lower.title())  # Title Case

    # 2. Each single letter capitalized (one by one)
    for i in range(word_len):
        temp = list(word_lower)
        temp[i] = temp[i].upper()
        variations.add(''.join(temp))

    # 3. Each single letter lowered from ALL CAPS
    for i in range(word_len):
        temp = list(word_upper)
        temp[i] = temp[i].lower()
        variations.add(''.join(temp))

    # 4. First + last uppercase
    if word_len >= 2:
        temp = list(word_lower)
        temp[0] = temp[0].upper()
        temp[-1] = temp[-1].upper()
        variations.add(''.join(temp))

    # 5. Alternating patterns
    temp = list(word_lower)
    for i in range(1, word_len, 2):
        temp[i] = temp[i].upper()
    variations.add(''.join(temp))

    temp = list(word_lower)
    for i in range(0, word_len, 2):
        temp[i] = temp[i].upper()
    variations.add(''.join(temp))

    # 6. Middle letters uppercase
    if word_len >= 4:
        temp = list(word_lower)
        for i in range(1, word_len - 1):
            temp[i] = temp[i].upper()
        variations.add(''.join(temp))

    # 7. Random 2, 3 capital letters
    if word_len >= 3:
        for _ in range(5):  # More random patterns
            temp = list(word_lower)
            positions = random.sample(range(word_len), min(2, word_len))
            for pos in positions:
                temp[pos] = temp[pos].upper()
            variations.add(''.join(temp))

    if word_len >= 4:
        for _ in range(3):
            temp = list(word_lower)
            positions = random.sample(range(word_len), min(3, word_len))
            for pos in positions:
                temp[pos] = temp[pos].upper()
            variations.add(''.join(temp))

    # 8. Vowels/Consonants patterns
    vowels = 'aeiou'
    temp = list(word_lower)
    for i, char in enumerate(temp):
        if char in vowels:
            temp[i] = char.upper()
    variations.add(''.join(temp))

    temp = list(word_lower)
    for i, char in enumerate(temp):
        if char not in vowels:
            temp[i] = char.upper()
    variations.add(''.join(temp))

    # 9. First half uppercase, second half lowercase (and vice versa)
    if word_len >= 4:
        mid = word_len // 2
        variations.add(word_lower[:mid].upper() + word_lower[mid:].lower())
        variations.add(word_lower[:mid].lower() + word_lower[mid:].upper())

    # 10. Every other letter with random case
    for _ in range(3):
        temp = list(word_lower)
        for i in range(word_len):
            if random.choice([True, False]):
                temp[i] = temp[i].upper()
        variations.add(''.join(temp))

    return list(variations)


# ██████████████████████████████████
# LEET SPEAK MUTATIONS (EXPANDED)
# ██████████████████████████████████

def generate_leet_variations(word):
    """Generate extensive leet speak variations"""
    leet_map = {
        'a': ['4', '@', '^'],
        'e': ['3', '&'],
        'i': ['1', '!', '|'],
        'o': ['0', '()'],
        's': ['5', '$', 'z'],
        't': ['7', '+'],
        'l': ['1', '|'],
        'b': ['8', '6'],
        'g': ['9', '6'],
        'z': ['2', '7'],
        'c': ['(', '<'],
        'd': ['[)', '|)'],
    }

    variations = {word}
    word_lower = word.lower()

    # Single replacements
    for char, replacements in leet_map.items():
        if char in word_lower:
            for rep in replacements[:2]:  # Limit to first 2 replacements
                variations.add(word_lower.replace(char, rep))
                variations.add(word_lower.replace(char, rep).capitalize())

    # Double replacements
    for char1, reps1 in leet_map.items():
        if char1 in word_lower:
            temp = word_lower.replace(char1, reps1[0])
            for char2, reps2 in leet_map.items():
                if char2 != char1 and char2 in temp:
                    variations.add(temp.replace(char2, reps2[0]))
                    break

    # Triple replacements (for longer words)
    if len(word_lower) >= 5:
        temp = word_lower
        replaced = 0
        for char, reps in leet_map.items():
            if char in temp and replaced < 3:
                temp = temp.replace(char, reps[0], 1)
                replaced += 1
        variations.add(temp)

    return list(variations)


# ██████████████████████████████████
# DATE EXTRACTION (DEEP)
# ██████████████████████████████████

def parse_birthdate_deep(bday_str):
    """
    Extract ALL possible date components with multiple formats
    """
    parts = []
    if not bday_str:
        return parts

    clean = bday_str.replace('-', ' ').replace('/', ' ').replace('.', ' ').replace(',', ' ')
    tokens = clean.split()

    numeric_tokens = []
    for t in tokens:
        if t.isdigit():
            numeric_tokens.append(t)

    full_numeric = ''.join(numeric_tokens)
    if full_numeric and len(full_numeric) >= 4:
        parts.append(full_numeric)

    if len(numeric_tokens) >= 1:
        for token in numeric_tokens:
            parts.append(token)

            if len(token) == 8:  # DDMMYYYY
                day = token[0:2]
                month = token[2:4]
                year = token[4:8]
                year_short = token[6:8]

                # All possible 2-digit combinations
                parts.extend([
                    day, month, year, year_short,
                    day + month, month + day,
                    month + year, year + month,
                    day + year, year + day,
                    day + month + year_short,
                    month + year_short,
                    year_short + month,
                    year_short + day,
                    day + month + year,
                    month + day + year,
                    year + month + day,
                ])

                # With separators
                for sep in ['', '_', '-', '.', '@', '#']:
                    parts.append(f"{day}{sep}{month}{sep}{year}")
                    parts.append(f"{day}{sep}{month}{sep}{year_short}")
                    parts.append(f"{month}{sep}{year}")
                    parts.append(f"{day}{sep}{year}")

            elif len(token) == 6:  # MMYYYY
                month = token[0:2]
                year = token[2:6]
                year_short = token[4:6]

                parts.extend([
                    month, year, year_short,
                    month + year_short,
                    year_short + month,
                    month + '_' + year,
                ])

            elif len(token) == 4 and 1900 <= int(token) <= 2100:
                year_short = token[2:4]
                parts.append(year_short)

    # Special: if we have day and month, create combined variations
    if len(numeric_tokens) >= 2:
        day = numeric_tokens[0]
        month = numeric_tokens[1]
        if len(day) <= 2 and len(month) <= 2:
            parts.extend([
                day + month,
                month + day,
                day + '_' + month,
                month + '_' + day,
            ])

    # If we have year as last token
    if len(numeric_tokens) >= 3:
        year = numeric_tokens[-1]
        if len(year) == 4:
            year_short = year[2:]
            day = numeric_tokens[0]
            month = numeric_tokens[1]

            # All combinations with year
            parts.extend([
                day + month + year,
                day + month + year_short,
                month + year,
                day + year,
                year + day + month,
                year_short + day + month,
            ])

    return list(set([p for p in parts if p and len(p) >= 1]))


# ██████████████████████████████████
# EXTRACT ALL BASE WORDS
# ██████████████████████████████████

def extract_all_base_words(data):
    """Extract every possible word from all fields"""
    all_words = set()

    fields = ['first', 'last', 'nick', 'partner', 'pet', 'company', 'phone', 'address']

    for key in fields:
        val = data.get(key, '')
        if val and len(val) >= 2:
            all_words.add(val)
            all_words.add(val[::-1])

            if len(val) >= 2:
                all_words.add(val[:2])
                all_words.add(val[-2:])
                all_words.add(val[:2].upper())
                all_words.add(val[-2:].upper())
            if len(val) >= 3:
                all_words.add(val[:3])
                all_words.add(val[-3:])
                all_words.add(val[:3].capitalize())
                all_words.add(val[-3:].capitalize())
            if len(val) >= 4:
                all_words.add(val[:4])
                all_words.add(val[-4:])

    # Extra keywords
    extra = data.get('keywords', '')
    if extra:
        for kw in extra.split(','):
            kw = kw.strip()
            if len(kw) >= 2:
                all_words.add(kw)
                all_words.add(kw[::-1])
                all_words.add(kw.capitalize())

    # Birthdate parts
    bday_parts = parse_birthdate_deep(data.get('bday', ''))
    pbday_parts = parse_birthdate_deep(data.get('pbday', ''))

    all_words.update(bday_parts)
    all_words.update(pbday_parts)

    all_words = {w for w in all_words if len(w) >= 1}

    return list(all_words)


# ██████████████████████████████████
# EXTENDED SUFFIXES POOL
# ██████████████████████████████████

def get_extended_suffixes():
    """Massive suffix/prefix pool for million-scale generation"""
    pool = []

    # Years (1960-2030)
    for y in range(1960, 2031):
        pool.append(str(y))
        pool.append(str(y)[2:])

    # All numbers 0-999
    for i in range(0, 1000):
        pool.append(str(i))
        pool.append(str(i).zfill(2))
        pool.append(str(i).zfill(3))
        pool.append(str(i).zfill(4))

    # Common number patterns
    common = [
        '0000', '00000', '000000', '1111', '2222', '3333', '4444', '5555',
        '6666', '7777', '8888', '9999', '12345', '54321', '123456', '654321',
        '1234567', '7654321', '12345678', '87654321', '112233', '445566',
        '778899', '101010', '121212', '131313', '141414', '151515', '161616',
        '171717', '181818', '191919', '202020', '212121', '232323', '242424',
        '252525', '262626', '272727', '282828', '292929', '303030', '313131',
        '696969', '969696', '123123', '321321', '456456', '654654', '789789',
        '987987', '147147', '258258', '369369', '159159', '753753', '852852',
    ]
    pool.extend(common)

    # Symbols
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '?', '_', '-', '.', '+', '=', '~', '`', '|', ':', ';']
    pool.extend(symbols)

    # Symbol combinations (2, 3 chars)
    for s1 in symbols[:8]:
        pool.append(s1 + s1)
        for s2 in symbols[8:14]:
            pool.append(s1 + s2)

    sym_triples = ['!!!', '@@@', '###', '$$$', '%%%', '___', '---', '...', '!@#', '#$%', '_-.', '***', '+++', '===',
                   '???']
    pool.extend(sym_triples)

    # Year + Symbol combinations
    for y in range(1990, 2031):
        for s in ['!', '@', '#', '$', '_', '-', '.', '*']:
            pool.append(f"{y}{s}")
            pool.append(f"{s}{y}")
            pool.append(f"{s}{y}{s}")

    # Year short + Symbol
    for y in range(90, 131):
        for s in ['!', '@', '#', '$', '_']:
            pool.append(f"{s}{y}")
            pool.append(f"{y}{s}")

    # Special words commonly used as suffixes
    special_words = [
        'admin', 'root', 'user', 'pass', 'word', 'love', 'life', 'god', 'devil',
        'angel', 'dark', 'light', 'fire', 'water', 'earth', 'wind', 'sun', 'moon',
        'star', 'sky', 'sea', 'ocean', 'river', 'stone', 'gold', 'silver', 'bronze',
        'king', 'queen', 'prince', 'princess', 'master', 'slave', 'warrior', 'ninja',
        'samurai', 'ranger', 'knight', 'wizard', 'witch', 'dragon', 'phoenix', 'unicorn',
        'lion', 'tiger', 'wolf', 'fox', 'bear', 'eagle', 'hawk', 'snake', 'spider',
        'ghost', 'phantom', 'shadow', 'storm', 'thunder', 'lightning', 'rain', 'snow',
        'ice', 'frost', 'blaze', 'flame', 'ember', 'ash', 'dust', 'rock', 'metal',
        'wood', 'leaf', 'flower', 'rose', 'lily', 'tulip', 'daisy', 'sunflower',
        'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
        'zero', 'hundred', 'thousand', 'million', 'billion', 'first', 'last',
        'top', 'best', 'super', 'ultra', 'mega', 'giga', 'tera', 'peta', 'exa',
        'alpha', 'beta', 'gamma', 'delta', 'omega', 'sigma', 'theta', 'lambda',
        'red', 'blue', 'green', 'yellow', 'black', 'white', 'purple', 'orange',
        'pink', 'brown', 'gray', 'grey', 'cyan', 'magenta', 'violet', 'indigo',
        'cat', 'dog', 'bird', 'fish', 'horse', 'cow', 'pig', 'sheep', 'goat', 'deer',
        'rabbit', 'mouse', 'rat', 'elephant', 'monkey', 'gorilla', 'tiger', 'leopard',
        'jaguar', 'panther', 'cheetah', 'hyena', 'jackal', 'fox', 'bear', 'panda',
    ]
    pool.extend(special_words)

    return pool


# ██████████████████████████████████
# MAIN GENERATION ENGINE - MILLION SCALE
# ██████████████████████████████████

def generate_million_wordlist(base_words, filename, target_min=1000000):
    """
    DiaaSuperCUPP Million Generation Engine
    - Memory-safe direct file writing
    - 8 phases to reach 1,000,000+ passwords
    """
    print(f"\n[*] Base words extracted: {len(base_words)}")
    print(f"[*] Target: {target_min:,} passwords")

    # Step 1: Generate variations
    print("\n[*] Generating deep case mutations for all words...")
    all_variations = set()

    for i, word in enumerate(base_words):
        case_vars = generate_all_case_variations(word)
        all_variations.update(case_vars)

        if len(word) >= 3 and len(all_variations) < 30000:
            leet_vars = generate_leet_variations(word)
            all_variations.update(leet_vars)

        if (i + 1) % 100 == 0:
            print(f"    Progress: {i + 1}/{len(base_words)} words... ({len(all_variations):,} variations)")

    # Limit variations to prevent memory issues (but keep enough for million)
    if len(all_variations) > 50000:
        all_variations = set(random.sample(list(all_variations), 50000))

    all_variations = list(all_variations)
    print(f"[+] Total variations: {len(all_variations):,}")

    # Separate name and date words
    name_words = [w for w in all_variations if not w.isdigit()]
    date_words = [w for w in all_variations if w.isdigit()]

    print(f"[+] Name variations: {len(name_words):,}")
    print(f"[+] Date variations: {len(date_words):,}")

    # Get extended suffixes
    suffixes = get_extended_suffixes()
    print(f"[+] Suffixes pool: {len(suffixes):,}")

    # Open file for direct writing
    f = open(filename, 'w', encoding='utf-8')
    seen = set()
    count = 0

    def add_password(pwd):
        """Add password if valid"""
        nonlocal count
        if 8 <= len(pwd) <= 40 and pwd not in seen:
            seen.add(pwd)
            f.write(pwd + '\n')
            count += 1
            if len(seen) > 1000000:
                seen.clear()
            return True
        return False

    # ═══════════════════════════════════
    # PHASE 1: Name + Date (ALL combinations)
    # ═══════════════════════════════════
    print("\n[*] PHASE 1: Name + Date massive combinations...")

    name_sample = name_words[:1000] if len(name_words) > 1000 else name_words
    date_sample = date_words[:300] if len(date_words) > 300 else date_words

    separators = ['', '_', '-', '.', '@', '#', '!', '$', '*', '+']

    for i, name in enumerate(name_sample):
        if count >= target_min * 0.15:
            break

        for date in date_sample:
            add_password(name + date)
            add_password(date + name)

            for sep in separators[:6]:
                add_password(f"{name}{sep}{date}")
                add_password(f"{date}{sep}{name}")

            add_password(name[::-1] + date)
            add_password(date + name[::-1])
            add_password(name.capitalize() + date)
            add_password(name.upper() + date)

        if i % 100 == 0:
            print(f"    {count:,} passwords...")

    print(f"[+] Phase 1: {count:,} passwords")

    # ═══════════════════════════════════
    # PHASE 2: Name + Suffix (Massive)
    # ═══════════════════════════════════
    print("\n[*] PHASE 2: Name + Suffix massive...")

    for i, word in enumerate(name_words[:2000]):
        if count >= target_min * 0.35:
            break

        for suf in suffixes[:500]:
            add_password(word + suf)
            add_password(suf + word)
            add_password(word.capitalize() + suf)
            add_password(suf + word.capitalize())
            add_password(word[::-1] + suf)
            add_password(suf + word[::-1])

            if count % 50000 == 0 and count > 0:
                print(f"    {count:,} passwords...")

        if i % 200 == 0:
            print(f"    Processing word {i}/{len(name_words[:2000])}: {count:,} passwords...")

    print(f"[+] Phase 2: {count:,} passwords")

    # ═══════════════════════════════════
    # PHASE 3: Name + Name combinations
    # ═══════════════════════════════════
    print("\n[*] PHASE 3: Name + Name pairs...")

    name_sample_2 = name_words[:300]

    for w1 in name_sample_2:
        if count >= target_min * 0.5:
            break

        for w2 in name_sample_2:
            add_password(w1 + w2)
            add_password(w1 + '_' + w2)
            add_password(w1 + '.' + w2)
            add_password(w1 + '@' + w2)
            add_password(w1.lower() + w2.upper())
            add_password(w1.upper() + w2.lower())
            add_password(w1.capitalize() + w2)
            add_password(w1 + w2.capitalize())
            add_password(w1[::-1] + w2)
            add_password(w1 + w2[::-1])

    print(f"[+] Phase 3: {count:,} passwords")

    # ═══════════════════════════════════
    # PHASE 4: Date + Date + Symbol
    # ═══════════════════════════════════
    print("\n[*] PHASE 4: Date + Date + Symbol...")

    date_sample_2 = date_words[:100]
    syms = ['!', '@', '#', '$', '%', '_', '-', '.', '*', '+']

    for d1 in date_sample_2:
        if count >= target_min * 0.6:
            break

        for d2 in date_sample_2:
            for s in syms[:8]:
                add_password(d1 + d2 + s)
                add_password(d1 + s + d2)
                add_password(s + d1 + d2)
                add_password(d1 + d2)
                add_password(d1 + '_' + d2 + s)

    print(f"[+] Phase 4: {count:,} passwords")

    # ═══════════════════════════════════
    # PHASE 5: Name + Symbol + Date (Ali@1990)
    # ═══════════════════════════════════
    print("\n[*] PHASE 5: Name + Symbol + Date (killer combo)...")

    years = [str(y) for y in range(1960, 2031)]
    years_short = [str(y)[2:] for y in range(1960, 2031)]

    for i, name in enumerate(name_sample[:800]):
        if count >= target_min * 0.75:
            break

        for yr in years[:50]:
            for s in syms[:8]:
                add_password(f"{name}{s}{yr}")
                add_password(f"{name}{yr}{s}")
                add_password(f"{s}{name}{yr}")
                add_password(f"{yr}{s}{name}")
                add_password(f"{name[::-1]}{s}{yr}")
                add_password(f"{name.capitalize()}{s}{yr}")
                add_password(f"{name}{s}{yr[2:]}")

        if i % 100 == 0:
            print(f"    {count:,} passwords...")

    print(f"[+] Phase 5: {count:,} passwords")

    # ═══════════════════════════════════
    # PHASE 6: Triple combinations
    # ═══════════════════════════════════
    print("\n[*] PHASE 6: Triple combinations (name+suffix+symbol)...")

    for i in range(50000):
        if count >= target_min * 0.9:
            break

        w = random.choice(name_words)
        suf = random.choice(suffixes[:200])
        sym = random.choice(syms)

        add_password(w + suf + sym)
        add_password(sym + w + suf)
        add_password(w + sym + suf)
        add_password(suf + w + sym)
        add_password(w.capitalize() + suf + sym)
        add_password(w + '_' + suf + sym)

    print(f"[+] Phase 6: {count:,} passwords")

    # ═══════════════════════════════════
    # PHASE 7: Four-part combinations
    # ═══════════════════════════════════
    print("\n[*] PHASE 7: Four-part combinations...")

    for i in range(50000):
        if count >= target_min * 0.98:
            break

        w1 = random.choice(name_words)
        w2 = random.choice(name_words)
        d = random.choice(date_words[:50]) if date_words else random.choice(suffixes[:50])
        s = random.choice(syms)

        add_password(w1 + s + w2 + d)
        add_password(w1 + d + s + w2)
        add_password(d + s + w1 + w2)
        add_password(w1 + '_' + w2 + '_' + d)
        add_password(s + w1 + d + s)

    print(f"[+] Phase 7: {count:,} passwords")

    # ═══════════════════════════════════
    # PHASE 8: Guarantee fill
    # ═══════════════════════════════════
    print("\n[*] PHASE 8: Final fill to guarantee million...")

    fill_count = 0
    while count < target_min:
        w = random.choice(name_words)
        d = random.choice(date_words) if date_words else str(random.randint(1900, 2030))
        s = random.choice(syms)
        suf = random.choice(suffixes[:300])

        add_password(w + d)
        add_password(w + s + d)
        add_password(w + suf)
        add_password(w + s + suf)
        add_password(w.capitalize() + '_' + d + s)
        add_password(w + d + suf)
        add_password(suf + w + d)
        add_password(w[::-1] + d + s)
        add_password(d + '_' + w + '_' + suf)
        add_password(w + s + d + suf)

        fill_count += 1
        if fill_count % 10000 == 0:
            print(f"    Filling... {count:,} passwords")

    f.close()
    print(f"\n[✓] GENERATION COMPLETE!")
    print(f"[✓] Total passwords: {count:,}")
    print(f"[✓] Saved to: {filename}")

    return count


# ██████████████████████████████████
# MAIN FUNCTION
# ██████████████████████████████████

def main():
    banner()

    print("\n[!] WARNING: This tool is for AUTHORIZED security testing only!")
    print("[!] Unauthorized use is illegal and unethical.")
    print()

    consent = input("Do you have authorization? (yes/no): ").strip().lower()
    if consent not in ['yes', 'y']:
        print("\n[!] Exiting. Authorization required.")
        return

    data = get_user_data()

    # Extract all base words
    base_words = extract_all_base_words(data)

    if len(base_words) < 3:
        print("\n[!] Very few inputs detected. Adding common defaults...")
        defaults = [
            'admin', 'password', 'user', 'test', 'guest', 'root',
            'love', 'abc', 'xyz', 'qwerty', 'master', 'access',
            'hello', 'world', 'secret', 'login', 'welcome',
            'computer', 'internet', 'system', 'network', 'security',
            'hacker', 'coder', 'program', 'software', 'hardware',
        ]
        base_words.extend(defaults)

    # Generate output filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"DiaaSuperCUPP_Million_{timestamp}.txt"

    # Start generation
    print("\n" + "=" * 70)
    print("   STARTING MILLION PASSWORD GENERATION")
    print(f"   Target: 1,000,000+ passwords")
    print("=" * 70)

    import time
    start_time = time.time()

    total = generate_million_wordlist(base_words, filename, target_min=1000000)

    elapsed = time.time() - start_time
    minutes = elapsed / 60

    # Summary
    print("\n" + "=" * 70)
    print(f"   ✓ SUCCESS: {total:,} passwords generated")
    print(f"   ✓ Time: {minutes:.1f} minutes")
    print(f"   ✓ Speed: {total / elapsed:.0f} passwords/second")
    print(f"   ✓ File size: {os.path.getsize(filename) / 1024 / 1024:.1f} MB")
    print(f"   ✓ File: {filename}")
    print("=" * 70)

    # Sample preview
    print("\n[?] Show 20 random samples? (y/n): ", end='')
    if input().strip().lower() == 'y':
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            samples = random.sample(lines, min(20, len(lines)))
            print("\n   ── Sample Passwords (20 of 1,000,000+) ──")
            for i, s in enumerate(samples, 1):
                print(f"   {i:2d}. {s.strip()}")


if __name__ == "__main__":
    main()