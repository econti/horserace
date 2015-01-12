from classification import ClassifyModel
from fabric.colors import magenta

class Race():
    """ Initialize horserace object to beging horserace"""

    def __init__(self
                , pandas_dataframe
                , independent_vars
                , dependent_vars 
                , problem_type
                , folds=5):

        self.df = pandas_dataframe
        self.Xs = independent_vars
        self.Y = dependent_vars
        self.problem_type = problem_type
        self.folds = folds


    def go(self):        
        """ start horserace and score algorithms """

        if self.problem_type == 1:
            print magenta("|" * 20 + " And they're off! " + "|" * 20)
            # classification
            c = ClassifyModel(self)
            c.logistic_regression()
            c.knn()
            c.random_forest()

        elif self.problem_type == 2:
            # regression
            pass

        elif self.problem_type == 3:
            # clustering
            pass

        elif self.problem_type == 4:
            # dimensionailty reduction
            pass

        elif self.problem_type == 5:
            # recommendation
            pass

        else:
            raise ValueError('Problem type not defined properly.')
