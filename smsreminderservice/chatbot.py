"""This ChatBot that will respond to reminder requests via SMS (eventually), email first."""
# https://realpython.com/build-a-chatbot-python-chatterbot/
# https://chatterbot.readthedocs.io/en/stable/examples.html

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
# from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot(
	"EmailReminderBot",
	logic_adapters=[
		"chatterbot.logic.MathematicalEvaluation",
		"chatterbot.logic.TimeLogicAdapter",
		"chatterbot.logic.BestMatch"
	]
)

# trainer = ChatterBotCorpusTrainer(chatbot)

# trainer.train(
# 	"chatterbot.corpus.english.greetings"
# 	)

trainer = ListTrainer(chatbot)
trainer.train([
	"Hi",
	"Welcome, friend 😊. You can send me requests to set reminders at a specific time!"
	])
trainer.train([
	"Hey",
	"Welcome, friend 😊. You can send me requests to set reminders at a specific time!"
	])
trainer.train([
	"Hey there",
	"Welcome, friend 😊. You can send me requests to set reminders at a specific time!"
	])
trainer.train([
	"Yo!",
	"Welcome, friend 😊. You can send me requests to set reminders at a specific time!"
	])
trainer.train([
	"Set me a reminder for something at 5PM tonight.",
	"Consider it done!"
	])
trainer.train([
	"Are you a plant?",
	"No, I'm the pot below the plant!"
	])

exit_conditions = ("q", "quit", "exit", "stop")
while True:
	query = input("> ")
	if query in exit_conditions:
		break
	else:
		print(f"🤖 {chatbot.get_response(query)}")

