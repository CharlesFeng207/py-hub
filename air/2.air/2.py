# -*- encoding=utf8 -*-
__author__ = "Charles"

from airtest.core.api import *

auto_setup(__file__)

while True:
    touch(Template(r"tpl1581177507759.png", record_pos=(-0.238, -0.127), resolution=(1806, 864)))

    touch(Template(r"tpl1581177515988.png", record_pos=(-0.166, -0.023), resolution=(1806, 864)))

    sleep(2)
