from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSPortMessage (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSPortMessage.sendBeforeDate_)

if __name__ == "__main__":
    main()
