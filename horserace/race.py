
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
