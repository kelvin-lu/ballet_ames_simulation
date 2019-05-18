from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["BsmtFin Type 2"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="NoBsmt"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Rating of basement finished area (if multiple types) type"
feature = Feature(input=input, transformer=transformer, name=name)
