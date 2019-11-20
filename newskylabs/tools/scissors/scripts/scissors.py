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

# Check that Kivy has been installed
try:
    import kivy
except ModuleNotFoundError:
    error_msg = """
ERROR Kivy has not been installed!

Scissors relies on Kivy for its graphical user interface.

Kivy has to be installed manually.  Please follow the installation
instructions on the following page:

  - Kivy Docs > Getting Started > Installation
    https://kivy.org/doc/stable/gettingstarted/installation.html

"""
    import sys
    print(error_msg, file=sys.stderr)
    sys.exit(1)

from kivy.logger import Logger

import click

from newskylabs.tools.scissors.utils.generic import get_version_long
from newskylabs.tools.scissors.gui.main import ScissorsApp

## =========================================================
## Examples
## ---------------------------------------------------------
 
def print_examples():
    """Print examples."""
    print("""Examples:

scissors \\
  --image-dir     data/images \\
  --class-mapping data/class-mappings.csv \\
  --annotations   data/annotations.csv

""")

## =========================================================
## Main
## ---------------------------------------------------------

# -i, --image-dir
option_image_dir_help = "Directory with the text images."
option_image_dir_default = "data/images" # TODO Get the default data dir from the config.

# -m, --class-mapping
option_class_mapping_help = "A file mapping class labels to actual values."
option_class_mapping_default = "data/class-mappings.csv" # TODO Get the default data mapping file from the config.

# -a, --annotations
option_annotations_help = "A file with the character annotations (labels and bounding boxes)."
option_annotations_default = "data/annotations.csv" # TODO Get the default annotation file from the config.

# -e, --examples
option_examples_help = "Show some usage examples."
option_examples_default = False

@click.command()

@click.option('-i', '--image-dir',
              type=click.Path(exists=True), 
              default=option_image_dir_default,
              help=option_image_dir_help)

@click.option('-m', '--class-mapping',
              type=click.Path(exists=True), 
              default=option_class_mapping_default,
              help=option_class_mapping_help)

@click.option('-a', '--annotations',
              type=click.Path(exists=False), 
              default=option_annotations_default,
              help=option_annotations_help)

@click.option('-e', '--examples',
              is_flag=True,
              default=option_examples_default,
              help=option_examples_help)

@click.version_option(get_version_long(), '-V', '--version')

def scissors(image_dir, class_mapping, annotations, examples):
    """A tool for recognizing and editing character bounding boxes and
    class annotations.

    """

    # DEBUG
    Logger.debug('Setting up Scissors Logger: Hello Kivy Logger :)')

    # DEBUG
    print("")
    print("  - image_dir:     {}".format(image_dir))
    print("  - class_mapping: {}".format(class_mapping))
    print("  - annotations:   {}".format(annotations))
    print("")
    
    # Show examples?
    if examples:
        print_examples()
        exit()

    # Start the GUI
    scissors = ScissorsApp()
    scissors.run()

## =========================================================
## =========================================================

## fin.
