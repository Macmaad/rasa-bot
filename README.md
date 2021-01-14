# *Chat Bot*

## How to run: 
* To run the chatbot we need to have at leat python installed and pip. When we have that installed we just need to do the nexts steps (I suggest to use [python venv](https://docs.python.org/3/library/venv.html))
1. pip install rasa 
1. rasa train 

* After doing those two steps we can use the chatbot in diferent ways: 
1. Run it locally 
    1. rasa shell -m models --endpoints endpoints.ym 
        1. With this, the terminal will be receiving the messages and answering you. 
1. Run it to connect or use in other service: 
    1. rasa run -m models --endpoints endpoints.ym  
        1. With this you will be able to connect your chatbot to diferent services. 

*Note*: This bot is planned to run in slack using [ngrok](https://ngrok.com/docs). The ngrok sessiond lasts 2 hours so we need to keep updating the URL that slack uses. 

## Learning Process: 
* The bot uses a lightweighted db (sqlilte3) where it stores all the conversations with the users, this way we are able to see how the bot is choosing the correct answer and which questions does the user uses. This way we can start the learning process, adding more data to the intents and responses. 

## Example: 
* Shell Output: ![Shell](https://github.com/Macmaad/rasa-bot/blob/master/img/Screen%20Shot%202021-01-13%20at%2020.36.00.png)

* Slack Output: ![Slack](https://github.com/Macmaad/rasa-bot/blob/master/img/Screen%20Shot%202021-01-13%20at%2020.36.18.png)

## Read the docs: 

For a better understand about what rasa is doing or how to use it, please go to the [docs](https://rasa.com/docs/rasa/).
