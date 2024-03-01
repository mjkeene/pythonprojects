# SMS Reminder Service

This project will have a chatbot that will send you a reminder in the form of an SMS notification at a given time.

Example: 

`Input: "Remind me about John's birthday next Wednesday at 5PM"`

`Output: "Sending you a reminder about John's birthday."`

The output is sent as an SMS message the following Wednesday at 5PM.

# Early Screenshots from Chatterbot

![Screen Shot 2024-02-29 at 1 44 05 PM](https://github.com/mjkeene/pythonprojects/assets/48185875/7cd35135-5f3d-4d11-bcb8-2308bc085cf8)


The chatbot wasn't very intelligent at first. The lines with the `>` symbol are what I typed as input, and the chatbot's responses are immediately after it. I didn't really make much of an effort to train this, but I do think that this could become far better with proper training. This may be a better approach long-term since ChatGPT isn't free. 


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

# Screenshot from ChatGPT-3.5-turbo
ChatGPT is lightyears ahead of (untrained) chatterbot for parsing event queries -- see a somewhat ambiguous query below that was picked up. 

![Screen Shot 2024-02-29 at 6 52 04 PM](https://github.com/mjkeene/pythonprojects/assets/48185875/4c0f4ff7-0fc9-481c-951a-e78d5beeb6dc)


For more complex requests, this doesn't work perfectly, but it'll do for now.

![Screen Shot 2024-02-29 at 6 55 14 PM](https://github.com/mjkeene/pythonprojects/assets/48185875/242022ec-98c9-41a8-a00f-45319fd99d15)
