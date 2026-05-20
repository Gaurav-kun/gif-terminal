import gifos
from datetime import datetime
import os
import requests

USERNAME = (
    os.environ.get("GITHUB_REPOSITORY_OWNER")
    or os.environ.get("GIT_USERNAME")
    or "Gaurav-kun"
)

def get_total_repos(username):
    try:
        response = requests.get(f"https://api.github.com/users/{username}")
        if response.status_code == 200:
            return response.json().get("public_repos", 0)
    except:
        pass
    return None

try:
    github_stats = gifos.utils.fetch_github_stats(user_name=USERNAME)
    has_stats = github_stats is not None
    if not has_stats:
        print("Warning: Could not fetch GitHub stats")
        print("Configure GITHUB_TOKEN in .env file")
except Exception as e:
    print(f"Warning: Error fetching GitHub stats: {e}")
    print("Using example data...")
    has_stats = False
    github_stats = None

total_repos = get_total_repos(USERNAME)

R = "\x1b[91m"   # crimson
G = "\x1b[93m"   # gold
C = "\x1b[96m"   # cyan
N = "\x1b[92m"   # green
B = "\x1b[94m"   # blue
X = "\x1b[0m"    # reset

t = gifos.Terminal(width=700, height=500, xpad=10, ypad=10)
t.set_prompt(f"{R}{USERNAME}{X}@{G}night-dojo{X} ~> ")

# -- Boot sequence (Night Dojo) --
t.gen_text(f"{C}= Night Dojo Terminal v2.0 ={X}", row_num=1)
t.clone_frame(8)
t.gen_text(f"{N}[OK]{X} Kernel loaded - Musashi discipline engaged", row_num=2)
t.clone_frame(5)
t.gen_text(f"{N}[OK]{X} C, C++, Rust runtimes ready", row_num=3)
t.clone_frame(5)
t.gen_text(f"{N}[OK]{X} Three.js renderer initialized", row_num=4)
t.clone_frame(8)

# -- Whoami --
t.gen_prompt(row_num=5)
t.gen_typing_text("whoami", row_num=5, contin=True, speed=1)
t.clone_frame(5)
t.gen_text(f"{C}Gaurav Saikia{R}{X}  -  {G}BCA Student & OSS Believer{X}", row_num=6)
t.clone_frame(15)

# -- GitHub stats command --
t.gen_prompt(row_num=8)
t.gen_typing_text("gh-stats", row_num=8, contin=True, speed=1)
t.clone_frame(5)

t.gen_text("", row_num=9)
t.gen_text(f"{C}===== GitHub Stats ====={X}", row_num=10)
t.clone_frame(3)

if has_stats:
    repos_count = total_repos if total_repos else github_stats.total_repo_contributions
    stats_lines = [
        f"{G}Name:{X}        {github_stats.account_name or USERNAME}",
        f"{G}Followers:{X}   {github_stats.total_followers}",
        f"{G}Stars:{X}       {github_stats.total_stargazers}",
        f"{G}Commits:{X}     {github_stats.total_commits_last_year} (last yr)",
        f"{G}PRs:{X}         {github_stats.total_pull_requests_made}",
        f"{G}Issues:{X}      {github_stats.total_issues}",
        f"{G}Repos:{X}       {repos_count}",
        f"{G}Rank:{X}        {github_stats.user_rank.level} ({github_stats.user_rank.percentile:.1f}%)",
    ]
    if github_stats.languages_sorted:
        top_langs = github_stats.languages_sorted[:3]
        langs_str = ", ".join([f"{lang[0]} ({lang[1]}%)" for lang in top_langs])
        stats_lines.append(f"{G}Top Langs:{X}   {langs_str}")
else:
    stats_lines = [
        f"{G}Name:{X}        Gaurav Saikia",
        f"{G}Status:{X}      BCA Student · Open-Source Developer",
        f"{G}Location:{X}    India",
        f"{G}OS:{X}          Arch Linux / Windows",
        f"{G}Focus:{X}       Rust + GNOME · Three.js · Web Audio",
    ]

for i, line in enumerate(stats_lines):
    t.gen_text(line, row_num=11+i)
    t.clone_frame(3)

end_stats = 11 + len(stats_lines)
t.clone_frame(10)
t.gen_text(f"{C}========================={X}", row_num=end_stats)
t.clone_frame(15)

# -- Clear --
t.gen_prompt(row_num=end_stats+1)
t.gen_typing_text("clear", row_num=end_stats+1, contin=True, speed=1)
t.clone_frame(4)
t.clear_frame()

# -- Skills --
t.gen_prompt(row_num=1)
t.gen_typing_text("cat /home/dojo/arsenal.txt", row_num=1, contin=True, speed=1)
t.clone_frame(5)

t.gen_text("", row_num=2)
t.gen_text(f"{C}=== Arsenal ==={X}", row_num=3)
t.clone_frame(3)

skills = [
    (f"{R}Languages:{X}  ", "C, C++, Rust, Java, JS, Lua, Python, PHP"),
    (f"{R}Web:{X}       ", "HTML, CSS, Three.js, Canvas API, Web Audio"),
    (f"{R}Learning:{X}  ", "TypeScript, React, Node.js, Tailwind, PostgreSQL"),
    (f"{R}Tools:{X}     ", "Git, Neovim, Kitty, Figma, Blender, Photoshop"),
    (f"{R}OS:{X}        ", "Arch Linux · GNOME 50 · Windows"),
    (f"{R}Terminal:{X}  ", "Kitty, Oh My Posh, Bash, PowerShell"),
    (f"{R}Featured:{X}  ", "animanga-archive  (2.5k+ JS, 1.8k+ CSS)"),
]

for i, (label, value) in enumerate(skills):
    t.gen_text(f"{label}{value}", row_num=4+i)
    t.clone_frame(2)

t.clone_frame(10)

# -- Closing --
last_skill = 4 + len(skills)
t.gen_text(f"{C}==================={X}", row_num=last_skill)
t.clone_frame(5)

final_row = last_skill + 2
t.gen_prompt(row_num=final_row)
t.gen_typing_text("fortune | cowsay", row_num=final_row, contin=True, speed=1)
t.clone_frame(5)
t.gen_text(f"{G}  \"Every config intentional. Every detail version-controlled.\"{X}", row_num=final_row+1)
t.clone_frame(5)
t.gen_text(f"{R}  ~ Gaurav Saikia, Night Dojo{X}", row_num=final_row+2)
t.clone_frame(40)

t.gen_gif()

print("\nGIF generated: output.gif")
print("\nEmbed in README.md:")
print("![Terminal GIF](./output.gif)")
