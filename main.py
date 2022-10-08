from data_description import DataDescription
from feature_scaling import FeatureScaling

class Preprocessor:

    # The Task associated with this class. This is also the main class of the project.
    tasks = [
           ]

    data = 0

    def __init__(self):
        self.data = None #constructor to assign input data

    # function to remove the target column of the DataFrame.
    def removeTargetColumn(self):

        return

    def printData(self):
        print(self.data)

    # main function of the Preprocessor class.
    def preprocessorMain(self):
        return



# obj is the object of our Preprocessor class(main class).
obj = Preprocessor()
# the object 'obj' calls the main function of our Preprocessor class.
obj.preprocessorMain()