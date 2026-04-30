import os, sqlite3

def generate_daily_stats():
    con = sqlite3.connect('titanium_system.db')
    cur = con.cursor()
    # Megszámoljuk a mai friss leadeket
    total = cur.execute("SELECT count(*) FROM leads WHERE status='new'").fetchone()[0]
    sent = cur.execute("SELECT count(*) FROM leads WHERE status='SENT'").fetchone()[0]
    
    # FFmpeg parancs: professzionális sötét téma, zöld "mátrix" stílusú szöveggel
    text = f"TITANIUM V8 REPORT\\n\\nNew Leads Found: {total}\\nEmails Sent Today: {sent}\\n\\nStatus: ACTIVE"
    
    cmd = (
        f"ffmpeg -y -f lavfi -i color=c=0x111111:s=1280x720:d=15 "
        f"-vf \"drawtext=text='{text}':fontcolor=0x00FF00:fontsize=45:x=(w-text_w)/2:y=(h-text_h)/2:line_spacing=20\" "
        "daily_marketing.mp4"
    )
    os.system(cmd)
    print("🎬 A mai marketing videó elkészült: daily_marketing.mp4")

generate_daily_stats()
