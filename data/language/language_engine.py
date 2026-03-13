import random, string, hashlib

class FantasyTranslator:
    def __init__(self):
        self.languages = {
            "dwarven": {"chars": "ᚠᚢᚦᚨᚱᚲᚷᚹᚺᚻᚼᛄᛇᛈᛉᛊᛋᛏᛒᛖᛗᛚᛜᛝᛟᛞ", "style": "rune"},
            "elven":   {"chars": "αβγδεζηθικλμνξοπρστυφχψω", "style": "flow"},
            "gnomish": {"chars": "kzpxjwvq", "style": "staccato"},
            "common":  {"chars": string.ascii_lowercase, "style": "dialect"}
        }
        self.lexicon = set()
        
        # --- MASTER FLAVOR POOLS ---
        self.flavor = {
            "drunk_base": ["sh...", "...hic!", "sssh...", " *belch* ", "...urgh"],
            "drunk_high": ["...wha?", "...I love you guys...", "...hic! *stumble*"],
            "pain_base":  ["...*ghk*...", "...*haaa*...", "...*cough*...", "...*gasp*..."],
            "pain_high":  ["...*gurgle*...", "...*blood fills mouth*...", "...*heavy breathing*..."],
            "mental_base":["Uhh...", "...", "Wh-what?", "I...", "Wait..."],
            "mental_high":["Who are you?", "???", "...forget it...", "*stares blankly*"]
        }

    def _is_description(self, word):
        """Prevents emotes like *hic* from being mangled."""
        return word.startswith("*") or (word.startswith("(") and word.endswith(")"))

    def _apply_mental(self, word, level):
        if level <= 25 or self._is_description(word): return word
        # Weight: Dividied by 3 to keep the sentence structure mostly intact
        if random.random() * 100 < (level / 3):
            pool = self.flavor["mental_base"]
            if level > 70: pool += self.flavor["mental_high"]
            return random.choice(pool)
        return word

    def _apply_intoxication(self, word, level):
        if level <= 20 or self._is_description(word): return word
        
        # Aggressive Double-Vowel Dragging
        vowels = "aeiouy"
        if random.random() * 100 < level:
            drag_factor = level // 20
            found = [c for c in word.lower() if c in vowels]
            targets = list(set(found))[:2] # Drag up to two different vowels
            
            for target in targets:
                drag = target * drag_factor
                if target.upper() in word:
                    word = word.replace(target.upper(), target.upper() + drag.lower(), 1)
                else:
                    word = word.replace(target, target + drag, 1)
        
        # Slurs
        if level > 40 and random.random() * 100 < (level / 2):
            pool = self.flavor["drunk_base"]
            if level > 75: pool += self.flavor["drunk_high"]
            word += random.choice(pool)
        return word

    def _apply_injury(self, word, level):
        if level <= 30 or not word or self._is_description(word): return word
        
        # Stuttering
        if word[0].isalpha() and random.random() * 100 < level:
            word = f"{word[0]}-{word[0].lower()}-{word}"
        
        # Pain Interjections
        if level > 50 and random.random() * 100 < (level / 3):
            pool = self.flavor["pain_base"]
            if level > 80: pool += self.flavor["pain_high"]
            word += random.choice(pool)
        return word

    def _scramble(self, word, lang):
        config = self.languages.get(lang, self.languages["common"])
        res = []
        for c in word:
            if not c.isalpha(): res.append(c); continue
            if config["style"] == "dialect":
                idx = (string.ascii_lowercase.index(c.lower()) + 3) % 26
                new_c = string.ascii_lowercase[idx]
                res.append(new_c.upper() if c.isupper() else new_c)
            else:
                new_c = random.choice(config["chars"])
                res.append(new_c.upper() if c.isupper() else new_c.lower())
        return "".join(res)

    def translate(self, text, lang, p_skill, r_skill, drunk=0, hurt=0, mental=0):
        words = text.split()
        # Weighted Penalty (Mental is the lightest impact)
        penalty = (drunk * 0.5) + (hurt * 0.4) + (mental * 0.1)
        eff_p = max(0, p_skill - penalty)
        
        spoken = []
        for w in words:
            clean = w.lower().strip(string.punctuation)
            random.seed(int(hashlib.md5((clean + lang).encode()).hexdigest(), 16))
            
            # 1. Base Word Selection (Lexicon/Skill check)
            base = w if (random.random() * 100 < eff_p or clean in self.lexicon) else self._scramble(w, lang)
            
            # 2. Pipeline (Mental Interruption -> Drunk Slur -> Injury Stutter)
            processed = self._apply_mental(base, mental)
            processed = self._apply_intoxication(processed, drunk)
            processed = self._apply_injury(processed, hurt)
            spoken.append(processed)

        return " ".join(spoken)

# --- Final Verification ---
engine = FantasyTranslator()
msg = "The dragon is here in the mountain."

# The "Bad Day" Test (Very Drunk, Very Hurt, Moderately Confused)
print(engine.translate(msg, "common", 100, 100, drunk=0, hurt=50, mental=40))