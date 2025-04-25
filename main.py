from instagrapi import Client
import random
import time

# Session-Login vorbereiten
USERNAME = "mira.insta95@gmail.com"
PASSWORD = "bekhew-bepxEd-cekse8"

cl = Client()
cl.login(USERNAME, PASSWORD)

# 30 Mira-Hashtags
hashtags = [
    "selflove", "selbstliebe", "selbstfürsorge", "dankbarkeit", "achtsamkeit",
    "bewusstsein", "mentalhealth", "mentalhealthawareness", "loveyourself", "healingjourney",
    "innerpeace", "mindsetmatters", "spiritualität", "femalepower", "emotionalhealth",
    "selfcaretips", "dailyrituals", "growthmindset", "inspirationdaily", "positivethoughts",
    "positivemindset", "soulwork", "youareenough", "innerglow", "seelenfrieden",
    "achtsamleben", "starkefrauen", "selfcompassion", "mirajourney", "mirasoul"
]

# Mehr natürliche Kommentare (rotierend)
mira_comments = [
    "So schön geschrieben ✨ danke fürs Teilen!",
    "Genau das hab ich gebraucht heute 💛",
    "Wow, so eine ruhige und starke Energie hier 🌿",
    "Bin ganz bei dir – wunderschöner Beitrag 🙏",
    "Danke für diese Erinnerung 💭🤍",
    "Achtsamkeit ist so kraftvoll 🌸",
    "Das strahlt so viel Liebe aus 💫",
    "Worte, die berühren. Danke dir! 🌞",
    "So wichtig, dass wir uns selbst nicht vergessen 🌱",
    "Einfach nur wow ✨ so inspirierend!"
]

# Einstellungen
MAX_POSTS_PER_HASHTAG = 3
COMMENT_PROBABILITY = 0.2  # 20 % werden kommentiert
DELAY_RANGE = (180, 420)   # 3–7 Minuten Pause

# Interaktionslogik
for tag in random.sample(hashtags, 10):  # 10 zufällige Hashtags
    try:
        posts = cl.hashtag_medias_recent(tag, amount=MAX_POSTS_PER_HASHTAG)
        for post in posts:
            cl.media_like(post.id)
            print(f"❤️ Like unter #{tag} – {post.code}")

            if random.random() < COMMENT_PROBABILITY:
                comment = random.choice(mira_comments)
                cl.media_comment(post.id, comment)
                print(f"💬 Kommentar: {comment}")

            sleep_time = random.randint(*DELAY_RANGE)
            print(f"⏳ Pause: {sleep_time} Sekunden…")
            time.sleep(sleep_time)

    except Exception as e:
        print(f"⚠️ Fehler bei #{tag}: {e}")
        time.sleep(90)
