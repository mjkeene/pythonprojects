import spacy
from spacy.tokens import Span
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

def get_event_and_time(text):
    doc = nlp(text)

    # Find named entities
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    # Find time expressions
    time_phrases = []
    for ent in entities:
        if ent[1] == "TIME":
            time_phrases.append(ent[0])
    
    # Find the event
    event = None
    for ent in entities:
        if ent[1] == "EVENT":
            event = ent[0]
            break

    if event is None:
        # if no explicit event was found, check if there's an action verb (e.g., "Remind me to [do something]")
        for token in doc:
            if token.pos_ == "VERB":
                event = token.text
                break

    if event is None:
        # if no event or action verb was found, the event is the full text
        event = text

    # Check for verb phrases in the dependency parse tree
    if event.lower() == "remind":
        for token in doc:
            if token.dep_ == "ROOT" and token.pos_ == "VERB":
                event = token.text
                break

    return event, time_phrases

# Example usage
text = "Remind me to go grocery shopping tonight at 7pm"
event, time_phrases = get_event_and_time(text)
print(f"Event: {event}")
print(f"Time phrases: {time_phrases}")





