#!/usr/bin/true
import sys


iterator = None


class Nothing(object):
    def __call__(self, *args, **kwargs):
        return self

    def __getattr__(self, *args, **kwargs):
        return self

    def __getitem__(self, *args, **kwargs):
        return self

    def __iter__(self, *args, **kwargs):
        return self.iterator

    def iter(self, *args, **kwargs):
        return self.iterator


class Iterator(Nothing):
    def __next__(self, *args, **kwargs):
        raise StopIteration

    def next(self, *args, **kwargs):
        raise StopIteration


Nothing.iterator = Iterator()
nothing = Nothing()
sys.modules['nothing'] = nothing
