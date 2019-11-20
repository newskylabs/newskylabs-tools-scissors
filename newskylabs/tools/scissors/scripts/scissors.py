"""newskylabs/tools/scissors/scripts/scissors.py:

Main of NewSkyLab's `scissors` tool.

Description:

A tool for recognizing and editing character bounding boxes and class annotations.

!!! Work in Progress !!!

Goal:

`scissors` is a tool to visualize, edit, and recognize bounding boxes
and character class annotations of printed and hand-written characters
in scanned texts.

Character bounding boxes together with the corresponding character
class annotations are an essential part of the data necessary to train
machine learning algorithms in optical character recognition (OCR)
tasks.

See:

  - Wikipedia: Optical character recognition
    https://en.wikipedia.org/wiki/Optical_character_recognition

For an example see the `Kuzushiji Recognition` kaggle project page:

  - Kuzushiji Recognition
    Opening the door to a thousand years of Japanese culture
    https://www.kaggle.com/c/kuzushiji-recognition/overview/about-kuzushiji

"""

__author__      = "Dietrich Bollmann"
__email__       = "dietrich@formgames.org"
__copyright__   = "Copyright 2019 Dietrich Bollmann"
__license__     = "Apache License 2.0, http://www.apache.org/licenses/LICENSE-2.0"
__date__        = "2019/10/19"

import click

## =========================================================
## Main
## ---------------------------------------------------------

@click.command()
def scissors():
    """A tool for recognizing and editing character bounding boxes and
    class annotations.

    """
    print("Hello Click Scissors :)")
    
## =========================================================
## =========================================================

## fin.
