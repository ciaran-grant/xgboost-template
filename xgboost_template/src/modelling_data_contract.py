from dataclasses import dataclass

@dataclass
class ModellingDataContract:
    """ Holds details for defining modelling terms in a single place.
    """
    
    ID_COL = ""
    RESPONSE = ""
    TRAIN_TEST_SPLIT_COL = ""

    feature_list = []
    
    monotone_constraints = {}
