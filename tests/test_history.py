from calculator.history import HistoryManager

def test_history():
    hist = HistoryManager()
    hist.add_to_history("2+3", 5)
    assert len(hist.get_history()) == 1

