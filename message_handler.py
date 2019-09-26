import difflib
import re
import search


available_commands = ['search', 'help']
available_websites = ['stackoverflow.com', 'stackexchange.com', 'docs.oracle.com', 'docs.python.org', 'quora.com', 'codeproject.com']
website_map = {
    'so': 'stackoverflow.com',
    'ex': 'stackexchange.com',
    'doc-java': 'docs.oracle.com',
    'doc-python': 'docs.python.org',
    'quora': 'quora.com',
    'cp': 'codeproject.com'
}

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
        try:
            website = arguments[0]
            query = ' '.join(arguments[1:])
        except:
            send_message('Invalid arguments. Type help for assistance with this command.', channel, web_client)
            return

        if website in website_map:
            website = website_map[website]
        elif website not in website_map.values():
            send_message('Website or acronym not supported!', channel, web_client)
            return
        
        send_message('\n'.join(search.search_web(website, query, 3)), channel, web_client)

    else:
        matches = difflib.get_close_matches(command, available_commands)
        if not matches or len(matches) > 1 or matches[0] == 'help':
            send_message("I don't recognize that command. Type in 'help' for a list of available commands.", channel, web_client)
        else:
            send_message("I don't recognize that command. Did you mean " + matches[0] + "? If not, type in 'help' for a list of available commands.", channel, web_client)
