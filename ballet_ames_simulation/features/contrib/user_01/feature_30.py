from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Electrical"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Electrical type"
feature = Feature(input=input, transformer=transformer, name=name)
