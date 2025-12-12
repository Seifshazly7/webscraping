
import requests
from bs4 import BeautifulSoup

url = "https://www.yallakora.com/match-center?date=12/7/2025"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

matches = []

sections = soup.find_all("div", class_="mc__section")

for section in sections:
    competition_title = section.find("h3")
    competition = competition_title.text.strip() if competition_title else "Unknown Competition"

    match_rows = section.find_all("div", class_="match-row")
    for match in match_rows:
        team_home = match.find("div", class_="team-home")
        team_away = match.find("div", class_="team-away")
        score = match.find("span", class_="score")
        time = match.find("span", class_="time")

        match_data = {
            "competition": competition,
            "team_home": team_home.text.strip() if team_home else "",
            "team_away": team_away.text.strip() if team_away else "",
            "score": score.text.strip() if score else "",
            "time": time.text.strip() if time else "",
        }
        matches.append(match_data)

for m in matches:
    print(f"{m['competition']} | {m['team_home']} vs {m['team_away']} | Score: {m['score']} | Time: {m['time']}")
