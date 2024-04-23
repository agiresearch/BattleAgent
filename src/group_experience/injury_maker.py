import random

injuries_info = {
    "Sword and Knife Wounds": {
        "Deep Lacerations": {
            "affected_areas": ["Arms", "Legs", "Torso"],
            "consequences": ["Deep cuts", "Muscle and bone damage", "Risk of vital organ damage"]
        },
        "Muscle and Ligament Damage": {
            "affected_areas": ["Shoulders", "Knees"],
            "consequences": ["Debilitating injuries", "Affects mobility"]
        },
        "Fractures": {
            "affected_areas": ["Hands", "Forearms", "Ribs"],
            "consequences": ["Bone fractures", "Potential damage to internal organs"]
        }
    },
    "Arrow Wounds": {
        "Penetration Injuries": {
            "affected_areas": ["Chest", "Abdomen"],
            "consequences": ["Internal bleeding", "Organ damage", "Fatal if vital organs are hit"]
        },
    },
    "Blunt Force Injuries": {
        "Blunt Trauma": {
            "affected_areas": ["Chest", "Abdomen", "Back"],
            "consequences": ["Internal bleeding", "Organ damage", "Spinal injuries"]
        },
        "Fractures": {
            "affected_areas": ["Skull", "Limbs"],
            "consequences": ["Bone fractures", "Brain injuries", "Impaired mobility"]
        },
        "Concussions and Head Injuries": {
            "affected_areas": ["Head"],
            "consequences": ["Concussions", "Traumatic brain injuries", "Death"]
        }
    }
}

injury_sentences = []
for injury_type, details in injuries_info.items():
    for injury, info in details.items():
        # Iterate through each affected area and its consequences
        for area in info["affected_areas"]:
            for consequence in info["consequences"]:
                # Formulate the sentence
                sentence = f"Due to {injury_type}, {area} become susceptible to {consequence}."
                injury_sentences.append(sentence)

def injury_generator(history, injury_sentences=injury_sentences, injury_chance=0.1):
    """
    Randomly selects an injury sentence with a 10% chance and saves it to the provided history list.
    
    Args:
    - history (list): The list where the selected injury sentence will be saved.
    
    Returns:
    - The selected injury sentence if one is selected, otherwise None.
    """
    # Determine if an injury should be selected based on 10% chance
    if random.random() <= injury_chance:
        # Randomly select an injury sentence
        selected_injury = random.choice(injury_sentences)
        # Save the selected injury to history
        history.append(selected_injury)
        return selected_injury
    else:
        return ""

if __name__ == "__main__":
    # Initialize an empty history list
    injury_history = []

    # Example usage of the function
    selected_injury_example = injury_generator(injury_history, injury_sentences, 0.9)
    print(selected_injury_example)
    print(type(selected_injury_example))
