import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_NAME = "My name is chatbot aka Lakshay's project :)"
R_GOOD = "Focus on the step infront of you, not the whole staircase!"
R_STATUS = "I am single   .   HAQ SE SINGLE"
R_LOVE = "I love myself"
R_SERVE = "I serve for the one who loves me "
R_IDOL = "My idol is Alexa."

def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response