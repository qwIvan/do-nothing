#!/usr/bin/true
import sys


class Nothing:
    def __call__(self, *args, **kwargs):
        return self

    def __getattr__(self, *args, **kwargs):
        return self

    def __getitem__(self, *args, **kwargs):
        return self

    def __iter__(self, *args, **kwargs):
        return iterator


class Iterator(Nothing):
    def __next__(self, *args, **kwargs):
        raise StopIteration

    def next(self, *args, **kwargs):
        raise StopIteration


iterator = Iterator()
nothing = Nothing()
sys.modules['nothing'] = nothing
