import csscolors


def test_iterator():
    for name, code in csscolors.iterator():
        assert code.startswith("#")
