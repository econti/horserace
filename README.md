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
from horserace.run_race import Race
race = Race(pandas_df, x_cols, y_cols, problem_type)
race.go()
```

####Algorithms used
![Algorithm cheat sheet](http://scikit-learn.org/stable/_static/ml_map.png)