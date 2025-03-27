def daily_meeting(team: list) -> str:
    return "\n".join([f"{member}: What did you do yesterday? What will you do today? Any blockers?" for member in team])
