from django.db import models


class Word(models.Model):

    wordname = models.CharField(unique=True, max_length=255, default="")
    def_noun = models.TextField(default="")
    def_verb = models.TextField(default="")
    def_adverb = models.TextField(default="")
    def_adjective = models.TextField(default="")

    def __str__(self) -> str:
        s = f"Word: {self.wordname}"
        s = s + f"\n   Noun: {self.def_noun}" if self.def_noun else s
        s = s + f"\n   Verb: {self.def_verb}" if self.def_verb else s
        s = s + f"\n   Adverb: {self.def_adverb}" if self.def_adverb else s
        s = s + f"\n   Adjective: {self.def_adjective}" if self.def_adjective else s
        return s
