# SMS Reminder Service

This project will have a chatbot that will send you a reminder in the form of an SMS notification at a given time.

Example: 
`Input: "Remind me about John's birthday next Wednesday at 5PM"`
`Output: "Sending you a reminder about John's birthday."`
The output is sent as an SMS message the following Wednesday at 5PM.

# Early Screenshots from Chatterbot




The chatbot wasn't very intelligent at first. 



# Switched over to ChatGPT-3.5-turbo

Sample console output from `chat_gpt.py`:

```
User : hi
Enter an event to be reminded about with a time, such as: 'Remind me to call John tonight at 6'
User : hey there 
Enter an event to be reminded about with a time, such as: 'Remind me to call John tonight at 6'
User : remind me to get an oil change tomorrow at noon 
Loop has executed 1 times
ChatGPT: {
    "event": "get an oil change",
    "timestamp": "2024-03-01 12:00:00 PST"
}
```

From here, an alert can be scheduled to be sent at the given datetime that is provided, and the SMS alert will be constructed with the event context. So you'll get a text at `2024-03-01 12:00:00 PST` saying something like `This is a reminder to get an oil change.`
