'''import wx
 
app = wx.App()
 
# create frame using Frame() constructor
frame = wx.Frame(None, id = 10, title ="Frame", 
                      pos = wx.DefaultPosition,
                         size = wx.DefaultSize, 
                style = wx.DEFAULT_FRAME_STYLE,
                               name = "frame")
 
# show frame
frame.Show(True)
 
app.MainLoop()'''
#!/usr/bin/env python

import wx
import wx.aui as aui


text = """\
Hello!

Welcome to this little demo of draggable tabs using the aui module.

To try it out, drag a tab from the top of the window all the way to the bottom.  After releasing the mouse, the tab will dock at the hinted position.  Then try it again with the remaining tabs in various other positions.  Finally, try dragging a tab to an existing tab ctrl.  You'll soon see that very complex tab layouts may be achieved.
"""

#----------------------------------------------------------------------

class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        self.log = log
        wx.Panel.__init__(self, parent, -1)

        self.nb = aui.AuiNotebook(self)
        page = wx.TextCtrl(self.nb, -1, text, style=wx.TE_MULTILINE)
        self.nb.AddPage(page, "Welcome")

        for num in range(1, 5):
            page = wx.TextCtrl(self.nb, -1, "This is page %d" % num ,
                               style=wx.TE_MULTILINE)
            self.nb.AddPage(page, "Tab Number %d" % num)

        sizer = wx.BoxSizer()
        sizer.Add(self.nb, 1, wx.EXPAND)
        self.SetSizer(sizer)
        wx.CallAfter(self.nb.SendSizeEvent)

#----------------------------------------------------------------------

def runTest(frame, nb, log):
    win = TestPanel(nb, log)
    return win

#----------------------------------------------------------------------



overview = """<html><body>
<h2><center>Say something nice here</center></h2>

</body></html>
"""



if __name__ == '__main__':
    import sys,os
    import run
    run.main(['', os.path.basename(sys.argv[0])] + sys.argv[1:])
