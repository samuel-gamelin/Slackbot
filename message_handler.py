import difflib
import re


available_commands = ['search', 'help']

with open('bot_help.md', 'r') as f:
    help_message = f.read()


def send_message(message, channel, web_client):
    """ str, slack.WebClient -> None

    Sends a message to a specific channel.
    """

    web_client.chat_postMessage(
        channel=channel,
        text=message
    )


def process_message(payload):
    """ dict -> None

    Processes a Slack message.
    """

    data = payload['data']

    if 'subtype' in data and data['subtype'] == 'bot_message' or not data['channel'].startswith('D'): # Ensure the bot isn't responding to itself and that it's only responding to direct messages
        return

    web_client = payload['web_client']
    channel = data['channel']
    message = data['text']

    _input = re.split(r'\s+', message)
    command = _input[0]
    arguments = _input[1:]

    if command == 'help':
        send_message(help_message, channel, web_client)
    
    elif command == 'search':
        send_message('Not ready yet!', channel, web_client)
        return
        website = arguments[0]
        query = ' '.join(arguments[1:])
        send_message(website, channel, web_client)
        send_message(query, channel, web_client)

    else:
        matches = difflib.get_close_matches(command, available_commands)
        if not matches or len(matches) > 1 or matches[0] == 'help':
            send_message("I don't recognize that command. Type in 'help' for a list of available commands.", channel, web_client)
        else:
            send_message("I don't recognize that command. Did you mean " + matches[0] + "? If not, type in 'help' for a list of available commands.", channel, web_client)
