def languages():


    languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }
    for key, values in languages.items():
        print(f"{key} was created by {values}")


languages()
