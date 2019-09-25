import argparse
import message_handler
import slack

from threading import Thread


@slack.RTMClient.run_on(event='message')
def handle_message(**payload):
    Thread(target=message_handler.process_message, args=(payload,)).start()

def main():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-t', '--token', type=str, required=True, help='The Slack API token.')
    
    args = parser.parse_args()

    rtm_client = slack.RTMClient(token=args.token)
    rtm_client.start()


if __name__ == '__main__':
    main()
