from flair.data import Sentence
from flair.models import SequenceTagger

# Load the NER model
tagger = SequenceTagger.load('ner')

def get_event_and_time(text):
    # Create a flair Sentence object
    sentence = Sentence(text)

    # Run NER on the sentence
    tagger.predict(sentence)

    # Extract named entities
    entities = [(ent.text, ent.tag) for ent in sentence.get_spans('ner')]

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
    if event == "Remind":
        for token in doc:
            if token.dep_ == "ROOT" and token.pos_ == "VERB":
                event = token.text
                break

    return event, time_phrases

# Example usage
text = "Remind me to go grocery shopping tonight at 5pm"
event, time_phrases = get_event_and_time(text)
print(f"Event: {event}")
print(f"Time phrases: {time_phrases}")



