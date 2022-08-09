# -*- coding: utf-8 -*-


from .submodule import bar


def return_foo():
    return f"{bar.return_bar()}foo!{bar.return_bar()}"
