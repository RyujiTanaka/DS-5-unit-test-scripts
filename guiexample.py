from arm_ds.debugger_v1 import Debugger
from arm_ds.debugger_v1 import DebugException
from javax.swing import (BoxLayout, ImageIcon, JButton, JFrame, JPanel,
        JPasswordField, JLabel, JTextArea, JTextField, JScrollPane,
        SwingConstants, WindowConstants)
from java.awt import Component, GridLayout

class guitest(object):

    def __init__(self):
        self.frame = JFrame("GUI Test")
        self.frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE) # EXIT_ON_CLOSE will terminate Eclipse

        self.loginPanel = JPanel(GridLayout(0,2))
        self.frame.add(self.loginPanel)

        self.dscmdField = JTextField('',15)
        self.loginPanel.add(JLabel("DS Command:", SwingConstants.RIGHT))
        self.loginPanel.add(self.dscmdField)

        self.loginButton = JButton('Run',actionPerformed=self.rundscmd)
        self.loginPanel.add(self.loginButton)

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
    print "GUI test"
    guitest() 
