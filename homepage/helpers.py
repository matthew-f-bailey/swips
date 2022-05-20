from typing import Tuple, List
from random import sample

from homepage.models import Word
from homepage.exceptions import NotPossibleError

ALL_WORDS = [w.wordname for w in Word.objects.all()]

def get_words() -> Tuple[Word, Word]:
    """Randomly sample 2 words"""

    # Load in words
    words = list(Word.objects.all())  # Convert to list to sample from
    word1, word2 = sample(words, 2)  # Take 2 words
    return word1, word2


def is_one_away(w1, w2) -> bool:
    """Returns true if word1 is one away from word2"""
    diffs = 0
    for ltr_dict, ltr_cur in zip(w1, w2):
        if ltr_dict != ltr_cur:
            diffs+=1
    if diffs==1:
        return True
    return False


def calculate_optimal(total_iterations: List[list]):
    """
    We have a list of lists, each index in the outer list is
    the current iteration. Meaning the first one will have the
    start word. List 2 will be all the words 1 away from that. List
    3 will be all the words away from all those words. Each iteration
    gets exp. longer. We need to connect each iter from the
    prior to the current, recording words in common. This will
    be the optimal path
    """
    start = total_iterations[0][0]
    for i, iteration in enumerate(total_iterations[1:]):
        print(f"Iter {i}")
        print(iteration)


def get_minimal_swaps(word1: str, word2: str, max_swaps: int = 10):

    WORDS = [w.wordname for w in Word.objects.all()]

    print(f"Getting minimal swaps of {word1} and {word2}")
    # Get all words 1 away from word1
    cur_words = [word1]
    seen_words = []
    num_swaps = 0
    # TODO: Figure out optimal path to show to user
    for _ in range(max_swaps):
        one_away = []
        num_swaps += 1
        for cur_word in cur_words:
            # Get words that are 1 swap away
            one_away_this = [dw for dw in WORDS if is_one_away(dw, cur_word)]
            for x in one_away_this:
                if x not in seen_words:
                    one_away.append(x)

            seen_words += one_away

            if word2 in one_away:
                print("Found It")
                return num_swaps

        cur_words = one_away

    raise NotPossibleError()
