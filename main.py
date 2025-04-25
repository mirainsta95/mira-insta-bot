from instagrapi import Client
import random
import time

# Session-Login vorbereiten
USERNAME = "mira.insta95@gmail.com"
PASSWORD = "bekhew-bepxEd-cekse8"

cl = Client()
cl.login(USERNAME, PASSWORD)

# Kommentare im Mira-Stil
mira_comments = [
    "Wow, was für starke Worte ✨",
    "Deine Energie inspiriert mich 🙏",
    "So viel Liebe in diesem Post 💛",
    "Danke, dass du das teilst 💫",
    "Genau das hab ich heute gebraucht 🤍"
]

# Ziel-Hashtags
hashtags = ["selbstliebe", "mindsetmatters", "femaleempowerment", "SelbstliebeJetzt", "WeiblichkeitLeben", "FreiheitFühlen", "IchGehöreMir",
"StilleStärke", "MindsetMagic", "FemaleEmpowerment", "InnerGlow", "WahreFreiheit", "Abendgedanken", "BalanceImAlltag", "Selbstfürsorg"]

for tag in hashtags:
    posts = cl.hashtag_medias_recent(tag, amount=5)
    for post in posts:
        cl.media_like(post.id)
        comment = random.choice(mira_comments)
        cl.media_comment(post.id, comment)
        print(f"💬 Kommentiert unter #{tag}: {comment}")
        time.sleep(random.randint(30, 60))
