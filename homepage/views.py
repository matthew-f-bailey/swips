from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate

from homepage.models import Word
from homepage.exceptions import NotPossibleError
from homepage.helpers import get_words, get_minimal_swaps, ALL_WORDS



def index(request):
    """Return the single page, ready to make ajax calls"""
    return render(
        request,
        'index.html',
        {}
    )

def game(request):
    """Handles the initial loading of the page"""

    user = authenticate(username='john', password='secret')
    if user is not None:
        pass
    else:
        pass

    # Verify that its possible for us to make the swap
    while True:
        try:
            word1, word2 = get_words()  # Get rando words
            # Verify that the words are possible
            min_swaps = get_minimal_swaps(
                word1=word1.wordname,
                word2=word2.wordname,
                max_swaps=5  # Will toss NotPossibleError if goes over this
            )
        except NotPossibleError:
            print("Dang... Lets go again")
            continue
        break

    print(f"Min num swaps of '{word1.wordname}' to '{word2.wordname}' is {min_swaps}")

    return render(
        request,
        'game.html',
        dict(
            word1=word1,
            word2=word2,
            guess_word=word2.wordname,
            min_possible_swaps=min_swaps
        )
    )

def guess(request):
    """API request to check on the new word and update"""

    guessed_word = request.GET.get('guessed_word')  # The word with 1 ltr changed
    past_word = request.GET.get('past_word')  # The old word
    final_word = request.GET.get('final_word')  # What they need to get to

    # Set default of them being wrong
    new_word = past_word
    win = False

    # If its a good word, update res
    if guessed_word in ALL_WORDS:
        print(f"VALID WORD FOUND = {guessed_word}")
        new_word = guessed_word

    # Check for a win
    if new_word == final_word:
        win = True

    # Grab the objects containing definitions
    word_obj1 = Word.objects.get(wordname=new_word)
    word_obj2 = Word.objects.get(wordname=final_word)

    return render(
        request,
        'words.html',
        dict(
            word1=word_obj1,
            word2=word_obj2,
            guess_word=word_obj2.wordname,
            win=win
        )
    )
