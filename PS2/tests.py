import math 

def test_cosine(cosine_fn):
    tests_passed = 0
    v1 = [0, 1, 1]
    v2 = [1, 0, 1]
    v3 = [0, 3, 0]

    assert math.isclose(round(cosine_fn(v1, v1), 4), 1), f'Cosine sim should be 1 if x1 = x2'
    tests_passed += 1

    assert math.isclose(round(cosine_fn(v1, v2), 4), 0.5), f'Cosine sim incorrect for x1: [0, 1, 1] and x2: [1, 0, 1]'
    tests_passed += 1 

    assert math.isclose(round(cosine_fn(v2, v3), 4), 0), f'Cosine sim incorrect for orthogonal vectors.'
    tests_passed += 1

    print(f'All tests passed!! 🎉')
    return 

def test_minkowski(mink_fn):
    v1 = [1, 2, 1]
    v2 = [1, 0, 13]

    assert math.isclose(round(mink_fn(v1, v1, 1), 4), 0), f'Minkowski distance should be 0 if x1 = x2'

    assert math.isclose(round(mink_fn(v1, v2, math.inf), 4), 12), f'Minkowski distance incorrect for p = math.inf'

    print(f'All tests passed!! 🎊')
    return 

