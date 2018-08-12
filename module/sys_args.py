"""
Retrieves the words from a given url
"""
import sys
from urllib.request import urlopen


def fetch_words_from_url(url):
    """
    function to fetch words from url
    :param url: takes url as str
    :return: void but prints the wrds extracted from the url
    """
    with urlopen(url) as story:
        story_word = []
        for line in story:
            for word in line.split():
                story_word.append(word.decode('utf-8'))
        print(story_word)


if __name__ == '__main__':  # __name__  is special attribute which evaluates to __main__ or actual module name
    print(sys.argv[0])  # /home/amit/Amit-Files/python-workspace/PythonBasics/module/sys_args.py
    fetch_words_from_url(sys.argv[1])  # 0th argument is the module file name