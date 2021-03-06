import datetime
import inspect
import os
import sys
import unittest

import numpy

import cf

class FieldTest(unittest.TestCase):
    def setUp(self):
        self.filename2 = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      'test_file2.nc')
        self.filename4 = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      'test_file4.nc')

        self.chunk_sizes = (17, 50, 100, 300, 3000, 300000)[::-1]
        self.original_chunksize = cf.CHUNKSIZE()

        self.test_only = []
#        self.test_only = ['nought']
#        self.test_only = ['test_COLLAPSE_CLIMATOLOGICAL_TIME']
#        self.test_only = ['test_COLLAPSE']
#        self.test_only = ['test_COLLAPSE_GROUP_OPTIONS']

    def test_COLLAPSE_CLIMATOLOGICAL_TIME(self):
        if self.test_only and inspect.stack()[0][3] not in self.test_only:
            return

        verbose = False

        f = cf.read(self.filename4)[0]

        g = f.collapse('T: mean within years time: minimum over years', within_years=cf.seasons(), _debug=False)
        if verbose:
            print('\n',f)
            print(g)
            print(g.constructs)
        self.assertTrue(g.shape == (4, 4, 5))

        g = f.collapse('T: max within years time: minimum over years', within_years=cf.seasons())
        if verbose:
            print('\n',f)
            print(g)
            print(g.constructs)
        self.assertTrue(g.shape == (4, 4, 5))

        g = f.collapse('T: mean within years time: minimum over years', within_years=cf.M(), _debug=0)
        if verbose:
            print('\n',f)
            print(g)
            print(g.constructs)
        self.assertTrue(g.shape == (12, 4, 5))

        g = f.collapse('T: max within years time: minimum over years', within_years=cf.M())
        if verbose:
            print('\n',f)
            print(g)
            print(g.constructs)
        self.assertTrue(g.shape == (12, 4, 5))

        g = f[:12].collapse('T: mean within years time: minimum over years', within_years=cf.seasons())
        if verbose:
            print('\n',f[:12])
            print(g)
            print(g.constructs)
        self.assertTrue(g.shape == (4, 4, 5))

        g = f[:12].collapse('T: max within years time: minimum over years', within_years=cf.seasons())
        if verbose:
            print('\n',f[:12])
            print(g)
            print(g.constructs)
        self.assertTrue(g.shape == (4, 4, 5))

        g = f[:12].collapse('T: mean within years time: minimum over years', within_years=cf.M())
        if verbose:
            print('\n',f[:12])
            print(g)
            print(g.constructs)
        self.assertTrue(g.shape == (12, 4, 5))

        g = f[:12].collapse('T: max within years time: minimum over years', within_years=cf.M())
        if verbose:
            print('\n',f[:12])
            print(g)
            print(g.constructs)
        self.assertTrue(g.shape == (12, 4, 5))

        for key in f.cell_methods:
            f.del_construct(key)

        g = f.collapse('T: max within years time: minimum over years', within_years=cf.seasons())
        if verbose:
            print('\n',f)
            print(g)
            print(g.constructs)
        self.assertTrue(g.shape == (4, 4, 5))

        g = f.collapse('T: max within years time: min over years', within_years=cf.M())
        if verbose:
            print('\n',f)
            print(g)
            print(g.constructs)
        self.assertTrue(g.shape == (12, 4, 5))

        g = f[:12].collapse('T: max within years time: minimum over years', within_years=cf.seasons())
        if verbose:
            print('\n',f[:12])
            print(g)
            print(g.constructs)
        self.assertTrue(g.shape == (4, 4, 5))

        g = f[:12].collapse('T: max within years time: minimum over years', within_years=cf.M())
        if verbose:
            print('\n',f[:12])
            print(g)
            print(g.constructs)
        self.assertTrue(g.shape == (12, 4, 5))

        g = f.collapse('T: max within years time: minimum over years',
                       within_years=cf.seasons(), over_years=cf.Y(5))
        if verbose:
            print('\n',f)
            print(g)
            print(g.constructs)
        self.assertTrue(g.shape == (8, 4, 5))

        g = f[::-1, ...].collapse('T: max within years time: minimum over years',
                                  within_years=cf.seasons(), over_years=cf.Y(5))
        if verbose:
            print('\n',f)
            print(g)
            print(g.constructs)
        self.assertTrue(g.shape == (8, 4, 5))
    # --- End: def

    def test_COLLAPSE(self):
        if self.test_only and inspect.stack()[0][3] not in self.test_only:
            return

        verbose = False

        f = cf.read(self.filename2)[0]

        g = f.collapse('mean')
        if verbose:
            print('\n',f)
            print(g)
            print(g.constructs)
        self.assertTrue(g.shape == (1, 1, 1), g.shape)

        g = f.collapse('mean', axes=['T', 'X'])
        if verbose:
            print('\n',f)
            print(g)
            print(g.constructs)
        self.assertTrue(g.shape == (1, 4, 1))

        g = f.collapse('mean', axes=[0, 2])

        if verbose:
            print('\n',f)
            print(g)
            print(g.constructs)
        self.assertTrue(g.shape == (1, 4, 1))

        g = f.collapse('mean', axes=[0, 1])
        if verbose:
            print('\n',f)
            print(g)
            print(g.constructs)
        self.assertTrue(g.shape == (1, 1, 5))

        g = f.collapse('mean', axes='domainaxis1')
        if verbose:
            print('\n',f)
            print(g)
            print(g.constructs)
        self.assertTrue(g.shape == (1800, 1, 5))

        g = f.collapse('mean', axes=['domainaxis1'])
        if verbose:
            print('\n',f)
            print(g)
            print(g.constructs)
        self.assertTrue(g.shape == (1800, 1, 5))

        g = f.collapse('mean', axes=[1])
        if verbose:
            print('\n',f)
            print(g)
            print(g.constructs)
        self.assertTrue(g.shape == (1800, 1, 5))

        g = f.collapse('mean', axes=1)
        if verbose:
            print('\n',f)
            print(g)
            print(g.constructs)
        self.assertTrue(g.shape == (1800, 1, 5))

        g = f.collapse('T: mean')
        if verbose:
            print('\n',f)
            print(g)
            print(g.constructs)
        self.assertTrue(g.shape == (1, 4, 5))

        g = f.collapse('T: mean X: maximum')
        if verbose:
            print('\n',f)
            print(g)
            print(g.constructs)
        self.assertTrue(g.shape == (1, 4, 1))

        g = f.collapse('T: mean within years time: minimum over years',
                       within_years=cf.M(), _debug=0)
        if verbose:
            print('\n',f)
            print(g)
            print(g.constructs)
        self.assertTrue(g.shape == (12, 4, 5))

        for m in range(1, 13):
            a = numpy.empty((5, 4, 5))
            for i, year in enumerate(f.subspace(T=cf.month(m)).coord('T').year.unique()):
                q = cf.month(m) & cf.year(year)
                x = f.subspace(T=cf.month(m) & cf.year(year))
                x.data.mean(axes=0, inplace=True)
                a[i] = x.array

            a = a.min(axis=0)
            self.assertTrue(numpy.allclose(a, g.array[m % 12]))
        # --- End: for

        g = f.collapse('T: mean', group=360)

        for group in (cf.M(12),
                      cf.M(12, month=12),
                      cf.M(12, day=16),
                      cf.M(12, month=11, day=27)):
            g = f.collapse('T: mean', group=group)
            bound = g.coord('T').bounds.datetime_array[0, 1]
            self.assertTrue(bound.month == group.offset.month,
                            "{}!={}, group={}".format(bound.month, group.offset.month, group))
            self.assertTrue(bound.day   == group.offset.day,
                            "{}!={}, group={}".format(bound.day, group.offset.day, group))
        # --- End: for

