from arm_ds.debugger_v1 import Debugger
from arm_ds.debugger_v1 import DebugException
from javax.swing import JButton, JFrame, JPanel, JLabel, JTextField

class gui_example(object):

    def __init__(self):
        self.frame = JFrame("GUI example")

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

        # Obtain the first execution context
        debugger = Debugger()
        ec = debugger.getCurrentExecutionContext()
        ec.executeDSCommand(dscmd)

if __name__ == '__main__':
    print "GUI example"
    gui_example() 
