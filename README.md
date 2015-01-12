# Horserace

Horserace is the easiest way to throw common machine learning algorithms at a data set and evaluate which performs the best.

Horserace supports the following types of problems:

  - classification
  - regression
  - clustering
  - dimensionality reduction
  - recommendation

#### Usage

```py
$ pip install horserace
```

```
$ from horserace.run_race import Race
$ race = Race(pandas_df, x_cols, y_cols, problem_type)
$ race.go()

|||||||||||||||||||| And they're off! ||||||||||||||||||||
Logistic regression: Accuracy: 0.50 (+/- 0.63)
KNN: Accuracy: 0.83 (+/- 0.28)
Random forest: Accuracy: 0.73 (+/- 0.32)
```

####Algorithms used
![Algorithm cheat sheet](http://scikit-learn.org/stable/_static/ml_map.png)