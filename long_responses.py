import random

R_EATING = "8570253"
R_ADVICE = "57050"


def unknown():
    response = ["Bocsi, nem értettem jól ",
                "Mivan?",
                "Nem értem.",
                "hogy micsoda?"][
        random.randrange(4)]
    return response