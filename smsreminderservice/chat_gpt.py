from openai import OpenAI
from datetime import datetime
import pytz

api_key = input("Input your API key: ")
client = OpenAI(api_key=api_key)

messages = [ {"role": "system", "content":
              f"You are an intelligent assistant that will set reminders. " +
              "Parse the following response for an \"event\", and a \"timestamp\"" +
              "to send a reminder. Convert the timestamp to YYYY-MM-DD HH:MM:SS PST. " +
              "Format the \"event\": and \"timestamp\" as a Python dictionary."} ]

count = 0
while True:
    message = input("User : ")
    # this is a basic proxy for valid input, i.e.,
    # "reminder to workout at 5" is about as short
    # as it gets
    if len(message.split()) < 5:
    	invalid_input_msg = ("Enter an event to be reminded about "
    	"with a time, such as: 'Remind me to call John tonight at 6'")
    	print(invalid_input_msg.replace("\n", " "))
    	continue

    current_datetime = datetime.now(pytz.timezone('US/Pacific')).strftime("%Y-%m-%d %H:%M:%S")
    message += f" Note that today's date and time is: {current_datetime}"
    count += 1
    print(f'Loop has executed {count} times')

    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
    reply = chat.choices[0].message.content 
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})
