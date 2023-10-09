from preprocessing import preprocessing_function
from modelling_data_contract import ModellingDataContract

from sklearn.base import BaseEstimator, TransformerMixin

import pandas as pd
import numpy as np

class Preprocessor(BaseEstimator, TransformerMixin):
    """ Preprocessing class and functions for training inside50 model
    """
    
    def __init__(self):
        self.ModellingDataContract = ModellingDataContract
       
        
    def fit(self, X):

        # Missing Values
        
        # Scaling
        
        # Mappings
        
        # Keep only modelling columns
        self.modelling_cols = ModellingDataContract.feature_list
                        
        return self
    
    def transform(self, X):
        """ Applies transformations and preprocessing steps to dataframe.

        Args:
            X (Dataframe): Training or unseen data to transform.

        Returns:
            Dataframe: Transformed data with modelling columns and no missing values.
        """

        X = preprocessing_function(X)
        
        X_features = X[ModellingDataContract.feature_list]
                
        return X_features
    