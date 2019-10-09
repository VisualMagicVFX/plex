# ****************************************************
# content = setup render settings in maya scene
# version = 1.0.0
# date    = 2019-10-06
#
# license = MIT
# author  = Alexander Richter <alexanderrichtertd.com>
#*********************************************************************


import os

import maya.cmds as cmds

from tank import Tank


#*********************************************************************
# VAR
TITLE = os.path.splitext(os.path.basename(__file__))[0]
LOG   = Tank().log.init(script=TITLE)


#*********************************************************************
# CLASS
class Rendersettings(object):

    def __init__(self):
        self.states = ["work", "preview", "publish", "custom"]

    def default(self):
        LOG.info('default')

    def work(self):
        LOG.info('work')


    def preview(self):
        LOG.info('preview')


    def publish(self):
        LOG.info('publish')


    def custom(self):
        LOG.info('custom')


    #*********************************************************************
    # CLASS
    def lowest(self):
        self.work()

    def highest(self):
        self.publish()


    #*********************************************************************
    # SETUP
    def setup(self, state="default"):
        if state != "custom": self.default()
        getattr(self, state, self.custom)()
