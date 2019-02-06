import pytest
from tachycardia import is_tachycardic


@pytest.mark.parametrize("word, expected", [
                        ('Tachycardic', True),
                        ('tachyCardic', True),
                        ('TACHYCARDIC', True),
                        ('TACHYCARdIC', True),
                        ('TAcHycARdIC', True),
                        ('tACHYCARDIC', True),
                        ])
def test_cap_tachycardic(word, expected):
    answer = is_tachycardic(word)
    assert answer == expected


@pytest.mark.parametrize("word, expected", [
                        ('Tachycardi1c.', True),
                        ('tachyCardic!', True),
                        ('TACHYCARDIC !', True),
                        ('TACHYCARdIC ?', True),
                        ('!TAcHycARdIC (', True),
                        ('$tACHYCARDIC!!! 4', True),
                        ])
def test_punct_spaces_tachycardic(word, expected):
    answer = is_tachycardic(word)
    assert answer == expected


@pytest.mark.parametrize("word, expected", [
                        ('tech cardio', False),
                        ('tachy cards', False),
                        ('ACHY CARDIO!', False),
                        ('tech car?', False),
                        ('tetrahedron (', False),
                        ('cardiology!', False),
                        ])
def test_not_tachycardic(word, expected):
    answer = is_tachycardic(word)
    assert answer == expected


@pytest.mark.parametrize("word, expected", [
                        ('t a c h y c a r d i c', True),
                        ('T achycardic', True),
                        ('-  tachycardic', True),
                        ('tachycardic(arrhythmia)', True),
                        ('istachycardic', True),
                        ('Theyaretachycardic.', True),
                        ])
def test_format_tachycardic(word, expected):
    answer = is_tachycardic(word)
    assert answer == expected
