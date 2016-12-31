import os

sendPath = '/home/pi/raspberry-remote/send'

class Steckdose(object):
    def __init__(self, systemcode, unitcode):
        self.systemcode = systemcode
        self.unitcode = unitcode

    def switchOn(self):
        self._switch(1)

    def switchOff(self):
        self._switch(0)

    def _switch(self, switch):
        # switch: 0 = off, 1 = on
        cmd = '%s %s %s %d' % (sendPath, self.systemcode, self.unitcode, switch)
        #print cmd
        os.system(cmd)

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 4:
        print "usage: python %s systemCode unitCode onOff" % (sys.argv[0])
        sys.exit(1)

    steckdose = Steckdose(sys.argv[1], sys.argv[2])

    if int(sys.argv[3]):
        steckdose.switchOn()
    else:
        steckdose.switchOff()
