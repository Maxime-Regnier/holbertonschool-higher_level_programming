def generate_invitations(template, attendees):
    # Validations (15-20 lignes)
    if not isinstance(template, str):
        print(f"Erreur : Le template doit être une chaîne de caractères, pas {type(template).__name__}.")
        return
    
    if not isinstance(attendees, list):
        print(f"Erreur : attendees doit être une liste, pas {type(attendees).__name__}.")
        return
    
    for i, attendee in enumerate(attendees):
        if not isinstance(attendee, dict):
            print(f"Erreur : L'élément {i} n'est pas un dictionnaire.")
            return
    
    # Vérifier vides (5-10 lignes)
    if not template or template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return
    
    # Traitement (30-40 lignes)
    placeholders = ["name", "event_title", "event_date", "event_location"]
    
    for index, attendee in enumerate(attendees, start=1):
        personalized_content = template
        
        for placeholder in placeholders:
            value = attendee.get(placeholder, "N/A")
            if value is None:
                value = "N/A"
            personalized_content = personalized_content.replace(
                f"{{{placeholder}}}", 
                str(value)
            )
        
        output_filename = f"output_{index}.txt"
        try:
            with open(output_filename, 'w', encoding='utf-8') as file:
                file.write(personalized_content)
        except IOError as e:
            print(f"Erreur : {e}")