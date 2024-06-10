from nlplogic.corenlp import get_phrases

def test_get_phrase():
    assert 'real madrid' in get_phrases("Real Madrid")
