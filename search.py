from googlesearch import search


def search_web(site, question, numberOfResults):
    """
    This function scrapes google for results based on the website needed,
    the question, and the number of results required.

    Arguments:
        site {[str]} -- [The website from which search results will be obtained]
        question {[str]} -- [The query to use as a search]
        numberOfResults {[int]} -- [the number of links to be returned]

    Returns:
        [List(str)] -- [Returns the URLs of the top results]
    """

    query = "site: " + site + " " + question
    listOfLinks = []
    for links in search(query, tld="com", lang='en', num=numberOfResults, stop=numberOfResults, pause=2):
        listOfLinks.append(links)
    return listOfLinks
