from .. import InputOutput
from .. import Pedigree
import pytest


@pytest.mark.benchmark(warmup=True)
def test_iothreads(benchmark):
    """
    Test the multi-threads input output functionality
    """
    ped = Pedigree.Pedigree()

    class args:
        pedigree = ["tests/test_iothreads/ped_file.txt"]
        genotypes = ["tests/test_iothreads/geno_file.txt"]
        main_metafounder = "MF_1"
        startsnp = 100
        stopsnp = 500
        iothreads = 5

    InputOutput.args = args
    benchmark(InputOutput.readInPedigreeFromInputs, ped, args)
