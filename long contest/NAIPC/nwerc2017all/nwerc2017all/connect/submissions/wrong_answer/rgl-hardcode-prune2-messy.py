#!/usr/bin/env python
from math import hypot

#
# Intentionally avoids trying to keep the answer "neat" with corners
# close to vertices, by having a cost function of -distance_to_vertex
#

pts = [(0.0, 0.0), (0.0, 1.0), (0.0, 2.0), (0.0, 3.0), (0.0, -1.0), (0.0, -2.0), (0.0, -3.0), (0.0, -0.5), (0.0, -1.5), (0.0, 1.5), (0.0, 0.5), (0.0, 4.0), (0.0, 2.5), (0.0, 6.0), (0.0, 5.0), (0.0, 4.5), (0.0, 3.5), (0.0, -4.0), (0.0, -6.0), (0.0, 9.0), (0.0, 7.0), (1.0, 0.0), (-1.0, 0.0), (-0.5, 0.0), (2.0, 0.0), (-2.0, 0.0), (3.0, 0.0), (-3.0, 0.0), (-1.5, 0.0), (4.0, 0.0), (-4.0, 0.0), (6.0, 0.0), (-6.0, 0.0), (1.5, 0.0), (4.5, 0.0), (9.0, 0.0), (0.5, 0.0), (5.0, 0.0), (2.5, 0.0), (7.0, 0.0), (3.5, 0.0), (0.5, 0.5), (1.0, 1.0), (-1.0, -1.0), (0.6666666666666666, 0.6666666666666666), (2.0, 2.0), (0.75, 0.75), (1.5, 1.5), (3.0, 3.0), (1.3333333333333333, 1.3333333333333333), (4.0, 4.0), (1.2, 1.2), (1.8, 1.8), (2.25, 2.25), (1.6666666666666667, 1.6666666666666667), (2.3333333333333335, 2.3333333333333335), (2.5, 2.5), (0.3333333333333333, 0.6666666666666666), (0.5, 1.0), (1.0, 2.0), (0.4, 0.8), (0.6666666666666666, 1.3333333333333333), (0.42857142857142855, 0.8571428571428571), (0.6, 1.2), (0.75, 1.5), (2.0, 4.0), (0.8, 1.6), (1.3333333333333333, 2.6666666666666665), (0.8571428571428571, 1.7142857142857142), (1.2, 2.4), (1.5, 3.0), (1.125, 2.25), (1.2857142857142858, 2.5714285714285716), (-1.0, -2.0), (3.0, 6.0), (-0.3333333333333333, -0.6666666666666666), (-3.0, -6.0), (1.25, 2.5), (1.4, 2.8), (-2.0, -4.0), (6.0, 12.0), (1.8, 3.6), (1.75, 3.5), (1.6666666666666667, 3.3333333333333335), (0.25, 0.75), (0.3333333333333333, 1.0), (0.5, 1.5), (1.0, 3.0), (0.2857142857142857, 0.8571428571428571), (0.4, 1.2), (0.3, 0.9), (0.375, 1.125), (0.42857142857142855, 1.2857142857142858), (0.6666666666666666, 2.0), (0.5714285714285714, 1.7142857142857142), (0.8, 2.4), (0.5454545454545454, 1.6363636363636365), (0.6, 1.8), (0.75, 2.25), (0.8571428571428571, 2.5714285714285716), (0.8181818181818182, 2.4545454545454546), (0.9, 2.7), (-0.5, -1.5), (-2.0, -6.0), (-0.2, -0.6), (-1.0, -3.0), (0.2, 0.6), (0.7142857142857143, 2.142857142857143), (2.0, 6.0), (-4.0, -12.0), (-3.0, -9.0), (1.2, 3.6), (1.5, 4.5), (1.4, 4.2), (1.25, 3.75), (3.0, 9.0), (0.6666666666666666, 0.3333333333333333), (2.0, 1.0), (-2.0, -1.0), (-0.6666666666666666, -0.3333333333333333), (1.0, 0.5), (1.2, 0.6), (6.0, 3.0), (-6.0, -3.0), (0.8, 0.4), (1.3333333333333333, 0.6666666666666666), (4.0, 2.0), (-4.0, -2.0), (1.7142857142857142, 0.8571428571428571), (2.4, 1.2), (12.0, 6.0), (0.8571428571428571, 0.42857142857142855), (1.5, 0.75), (3.0, 1.5), (2.5714285714285716, 1.2857142857142858), (3.6, 1.8), (1.6, 0.8), (2.5, 1.25), (2.6666666666666665, 1.3333333333333333), (2.25, 1.125), (3.5, 1.75), (2.8, 1.4), (3.3333333333333335, 1.6666666666666667), (0.4, 0.6), (0.6666666666666666, 1.0), (2.0, 3.0), (-2.0, -3.0), (0.5, 0.75), (1.0, 1.5), (0.5454545454545454, 0.8181818181818182), (0.8571428571428571, 1.2857142857142858), (1.2, 1.8), (0.5714285714285714, 0.8571428571428571), (0.8, 1.2), (1.3333333333333333, 2.0), (4.0, 6.0), (0.9230769230769231, 1.3846153846153846), (1.0909090909090908, 1.6363636363636365), (1.7142857142857142, 2.5714285714285716), (1.5, 2.25), (1.3846153846153846, 2.076923076923077), (1.6363636363636365, 2.4545454545454546), (-0.5, -0.75), (0.75, 1.125), (1.1428571428571428, 1.7142857142857142), (1.25, 1.875), (1.4285714285714286, 2.142857142857143), (1.6, 2.4), (1.75, 2.625), (-4.0, -6.0), (8.0, 12.0), (6.0, 9.0), (3.0, 4.5), (0.75, 0.25), (3.0, 1.0), (-1.5, -0.5), (-0.6, -0.2), (1.2, 0.4), (-6.0, -2.0), (1.5, 0.5), (-3.0, -1.0), (0.8571428571428571, 0.2857142857142857), (6.0, 2.0), (2.4, 0.8), (-12.0, -4.0), (2.0, 0.6666666666666666), (0.9, 0.3), (1.2857142857142858, 0.42857142857142855), (2.25, 0.75), (9.0, 3.0), (1.6363636363636365, 0.5454545454545454), (3.6, 1.2), (4.5, 1.5), (1.0, 0.3333333333333333), (1.125, 0.375), (0.6, 0.2), (1.8, 0.6), (1.7142857142857142, 0.5714285714285714), (-9.0, -3.0), (2.142857142857143, 0.7142857142857143), (2.4545454545454546, 0.8181818181818182), (4.2, 1.4), (2.5714285714285716, 0.8571428571428571), (2.7, 0.9), (3.75, 1.25), (0.6, 0.4), (1.5, 1.0), (-3.0, -2.0), (-0.75, -0.5), (0.8571428571428571, 0.5714285714285714), (6.0, 4.0), (1.0, 0.6666666666666666), (3.0, 2.0), (0.75, 0.5), (1.2, 0.8), (-6.0, -4.0), (1.7142857142857142, 1.1428571428571428), (12.0, 8.0), (2.0, 1.3333333333333333), (0.8181818181818182, 0.5454545454545454), (1.125, 0.75), (1.8, 1.2), (4.5, 3.0), (1.3846153846153846, 0.9230769230769231), (2.5714285714285716, 1.7142857142857142), (2.25, 1.5), (1.2857142857142858, 0.8571428571428571), (2.142857142857143, 1.4285714285714286), (9.0, 6.0), (1.6363636363636365, 1.0909090909090908), (1.875, 1.25), (2.4, 1.6), (2.076923076923077, 1.3846153846153846), (2.4545454545454546, 1.6363636363636365), (2.625, 1.75), (-1.0, 2.0), (-0.5, 1.5), (-2.0, 3.0), (-0.6666666666666666, 1.6666666666666665), (-3.0, 4.0), (-1.5, 2.5), (-0.75, 1.75), (2.0, -1.0), (4.0, -3.0), (-4.0, 5.0), (-6.0, 7.0), (3.0, -2.0), (-0.3333333333333333, 1.3333333333333333), (2.5, -1.5), (7.0, -6.0), (-5.0, 6.0), (1.5, -0.5), (1.6666666666666667, -0.6666666666666667), (1.75, -0.75), (1.3333333333333333, -0.33333333333333326), (5.0, -4.0), (6.0, -5.0), (-1.0, 1.0), (-2.0, 1.0), (-3.0, 1.0), (1.3333333333333333, 1.0), (4.0, 1.0), (6.0, 1.0), (1.6666666666666667, 1.0), (2.3333333333333335, 1.0), (5.0, 1.0), (2.5, 1.0), (2.6666666666666665, 1.0), (0.3333333333333333, 1.3333333333333333), (0.6666666666666666, 1.6666666666666665), (0.6, 1.6), (0.75, 1.75), (1.5, 2.5), (0.8, 1.8), (1.3333333333333333, 2.333333333333333), (1.2, 2.2), (3.0, 4.0), (5.0, 6.0), (1.25, 2.25), (1.4, 2.4), (1.6666666666666667, 2.666666666666667), (3.5, 4.5), (4.0, 5.0), (0.25, 1.5), (0.3333333333333333, 1.6666666666666665), (0.5, 2.0), (0.4, 1.8), (0.6666666666666666, 2.333333333333333), (0.375, 1.75), (0.42857142857142855, 1.8571428571428572), (0.6, 2.2), (0.5714285714285714, 2.142857142857143), (0.8, 2.6), (0.75, 2.5), (0.8571428571428571, 2.7142857142857144), (4.0, 9.0), (-5.0, -9.0), (0.2, 1.4), (-0.3333333333333333, 0.33333333333333337), (2.0, 5.0), (-3.0, -5.0), (7.0, 15.0), (1.25, 3.5), (1.6, 4.2), (1.5, 4.0), (1.3333333333333333, 3.6666666666666665), (3.0, 7.0), (-2.0, 2.0), (-0.6666666666666666, 1.3333333333333333), (-1.0, 1.5), (6.0, -2.0), (-6.0, 4.0), (-1.2, 1.6), (0.8, 0.6), (1.3333333333333333, 0.33333333333333337), (4.0, -1.0), (-4.0, 3.0), (12.0, -5.0), (-12.0, 7.0), (1.1428571428571428, 0.4285714285714286), (1.5, 0.25), (1.25, 0.375), (-0.5, 1.25), (2.6666666666666665, -0.33333333333333326), (3.5, -0.75), (1.6, 0.19999999999999996), (3.3333333333333335, -0.6666666666666667), (3.2, -0.6000000000000001), (8.0, -3.0), (3.0, -0.5), (0.8571428571428571, 1.4285714285714286), (1.2, 1.6), (0.5714285714285714, 1.2857142857142856), (0.8, 1.4), (1.3333333333333333, 1.6666666666666665), (4.0, 3.0), (1.7142857142857142, 1.8571428571428572), (2.4, 2.2), (1.6, 1.8), (2.5, 2.25), (0.5, 1.25), (1.5, 1.75), (1.4285714285714286, 1.7142857142857144), (1.75, 1.875), (3.3333333333333335, 2.666666666666667), (2.8, 2.4), (2.6666666666666665, 2.333333333333333), (2.2857142857142856, 2.142857142857143), (3.0, 2.5), (0.6, 0.8), (-3.0, 2.0), (-0.75, 1.25), (6.0, -1.0), (-1.2, 1.4), (-1.5, 1.5), (-6.0, 3.0), (1.7142857142857142, 0.4285714285714286), (12.0, -3.0), (1.2857142857142858, 0.5714285714285714), (1.8, 0.4), (1.3636363636363635, 0.5454545454545454), (0.8571428571428571, 0.7142857142857143), (9.0, -2.0), (-0.6, 1.2), (1.875, 0.375), (2.4, 0.19999999999999996), (4.5, -0.5), (15.0, -4.0), (2.0, 0.33333333333333337), (2.25, 0.25), (2.142857142857143, 0.2857142857142857), (2.1, 0.30000000000000004), (3.6, -0.19999999999999996), (0.42857142857142855, 1.1428571428571428), (0.75, 1.25), (-1.5, 0.5), (1.2, 1.4), (-6.0, -1.0), (1.0, 1.3333333333333333), (1.0909090909090908, 1.3636363636363638), (2.4, 1.8), (2.0, 1.6666666666666665), (1.8, 1.6), (9.0, 4.0), (2.142857142857143, 1.7142857142857144), (1.2857142857142858, 1.4285714285714286), (1.7142857142857142, 1.5714285714285714), (2.25, 1.75), (1.9090909090909092, 1.6363636363636362), (4.5, 2.5), (2.625, 1.875), (2.5714285714285716, 1.8571428571428572), (0.375, 1.25), (0.6, 1.4), (1.5, 2.0), (0.8571428571428571, 1.5714285714285714), (6.0, 5.0), (1.0, 1.6666666666666665), (0.5454545454545454, 1.3636363636363638), (0.9230769230769231, 1.6153846153846154), (1.7142857142857142, 2.142857142857143), (2.0, 2.333333333333333), (2.25, 2.5), (-9.0, -5.0), (1.125, 1.75), (1.2857142857142858, 1.8571428571428572), (1.3636363636363635, 1.9090909090909092), (1.8, 2.2), (1.6153846153846154, 2.0769230769230766), (2.142857142857143, 2.428571428571429), (9.0, 7.0), (3.75, 3.5), (1.875, 2.25), (2.1818181818181817, 2.4545454545454546), (2.4, 2.6), (-1.0, 4.0), (-0.5, 3.0), (-2.0, 6.0), (-0.6666666666666666, 3.333333333333333), (-0.75, 3.5), (-0.6, 3.2), (-0.3333333333333333, 2.6666666666666665), (0.2, 1.6), (4.0, -6.0), (-5.0, 12.0), (2.0, -2.0), (1.3333333333333333, -0.6666666666666665), (1.5, -1.0), (1.6, -1.2000000000000002), (1.25, -0.5), (7.0, -12.0), (-3.0, 8.0), (3.0, -4.0), (-1.0, 3.0), (-2.0, 4.0), (-3.0, 5.0), (-1.5, 3.5), (1.25, 0.75), (1.6666666666666667, 0.33333333333333326), (1.4, 0.6000000000000001), (3.0, -1.0), (5.0, -3.0), (4.0, -2.0), (3.5, -1.5), (0.3333333333333333, 2.0), (1.6666666666666667, 2.0), (5.0, 2.0), (2.3333333333333335, 2.0), (2.6666666666666665, 2.0), (2.5, 2.0), (0.25, 2.25), (0.3333333333333333, 2.3333333333333335), (0.5, 2.5), (0.4, 2.4), (0.6666666666666666, 2.6666666666666665), (0.6, 2.6), (0.75, 2.75), (2.5, 4.5), (-5.0, -3.0), (7.0, 9.0), (3.0, 5.0), (-0.3333333333333333, 1.6666666666666667), (6.0, 8.0), (5.0, 7.0), (1.3333333333333333, 3.333333333333333), (1.75, 3.75), (1.6666666666666667, 3.666666666666667), (1.5, 3.5), (-6.0, 5.0), (1.6, 1.2), (1.4285714285714286, 1.2857142857142856), (2.5, 0.75), (1.75, 1.125), (1.5, 1.25), (0.5, 1.75), (2.6666666666666665, 0.6666666666666667), (2.2857142857142856, 0.8571428571428572), (2.8, 0.6000000000000001), (3.3333333333333335, 0.33333333333333326), (3.0, 0.5), (0.2857142857142857, 2.142857142857143), (0.4, 2.2), (0.5, 2.25), (1.0, 2.5), (0.8571428571428571, 2.4285714285714284), (1.2, 2.6), (2.6666666666666665, 3.333333333333333), (3.5, 3.75), (-0.5, 1.75), (1.1428571428571428, 2.571428571428571), (1.25, 2.625), (1.5, 2.75), (8.0, 6.0), (3.2, 3.6), (3.3333333333333335, 3.666666666666667), (1.6, 2.8), (3.0, 3.5), (0.42857142857142855, 1.7142857142857144), (-1.5, 3.0), (-6.0, 6.0), (1.8, 0.8), (1.3636363636363635, 1.0909090909090908), (2.142857142857143, 0.5714285714285714), (1.6153846153846154, 0.9230769230769231), (1.125, 1.25), (1.2857142857142858, 1.1428571428571428), (2.25, 0.5), (-9.0, 8.0), (2.4, 0.3999999999999999), (2.1818181818181817, 0.5454545454545454), (1.875, 0.75), (3.75, -0.5), (9.0, -4.0), (0.375, 1.875), (-3.0, 3.0), (2.25, 1.25), (1.7142857142857142, 1.4285714285714286), (1.9090909090909092, 1.3636363636363638), (1.2857142857142858, 1.5714285714285714), (1.8, 1.4), (2.142857142857143, 1.2857142857142856), (9.0, -1.0), (2.5714285714285716, 1.1428571428571428), (2.625, 1.125), (4.5, 0.5), (0.3, 2.1), (0.42857142857142855, 2.142857142857143), (0.5454545454545454, 2.1818181818181817), (1.0, 2.3333333333333335), (4.5, 3.5), (2.4, 2.8), (1.875, 2.625), (15.0, 7.0), (1.8, 2.6), (-0.6, 1.8), (9.0, 5.0), (0.8571428571428571, 2.2857142857142856), (1.2857142857142858, 2.4285714285714284), (1.3636363636363635, 2.4545454545454546), (2.0, 2.6666666666666665), (3.6, 3.2), (2.1, 2.7), (2.142857142857143, 2.7142857142857144), (2.25, 2.75), (0.7142857142857143, 0.8571428571428572), (-1.0, 6.0), (0.2, 2.4), (-2.0, 9.0), (-0.5, 4.5), (-0.2, 3.6), (2.0, -3.0), (1.25, -0.75), (1.4, -1.2000000000000002), (1.5, -1.5), (1.2, -0.6000000000000001), (-3.0, 12.0), (-4.0, 15.0), (3.0, -6.0), (1.25, 0.5), (1.4, 0.20000000000000018), (3.0, -3.0), (-1.0, 5.0), (-3.0, 9.0), (-0.3333333333333333, 3.6666666666666665), (1.6666666666666667, -0.3333333333333335), (1.75, -0.5), (1.8, -0.6000000000000001), (6.0, -9.0), (-2.0, 7.0), (1.6666666666666667, 1.3333333333333333), (2.3333333333333335, 0.6666666666666665), (2.5, 0.5), (2.5, 3.0), (7.0, 3.0), (5.0, 3.0), (0.5, 3.0), (3.5, 3.0), (1.6, 0.6000000000000001), (1.4285714285714286, 0.8571428571428572), (1.75, 0.375), (1.1428571428571428, 1.2857142857142858), (1.25, 1.125), (0.75, 1.875), (-0.5, 3.75), (6.0, -6.0), (8.0, -9.0), (-4.0, 9.0), (3.0, -1.5), (2.6666666666666665, 1.6666666666666667), (3.5, 1.25), (2.25, 1.875), (1.6, 2.2), (2.5, 1.75), (3.3333333333333335, 1.3333333333333333), (2.8, 1.6), (2.4, 1.4), (1.875, 1.75), (1.6363636363636365, 1.9090909090909092), (2.076923076923077, 1.6153846153846154), (9.0, -3.0), (2.142857142857143, 1.5714285714285714), (1.2857142857142858, 2.142857142857143), (2.625, 1.25), (2.4545454545454546, 1.3636363636363635), (1.0, 2.6666666666666665), (2.142857142857143, 2.2857142857142856), (1.8, 2.4), (4.2, 1.6), (2.4545454545454546, 2.1818181818181817), (1.7142857142857142, 2.428571428571429), (-9.0, 6.0), (0.6, 2.8), (1.125, 2.625), (3.75, 1.75), (2.7, 2.1), (2.5714285714285716, 2.142857142857143), (1.0, -1.0), (1.0, -2.0), (1.0, -3.0), (1.0, 4.0), (1.0, 6.0), (1.0, 5.0), (1.6666666666666665, 0.6666666666666666), (2.333333333333333, 1.3333333333333333), (5.0, 4.0), (1.75, 0.75), (2.5, 1.5), (2.2, 1.2), (1.4, 0.8), (2.333333333333333, 2.6666666666666665), (1.75, 1.5), (1.8571428571428572, 1.7142857142857142), (2.2, 2.4), (1.4, 1.2), (1.5714285714285714, 1.7142857142857142), (1.75, 2.25), (1.8571428571428572, 2.5714285714285716), (0.5, -1.5), (-1.0, -6.0), (0.33333333333333337, -0.3333333333333333), (2.0, 0.5), (1.8571428571428572, 0.42857142857142855), (2.2, 0.6), (4.0, 1.5), (2.6, 0.8), (2.7142857142857144, 0.8571428571428571), (3.6666666666666665, 1.3333333333333333), (2.0, 1.5), (1.5714285714285714, 0.8571428571428571), (1.8571428571428572, 1.2857142857142858), (2.2, 1.8), (2.428571428571429, 2.142857142857143), (2.6, 2.4), (1.25, 1.5), (1.4, 1.8), (1.6666666666666665, 2.333333333333333), (1.5714285714285714, 2.142857142857143), (5.0, 9.0), (1.75, 2.5), (2.333333333333333, 0.33333333333333337), (5.0, -1.0), (2.2, 0.4), (2.142857142857143, 0.4285714285714286), (3.6666666666666665, -0.33333333333333326), (7.0, -2.0), (1.5714285714285714, 1.2857142857142856), (2.333333333333333, 1.6666666666666665), (2.6, 1.8), (2.2, 1.6), (2.428571428571429, 1.7142857142857144), (0.33333333333333337, 3.333333333333333), (1.75, 0.5), (5.0, -6.0), (2.6, 1.2), (2.428571428571429, 1.2857142857142856), (2.2, 1.4), (1.4, 2.2), (2.0, 2.5), (7.0, 5.0), (3.6666666666666665, 3.333333333333333), (2.142857142857143, 2.571428571428571), (2.2, 2.6), (-1.0, 9.0), (0.5, 4.5), (2.6, 0.6000000000000001), (2.428571428571429, 0.8571428571428572), (3.6666666666666665, 1.6666666666666667), (2.7142857142857144, 2.142857142857143), (2.6, 2.2), (2.75, 0.75), (3.5, 1.5), (2.75, 1.5), (2.75, 2.25)]
ptmap = dict()
for i in range(len(pts)):
    ptmap[pts[i]] = i

