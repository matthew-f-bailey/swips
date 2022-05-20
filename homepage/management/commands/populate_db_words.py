from ctypes.wintypes import WORD
import json

from django.core.management.base import BaseCommand
from django.utils import timezone

from homepage.models import Word

class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):

        with open("word_definitions.json", "r") as fh:
            WORDS = json.load(fh)

        for wordname, definition in WORDS.items():
            noun_def = definition.get("Noun", [""])[0]
            verb_def = definition.get("Verb", [""])[0]
            adv_def = definition.get("Adverb", [""])[0]
            adj_def = definition.get("Adjective", [""])[0]

            word = Word(
                wordname = wordname,
                def_noun = noun_def,
                def_verb = verb_def,
                def_adverb = adv_def,
                def_adjective = adj_def,
            )
            word.save()