#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created: 2024-03-09 17:15:13

def cprint(*args, color:str=None, reprint=False, noColorIfFile=False, **kwargs):
  colors = {
    "BLACK": "\033[30m",
    "RED": "\033[31m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[33m",
    "BLUE": "\033[34m",
    "PURPLE": "\033[35m",
    "CYAN": "\033[36m",
    "WHITE": "\033[37m"
  }
  reset = '\033[0m'
  if color is None or ("file" in kwargs.keys() and noColorIfFile):
    print(*args, **kwargs)
  else:
    if color.upper() not in colors.keys():
      raise ValueError('color must be RED, GREEN, YELLOW, BLUE, PURPLE, CYAN, WHITE')
    if "end" in kwargs.keys():
      kwargs["end"] = reset+kwargs["end"]
    else:
      kwargs["end"] = reset+"\n"
    end = kwargs["end"]
    kwargs["end"] = ""
    print(colors[color.upper()], **kwargs)
    kwargs["end"] = end
    print(*args, **kwargs)
  if reprint:
    kwargs["file"] = None
    cprint(*args, color=color, reprint=False, **kwargs)
