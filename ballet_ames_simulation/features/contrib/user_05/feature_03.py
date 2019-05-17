from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["MS SubClass"]
transformer = [
    ballet.eng.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "MS Fill None"
feature = Feature(input=input, transformer=transformer, name=name)
