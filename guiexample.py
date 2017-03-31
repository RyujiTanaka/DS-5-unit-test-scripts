from arm_ds.debugger_v1 import Debugger
from arm_ds.debugger_v1 import DebugException
from javax.swing import JButton, JFrame, JPanel, JLabel, JTextField

class gui_example(object):

    def __init__(self):
        self.frame = JFrame("GUI example")
        # Do not define DS-5 debugger contexts here

    def initGUI(self, ec):
        self.dscmdEC = ec

        self.dscmdPanel = JPanel()
        self.frame.add(self.dscmdPanel)

        self.dscmdField = JTextField('',30)
        self.dscmdPanel.add(JLabel("DS Command:"))
        self.dscmdPanel.add(self.dscmdField)

        self.dscmdButton = JButton('Run',actionPerformed=self.rundscmd)
        self.dscmdPanel.add(self.dscmdButton)

        self.frame.pack()
        self.frame.setVisible(True)

    def rundscmd(self,event):
        dscmd = self.dscmdField.text
        print dscmd
        ec.executeDSCommand(dscmd)

if __name__ == '__main__':
    print "GUI example"

    # Obtain the first execution context
    debugger = Debugger()
    ec = debugger.getCurrentExecutionContext()

    gui = gui_example()
    gui.initGUI(ec)
