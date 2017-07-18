"""
Run these unit test at commandline.
$   cd u25656@PC /e/Githubz/mtpy2 (develop)
$   nosetests tests/imaging/
"""
import os.path
from unittest import TestCase

# matplotlib.use('Qt4Agg')  # comment out this line if you want to see the plots 1-by-1 on screen.
import matplotlib.pyplot as plt

plt.ion()
# plt.ioff()

from mtpy.imaging.penetration import ZComponentError
from mtpy.imaging.penetration_depth1d import plot_edi_dir
from mtpy.imaging.penetration_depth1d import plot_edi_file


class TestPenetration_depth1d(TestCase):
    @classmethod
    def setUpClass(cls):
        cls._temp_dir = "tests/temp"
        if not os.path.isdir(cls._temp_dir):
            os.mkdir(cls._temp_dir)

    @classmethod
    def tearDownClass(cls):
        plt.close('all')

    # def setUp(self):
    #     plt.clf()

    def tearDown(self):
        plt.pause(1)

    def test_plot_edi_dir(self):
        """
        testing plotting all edi files in a given dir
        :return:
        """
        # all plots
        plot_edi_dir("tests/data/edifiles")
        # plt.close()

    def test_plot_edi_file(self):
        """
        testing plotting a single edi file
        :return:
        """
        plot_edi_file("tests/data/edifiles/15125A.edi")

    def test_plot_edi_file_zxy(self):
        """
        testing ploting zxy of a single edi file
        :return:
        """
        plot_edi_file("tests/data/edifiles/15125A.edi", ['zxy'])

    def test_plot_edi_file_zyx(self):
        """
        testing plotting zyx of a single edi file
        :return:
        """
        plot_edi_file("tests/data/edifiles/15125A.edi", ['zyx'])

    def test_plot_edi_file_det(self):
        """
        testing plotting det of a single edi file
        :return:
        """
        plot_edi_file("tests/data/edifiles/15125A.edi", ['det'])

    def test_plot_edi_file_zxy_zyx(self):
        """
        testing plotting zxy & zyx of a single edi file
        :return:
        """
        plot_edi_file("tests/data/edifiles/15125A.edi", ['zxy', 'zyx'])

    def test_plot_edi_file_zxy_det(self):
        """
        testing plotting zxy & det of a single edi file
        :return:
        """
        plot_edi_file("tests/data/edifiles/15125A.edi", ['zxy', 'det'])

    def test_plot_edi_file_zyx_det(self):
        """
        testing plotting zyx & det of a single edi file
        :return:
        """
        plot_edi_file("tests/data/edifiles/15125A.edi", ['zyx', 'det'])

    def test_plot_edi_file_unknown_type(self):
        """
        testing plotting zyx and an unknown of a single edi file
        :return:
        """
        plot_edi_file("tests/data/edifiles/15125A.edi", ['zyx', 'dat'])

    def test_plot_edi_file_empty_rholist(self):
        """
        testing plotting an empty rholist of a single edi file
        :return:
        """
        try:
            plot_edi_file("tests/data/edifiles/15125A.edi", [])
        except ZComponentError:
            pass

    def test_plot_edi_file_save_inage(self):
        """
        testing saving plot of a single edi file
        :return:
        """
        fname = os.path.join(self._temp_dir,"TestPenetration_depth1d.jpg")
        if os.path.isfile(fname):
            os.remove(fname)    # remove test file if already exist
        plot_edi_file("tests/data/edifiles/15125A.edi", savefile=fname)
        assert (os.path.isfile(fname))
        pass
