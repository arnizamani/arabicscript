from arabicscript import remove_combining_characters

def test_remove_combining_characters():
    assert remove_combining_characters('بَ') == 'ب'
    assert remove_combining_characters('ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ۝') == 'ٱلحمد لله رب ٱلعلمين۝'
    assert remove_combining_characters('English text Älv') == 'English text Älv'