v = [None for i in range(16)]
for y in range(3,-1,-1):
    p = map(int, raw_input().split())
    for x in range(4):
        v[p[x]-1] = (float(x), float(y))
        assert(v[p[x]-1] in ptmap)
        # v[p[x]-1] = ptmap[v[p[x]-1]]

def overlaps(a, b, z):
    ab = [b[0]-a[0], b[1]-a[1]]
    az = [z[0]-a[0], z[1]-a[1]]

    if abs(az[0]) + abs(az[1]) < 1e-9: return 0.0
    if abs(ab[0]) + abs(ab[1]) < 1e-9: return -1

    T = hypot(ab[0],ab[1]) / hypot(az[0],az[1])
    if T + 1e-9 < 1: return -1
    if hypot(az[0]*T-ab[0], az[1]*T-ab[1]) > 1e-9: return -1

    return 1.0 / T

dp = [dict() for i in range(16)]
dp[0][ptmap[v[0]]] = [0, 0.0, None]
def up(n, t, score):
    if t not in dp[n] or score < dp[n][t]:
        dp[n][t] = score

for i in range(16):
    if i > 0:
        k = dp[i].keys()
        best = min(map(lambda x: dp[i][x][0], k))
        for sp in k:
            if dp[i][sp][0] > best + 1:
                del dp[i][sp]

    for sp in dp[i].keys():
        for ep in range(len(pts)):
            j = i
            where = 0.0
            while j+1 < 16:
                T = overlaps(pts[sp], pts[ep], v[j+1])
                if T >= where:
                    where = T
                    j += 1
                else:
                    break
            if j <> i:
                up(j, ep, [dp[i][sp][0]+1, -hypot(pts[sp][0]-v[i][0], pts[sp][1]-v[i][1]), [i, sp]])

assert ptmap[v[-1]] in dp[-1]

res = []
i = [15, ptmap[v[-1]]]
while i is not None:
    res += [i[1]]
    i = dp[i[0]][i[1]][2]

print len(res) - 1
# for i in res[::-1]:
#     print '%.9f %.9f' % (pts[i][0],pts[i][1])
