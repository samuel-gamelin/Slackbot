from googlesearch import search
from difflib import get_close_matches


def search_web(site, question, numberOfResults):
    """
    This function scraps google for results based on the website needed,
    the question, and the number of results required

    Arguments:
        site {[str]} -- [This will be used to search a specific website]
        question {[str]} -- [The question the user wants to ask]
        numberOfResults {[int]} -- [the number of links they want returned]

    Returns:
        [List(str)] -- [list of strings. returns the url returned by the google search]
    """

    query = get_website(site) + " " + question

    listOfLinks = []
    for links in search(query, tld="com", lang='en', num=numberOfResults, stop=numberOfResults, pause=2):
        listOfLinks.append(links)
    return links


def get_website(website):
    """[summary]

    Arguments:
        website {[type]} -- [description]

    Returns:
        [type] -- [description]
    """

    websites = ['site:stackoverflow.com', 'site:stackexchange.com', 'site:docs.oracle.com',
                'site:docs.python.org', 'site:quora.com', 'site:codeproject.com', '']

    realWebsite = websites[0]
    return realWebsite
