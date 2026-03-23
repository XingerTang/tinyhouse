from .. import InputOutput
from .. import Pedigree
import yappi


def test_iothreads():
    """
    Test the multi-threads input output functionality
    """
    ped = Pedigree.Pedigree()

    class args:
        pedigree = ["tests/test_iothreads/ped_file.txt"]
        genotypes = ["tests/test_iothreads/geno_file.txt"]
        main_metafounder = "MF_1"
        iothreads = 5

    yappi.start()
    InputOutput.args = args
    InputOutput.readInPedigreeFromInputs(ped, args)
    yappi.stop()

    # it may not need up to 5 threads
    assert len(yappi.get_thread_stats()) > 1
