# Slackbot
A simple Slack bot that returns search results for programming websites.

### Requirements
- Python 3
- A [Slack bot user](https://api.slack.com/bot-users) installed in a Slack workplace of your choice and its associated [bot user token](https://api.slack.com/authentication/token-types#granular_bot)

### Setup

1. Clone the repository and enter the new directory
```
git clone https://github.com/samuel-gamelin/Slackbot && cd Slackbot
```

2. Install the Python dependencies in the `requirements.txt` file (shown here using pip). The use of [virtualenv](https://virtualenv.pypa.io/en/latest/) is recommended.
```
pip3 install -r requirements
```

3. Run the bot
```
python3 bot.py --token <Slack API Token>
```

### Usage
In a Slack channel where the bot is present, it will respond to any messages beginning with an exclamation point (!). There are currently two available commands:
- `!search`
- `!help`
