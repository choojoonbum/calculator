# ch 5.2.1 ctrl.py

class Control:
    def __init__(self, view):
        self.view = view
        self.connectSignals()

    def connectSignals(self):
        self.view.btn1.clicked.connect(self.calculate)
        self.view.btn2.clicked.connect(self.view.clearMessage)

    def calculate(self):
        pass

    def sum(self, a, b) :
        try:
            return str(a + b)
        except:
            return "Calculation Error"

