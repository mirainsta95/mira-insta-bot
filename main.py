from instagrapi import Client
import random
import time

# Session-Login vorbereiten
USERNAME = "mira.insta95@gmail.com"
PASSWORD = "bekhew-bepxEd-cekse8"

cl = Client()
cl.login(USERNAME, PASSWORD)

# Erweiterte Hashtag-Liste (max. 20 wird empfohlen zu durchmischen)
hashtags = [
    "selbstliebe", "mindsetmatters", "femaleempowerment", "freiheitfühlen",
    "innerglow", "achtsamkeit", "positivevibes", "mentalhealth", "selfgrowth",
    "weiblichestärke", "spiritualität", "souljourney", "persönlichkeitsentwicklung",
    "selbstfürsorge", "stillemomente", "bewusstleben", "wachstum", "lebensfreude",
    "vertraueninsleben", "herzensweg"
]

# Mira-Kommentare (sehr selten)
mira_comments = [
    "Danke fürs Teilen 💫",
    "So schön gesagt 💛",
    "Das hat mich gerade berührt ✨"
]

# Einstellungen
MAX_POSTS_PER_HASHTAG = 3  # Noch dezenter
COMMENT_PROBABILITY = 0.1  # Nur 10 % der Likes werden kommentiert
DELAY_RANGE = (120, 240)   # 2 bis 4 Minuten Pause zwischen Aktionen

# Durchlaufe Hashtags
for tag in random.sample(hashtags, 10):  # Max 10 Hashtags pro Durchlauf
    posts = cl.hashtag_medias_recent(tag, amount=MAX_POSTS_PER_HASHTAG)
    for post in posts:
        try:
            cl.media_like(post.id)
            print(f"❤️ Like unter #{tag}")

            if random.random() < COMMENT_PROBABILITY:
                comment = random.choice(mira_comments)
                cl.media_comment(post.id, comment)
                print(f"💬 Kommentar: {comment}")

            sleep_time = random.randint(*DELAY_RANGE)
            print(f"⏳ Pause: {sleep_time} Sekunden…")
            time.sleep(sleep_time)

        except Exception as e:
            print(f"⚠️ Fehler bei #{tag}: {e}")
            time.sleep(60)  # Bei Fehler: 1 Minute cool down
