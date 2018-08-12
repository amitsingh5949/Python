from urllib.request import urlopen


def fetch_words_from_url():
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_word = []
        for line in story:
            for word in line.split():
                story_word.append(word.decode('utf-8'))
        print(story_word)


if(__name__ == '__main__'):   # __name__  is special attribute which evaluates to __main__ or actual module name
    fetch_words_from_url()