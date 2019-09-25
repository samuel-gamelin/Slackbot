import argparse
import slack



def main():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-t', '--token', type=str, help='The Slack API token.')
    pass

if __name__ == '__main__':
    main()
