Contribution and Development Guide
==================================

Welcome to the tinyhouse contribution and development guide.

tinyhouse is a collection of Python modules for processing genotypes and pedigrees.  
It is used as a submodule in AlphaSuite programs such as AlphaPeel, AlphaImpute2, and others.

This guide is intended for developers who want to contribute to tinyhouse.  
It covers best practices for working with submodules and how to run tests.

1. Make your changes in your fork of tinyhouse, or in the relevant branch of
   AlphaSuite programs if the changes are specific to those programs.

2. Push the changes to your fork of tinyhouse.

3. Test the changes by running the tests in AlphaSuite programs with the
   updated tinyhouse submodule reference. For example:

   .. code-block:: bash

      cd AlphaPeel # navigate to the AlphaPeel directory
      cd src/tinypeel/tinyhouse
      git remote add fork https://github.com/yourusername/tinyhouse.git
      git fetch fork
      git checkout fork/your-branch
      cd ../../../
      pytest

4. If all tests pass, create a pull request.  
   If not, fix the issues and repeat steps 1–3 until all tests pass.

5. In the pull request, include:

   - The commits of AlphaPeel and AlphaImpute2 used for testing.

   - Any other relevant information about the changes.



