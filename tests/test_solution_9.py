from ProjectEuler.src.p9.solution import *

def test_find_triplet():
    assert set(find_triplet(1000)) == set((200, 375, 425))
    assert set(find_triplet(12)) == set((3, 4, 5))
