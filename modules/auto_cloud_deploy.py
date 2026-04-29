import requests, os, json, time

def get_env(key):
    try:
        with open(".env", "r") as f:
            for line in f:
                if line.startswith(f"{key}="):
                    return line.split("=", 1)[1].strip().replace('"', '')
    except FileNotFoundError:
        return None
    return None

RENDER_KEY = get_env("RENDER_API_KEY")
HF_TOKEN = get_env("HF_TOKEN")
GH_TOKEN = get_env("GITHUB_TOKEN")
REPO_NAME = "TitaniumEmpire"
USER = "pityumajsaii-cell"

def deploy_to_render():
    print("🚀 Render Auto-Provisioning indítása...")
    if not RENDER_KEY:
        print("❌ HIBA: RENDER_API_KEY hiányzik a .env-ből!")
        return
    
    url = "https://api.render.com/v1/services"
    headers = {"Authorization": f"Bearer {RENDER_KEY}", "Content-Type": "application/json"}
    
    # Render API-hoz szükséges alap adatok
    payload = {
        "type": "web_service",
        "name": REPO_NAME,
        "repo": f"https://github.com/{USER}/{REPO_NAME}",
        "autoDeploy": "yes",
        "serviceDetails": {
            "env": "python",
            "buildCommand": "pip install -r requirements.txt",
            "startCommand": "gunicorn app:app",
            "plan": "free"
        }
    }
    
    r = requests.post(url, json=payload, headers=headers)
    if r.status_code in [200, 201]:
        print(f"✅ RENDER SZOLGÁLTATÁS LÉTREHOZVA!")
    else:
        print(f"ℹ️ Render Info: {r.text}")

def deploy_to_huggingface():
    print("🤗 Hugging Face Space szinkronizálás...")
    if not HF_TOKEN:
        print("❌ HIBA: HF_TOKEN hiányzik!")
        return
    # HF Remote hozzáadása és Push
    os.system(f"git remote add hf https://{USER}:{HF_TOKEN}@huggingface.co/spaces/{USER}/{REPO_NAME} 2>/dev/null || true")
    os.system("git push hf main --force")
    print("✅ HF SPACE FRISSÍTVE!")

if __name__ == "__main__":
    deploy_to_huggingface()
    deploy_to_render()
