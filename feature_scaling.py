# This is a sample Python script.
import pandas as pd
from data_description import DataDescription
from sklearn.preprocessing import MinMaxScaler, StandardScaler

class FeatureScaling:
    # All the tasks associated with the feature scaling are in this class.
    tasks = [
            ]

    tasks_normalization = [
            ]

    tasks_standardization = [
           ]

    def __init__(self, data):
        self.data = data

    # Will perform normalization on specific columns or on whole dataset.
    def normalization(self):

        return

    # Will perform standardization on specific columns or on whole dataset.
    def standardization(self):

       return

    # main function of the FeatureScaling Class.
    def scaling(self):
        # Returns all the changes on the DataFrame.
        return


