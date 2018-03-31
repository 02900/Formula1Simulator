# -*- coding: utf-8 -*-
#title           :  intro.py
#description     :  Intro of the program
#author          :  asciimatics example
#version         :  0.1
#python_version  :  2.7.14
#=======================================================================
from __future__ import division
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.particles import DropScreen
from asciimatics.exceptions import ResizeScreenError
from asciimatics.renderers import FigletText, SpeechBubble, Rainbow, Fire
from asciimatics.effects import Scroll, Mirage, Wipe, Cycle, Matrix, BannerText, Stars, Print
from random import randint

def demo(screen):
    effects = [
        Cycle(screen, FigletText("F1    Simulator ", font='big'), int(screen.height / 2 - 4)),
        Print(screen, SpeechBubble("Press 'X' to continue."), screen.height // 2 + 8, attr=Screen.A_BOLD),
        Print(screen, SpeechBubble("Made By Juan Ortiz"), screen.height // 2 + 10, attr=Screen.A_BOLD),
        Stars(screen, 200)
    ]
    screen.play([Scene(effects, 500)])


def Start ():
	Screen.wrapper(demo)
