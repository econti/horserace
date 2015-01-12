from sklearn import cross_validation
from sklearn import linear_model
from fabric.colors import magenta, green
from sklearn.neighbors import KNeighborsClassifier

class ClassifyModel():
    """generic class of a machine learning model"""


    def __init__(self, race):
        self.X_names = race.Xs
        self.Y_names = race.Y
        self.X = race.df[race.Xs].values
        self.y = race.df[race.Y].values
        self.folds = race.folds


    def validate(self, model):
        """
        use k fold cross-validation to validate model
        """
        scores = cross_validation.cross_val_score(model, self.X, self.y, cv=self.folds)
        avg, std = scores.mean(), scores.std()
        return avg, std


    def logistic_regression(self):
        """
        run logistic_regression
        """
        logreg = linear_model.LogisticRegression()
        avg, std = self.validate(logreg)
        print "Logistic regression: Accuracy: %0.2f (+/- %0.2f)" % (avg, std * 2)

    def knn(self):
        """
        run knn
        """
        knn_model = KNeighborsClassifier()
        avg, std = self.validate(knn_model)
        print "KNN: Accuracy: %0.2f (+/- %0.2f)" % (avg, std * 2)        