#            for group in (cf.D(30),
#                          cf.D(30, month=12),
#                          cf.D(30, day=16),
#                          cf.D(30, month=11, day=27)):
#                g = f.collapse('T: mean', group=group)
#                bound = g.coord('T').bounds.datetime_array[0, 1]
#                self.assertTrue(bound.day == group.offset.day,
#                                "{}!={}, bound={}, group={}".format(bound.day, group.offset.day, bound, group))
    # --- End: def

    def test_COLLAPSE_weights(self):
        if self.test_only and inspect.stack()[0][3] not in self.test_only:
            return

        verbose = False

        f = cf.read(self.filename4)[0]
        if verbose:
            print(f)

        g = f.collapse('area: mean')
        g = f.collapse('area: mean', weights='area')
        if verbose:
            print(g)
    # --- End: def

    def test_COLLAPSE_groups(self):
        if self.test_only and inspect.stack()[0][3] not in self.test_only:
            return

        verbose = False

        f = cf.read(self.filename4)[0]

        g = f.collapse('T: mean', group=cf.M(12), group_span=cf.Y(), _debug=0)
        if verbose:
            print(f)
            print(g)
            print(g.constructs)
        self.assertTrue(g.shape == (9, 4, 5))

        g = f.collapse('T: mean', group=cf.M(12, month=12)        , group_span=cf.Y())
        if verbose:
            print(f)
            print(g)
            print(g.constructs)
        self.assertTrue(g.shape == (10, 4, 5))

        g = f.collapse('T: mean', group=cf.M(12, day=16)          , group_span=cf.Y())
        if verbose:
            print(f)
            print(g)
            print(g.constructs)
        self.assertTrue(g.shape == (9, 4, 5))

        g = f.collapse('T: mean', group=cf.M(12, month=11, day=27), group_span=cf.Y())
        if verbose:
            print(f)
            print(g)
            print(g.constructs)
        self.assertTrue(g.shape == (10, 4, 5))

        g = f.collapse('T: mean', group=cf.M(12, month=6, day=27), group_span=cf.Y(), _debug=0)
        if verbose:
            print(f)
            print(g)
            print(g.dimension_coordinates('T').value().bounds.data.datetime_array)
            print(g.constructs)
        self.assertTrue(g.shape == (9, 4, 5))

        g = f.collapse('T: mean', group=cf.M(5, month=12), group_span=cf.M(5), group_contiguous=1)
        if verbose:
            print(f)
            print(g)
            print(g.dimension_coordinates('T').value().bounds.data.datetime_array)
            print(g.constructs)
        self.assertTrue(g.shape == (24, 4, 5))

        g = f.collapse('T: mean', group=cf.M(5, month= 3), group_span=cf.M(5), group_contiguous=1)
        if verbose:
            print(f)
            print(g)
            print(g.dimension_coordinates('T').value().bounds.data.datetime_array)
            print(g.constructs)
        self.assertTrue(g.shape == (24, 4, 5))

        g = f.collapse('T: mean', group=cf.M(5, month=2), group_span=cf.M(5), group_contiguous=1)
        if verbose:
            print(f)
            print(g)
            print(g.dimension_coordinates('T').value().bounds.data.datetime_array)
            print(g.constructs)
        self.assertTrue(g.shape == (24, 4, 5))

        g = f.collapse('T: mean', group=cf.M(5, month=12), group_span=cf.M(5), group_contiguous=2)
        if verbose:
            print(f)
            print(g)
            print(g.dimension_coordinates('T').value().bounds.data.datetime_array)
            print(g.constructs)
        self.assertTrue(g.shape == (24, 4, 5))

        g = f.collapse('T: mean', group=cf.M(5, month=3), _debug=0)
        if verbose:
            print(f)
            print(g)
            print(g.dimension_coordinates('T').value().bounds.data.datetime_array)
            print(g.constructs)
        self.assertTrue(g.shape == (24, 4, 5)) # TODO - look into month offset when M< 12

        g = f.collapse('T: mean', group=cf.M(5, month=3), group_span=cf.M(5), group_contiguous=2)
        if verbose:
            print(f)
            print(g)
            print(g.dimension_coordinates('T').value().bounds.data.datetime_array)
            print(g.constructs)
        self.assertTrue(g.shape == (24, 4, 5))

        g = f.collapse('T: mean', group=cf.M(5, month=12), group_contiguous=1)
        if verbose:
            print(f)
            print(g)
            print(g.dimension_coordinates('T').value().bounds.data.datetime_array)
            print(g.constructs)
        self.assertTrue(g.shape == (24, 4, 5))

        g = f.collapse('T: mean', group=cf.M(5, month= 3), group_contiguous=1)
        if verbose:
            print(f)
            print(g)
            print(g.dimension_coordinates('T').value().bounds.data.datetime_array)
            print(g.constructs)
        self.assertTrue(g.shape == (24, 4, 5))

        g = f.collapse('T: mean', group=cf.M(5, month=12), group_contiguous=2)
        if verbose:
            print(f)
            print(g)
            print(g.dimension_coordinates('T').value().bounds.data.datetime_array)
            print(g.constructs)
        self.assertTrue(g.shape == (24, 4, 5))

        g = f.collapse('T: mean', group=cf.M(5, month= 3), group_contiguous=2)
        if verbose:
            print(f)
            print(g)
            print(g.dimension_coordinates('T').value().bounds.data.datetime_array)
            print(g.constructs)
        self.assertTrue(g.shape == (24, 4, 5))

        g = f.collapse('T: mean within years time: minimum over years', within_years=cf.M(3), group_span=True)
        if verbose:
            print(f)
            print(g)
            print(g.dimension_coordinates('T').value().bounds.data.datetime_array)
            print(g.constructs)
        self.assertTrue(g.shape == (4, 4, 5))

        g = f.collapse('T: mean within years time: minimum over years', within_years=cf.seasons(), group_span=cf.M(3))
        if verbose:
            print(f)
            print(g)
            print(g.dimension_coordinates('T').value().bounds.data.datetime_array)
            print(g.constructs)
        self.assertTrue(g.shape == (4, 4, 5))

#            g = f[::2].collapse('T: mean', group=cf.M(5, month=12),
#                                group_span=cf.M(5),group_contiguous=1)
#            print (g)
#            g = f.collapse('T: mean', group=cf.M(5, month= 3),
#                           group_contiguous=1)
#            g = f.collapse('T: mean', group=cf.M(5, month=12),
#                           group_contiguous=2)
#            g = f.collapse('T: mean', group=cf.M(5, month= 3),
#                           group_contiguous=2)
    # --- End: def

# --- End: class

if __name__ == '__main__':
    print('Run date:', datetime.datetime.now())
    cf.environment()
    print()
    unittest.main(verbosity=2)
