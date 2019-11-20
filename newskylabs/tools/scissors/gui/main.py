"""newskylabs/tools/scissors/gui/main.py:

The GUI of the scissors tool.

"""

__author__      = "Dietrich Bollmann"
__email__       = "dietrich@formgames.org"
__copyright__   = "Copyright 2019 Dietrich Bollmann"
__license__     = "Apache License 2.0, http://www.apache.org/licenses/LICENSE-2.0"
__date__        = "2019/11/20"

import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.label import Label

## =========================================================
## Scissors GUI
## 
## class ScissorsApp
## ---------------------------------------------------------

class ScissorsApp(App):

    def build(self):
        return Label(text='Hello Scissors GUI :)')

## =========================================================
## =========================================================

## fin.
