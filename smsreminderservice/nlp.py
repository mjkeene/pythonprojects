import transformers

"""
What kind of model do I need?

Not a summarizer.
Not sentiment analysis.

Do I even need AI for this? Kind of, but also could use re and manual logic FIRST, and then
if that doesn't work, then move on to AI. If all words in a given text are accounted for,
then you do not need AI. 

Ex: Remind me to call John at 5PM tomorrow.
[Action] Remind me to ... 
[Event] Call John
[DateTime -- also need TZ] at 5PM tomorrow

Common queries would probably be something like:
Remind me to...
Remind me about...
Reminder about...
Reminder to...

"""

# summarizer = transformers.pipeline("summarization", model = "google/pegasus-xsum")

print('done')
