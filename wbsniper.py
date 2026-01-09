import webbrowser


while True:
    query = input("what do you want to look for? (press the x on the top to quit)").lower()

    webbrowser.open(f'https://www.google.com/search?q={query}')
    webbrowser.open(f'https://en.wikipedia.org/wiki/{query}')
    webbrowser.open(f'https://www.youtube.com/results?search_query={query}')

    input("done! press enter do to put in another query")