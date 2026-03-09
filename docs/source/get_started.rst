===============
Getting Started
===============

An example
----------

You can call the ``tinyhouse`` function by the following: 

.. code-block:: python

    # require the installation of AlphaPeel
    import tinypeel.tinyhouse.Pedigree as Pedigree
    import tinypeel.tinyhouse.InputOutput as InputOutput

    pedigree = Pedigree.Pedigree()

    class args:
        pedigree = ["example/simple_example/simple_pedigree.txt"]
        genotypes = ["example/simple_example/simple_genotype.txt"]
        main_metafounder = "MF_1"

    InputOutput.readInPedigreeFromInputs(pedigree, args)

    print(f"Individual {pedigree.individuals['C'].idx} has parents {pedigree.individuals['C'].sire.idx} and {pedigree.individuals['C'].dam.idx}.")