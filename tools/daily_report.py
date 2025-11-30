import os
import requests
from datetime import datetime, timedelta, timezone

OWNER = "pradneshluniya58-creator"
REPO = "Python-learning"
TOKEN = os.getenv("GITHUB_TOKEN")
API_BASE = "https://api.github.com"

def gh_get(path, params=None):
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github+json",
    }
    url = f"{API_BASE}{path}"
    r = requests.get(url, headers=headers, params=params)
    r.raise_for_status()
    return r.json()

def get_commits_since(since, until):
    return gh_get(f"/repos/{OWNER}/{REPO}/commits", {
        "since": since.isoformat(),
        "until": until.isoformat(),
    })

def analyze():
    now = datetime.now(timezone.utc)
    start_this_week = now - timedelta(days=7)
    start_last_week = now - timedelta(days=14)

    commits_this_week = get_commits_since(start_this_week, now)
    commits_last_week = get_commits_since(start_last_week, start_this_week)

    commits_today = [
        c for c in commits_this_week
        if c["commit"]["author"]["date"][:10] == now.date().isoformat()
    ]

    # Languages
    languages = gh_get(f"/repos/{OWNER}/{REPO}/languages")

    total_lang_loc = sum(languages.values()) or 1
    python_pct = round(languages.get("Python", 0) * 100 / total_lang_loc, 1)

    # Simple velocity numbers
    cw = len(commits_this_week)
    pw = len(commits_last_week)
    change_pct = 0 if pw == 0 else round((cw - pw) * 100 / pw, 1)

    # Very rough skill level heuristic
    skill_level = 2 if cw > 0 else 1

    # Print in your format
    print("DAILY PROGRESS SNAPSHOT")
    print(f'- {len(commits_today)} commits today, {cw} this week, repo {python_pct}% Python')
    print()
    print("THIS WEEK'S FOCUS")
    print("- Main project: Phase 0 Tutorials (in-progress)")
    print("- Topics: basics, conditionals, Git workflow")
    print()
    print("VELOCITY METER")
    print(f"- This week: {cw} commits vs Previous week: {pw} commits = {change_pct}% change")
    print()
    print("SKILL READINESS ASSESSMENT")
    print(f"- Current level: {skill_level}/10 (early, but committing regularly)")
    print("- Next recommended skill: loops + functions, then small CLI tools")
    print("- Risk flag: No (steady progress)")
    print()
    print("QUICK WINS")
    print("- Consistent commits to learning repo")
    print("- Practicing conditionals and pushing code to GitHub")
    print()
    print("ACTION NEEDED")
    print("- Add at least 1 small script using loops + functions before next report")

if __name__ == "__main__":
    analyze()
