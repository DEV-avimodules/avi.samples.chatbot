#
# (c) A.V.I Technology 2017
#   Author: 0x520x430x32
#   Description: 
#       The loading point of any module.
#


def on_load(core):
    core.logger.info("ChatBot Example loaded!")


def on_unload(core):
    core.logger.info("ChatBot Example unloaded!")
