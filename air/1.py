# -*- encoding=utf8 -*-
__author__ = "Charles"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
            "Android://127.0.0.1:5037/127.0.0.1:7555",
    ], project_root="C:/repos/py-hub/air")


# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)