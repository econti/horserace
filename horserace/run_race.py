
class Race():
    """ Initialize horserace object to beging horserace"""

    def __init__(self
                , pandas_dataframe
                , independent_vars
                , dependent_vars 
                , problem_type):

        self.df = pandas_dataframe
        self.Xs = independent_vars
        self.Y = dependent_vars
        self.problem_type = problem_type


    def go(self):        
        """ start horserace and score algorithms """

        if self.problem_type == 1:
            # classification
            pass

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
