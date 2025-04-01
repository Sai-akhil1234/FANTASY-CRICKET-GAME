# Define a class for CricketTeamMember
class CricketTeamMember:
    def __init__(self, name, role, description):
        self.name = name
        self.role = role
        self.description = description

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Description: {self.description}\n")

# Create instances of CricketTeamMember
team_members = [
    CricketTeamMember("Virat Kohli", "Batsman", "One of the best batsmen in the world, known for his exceptional technique and leadership skills."),
    CricketTeamMember("Jasprit Bumrah", "Bowler", "A skilled fast bowler with the ability to swing the ball both ways, making him a threat to opposing batsmen."),
    CricketTeamMember("Rohit Sharma", "Batsman", "A talented opening batsman with a strong record in international cricket, known for his elegant strokeplay."),
    CricketTeamMember("Ravindra Jadeja", "All-rounder", "A skilled all-rounder who contributes to the team with both his batting and bowling abilities, and is also an excellent fielder."),
    CricketTeamMember("MS Dhoni", "Wicket-keeper Batsman", "A legendary wicket-keeper batsman and former captain of the Indian cricket team, known for his exceptional leadership skills and finishing abilities."),
    CricketTeamMember("Ashwin","All-rounder","Ravichandran Ashwin is an Indian cricketer who is widely regarded as one of the best spin bowlers in the world. He is a right-arm off-spinner and is known for his ability to take wickets on any type of pitch. Ashwin has taken over 400 wickets in Test cricket and is one of the fastest bowlers to reach this milestone."),
    CricketTeamMember("Yuvraj","All-rounder","Yuvraj Singh is a former Indian cricketer who was a key player in India's 2011 World Cup-winning team."),
    CricketTeamMember("Pandey","Left handed middle-order batsman","Manish Pandey is an Indian cricketer who is a right-handed batsman and plays for the Indian national team, known for his impressive strokeplay and ability to finish matches."),
    CricketTeamMember("Dhawan","Left handed opening batter","Shikhar Dhawan is an Indian cricketer and opening batsman, known for his aggressive batting style and impressive performances in ICC tournaments."),
    CricketTeamMember("Karthik","Wicket-keeper","Dinesh Karthik is a former Indian cricketer, coach, and commentator who played for the India national cricket team and captained Tamil Nadu in domestic cricket. Born on June 1, 1985, Karthik made his debut for the Indian cricket team in 2004 and was known for his aggressive batting style and ability to finish games strong."),
    CricketTeamMember("Rahane","Batsman","Ajinkya Rahane is an Indian cricketer and former vice-captain of the Indian national team known for his solid batting technique and impressive performances in Test cricket.")
]

# Display team members' details
for i, member in enumerate(team_members, start=1):
    print(f"Team Member {i}:")
    member.display_details()
