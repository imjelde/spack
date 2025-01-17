# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHardhat(RPackage):
    """Construct Modeling Packages.

    Building modeling packages is hard. A large amount of effort generally goes
    into providing an implementation for a new method that is efficient, fast,
    and correct, but often less emphasis is put on the user interface. A good
    interface requires specialized knowledge about S3 methods and formulas,
    which the average package developer might not have. The goal of 'hardhat'
    is to reduce the burden around building new modeling packages by providing
    functionality for preprocessing, predicting, and validating input."""

    cran = "hardhat"

    version('1.0.0', sha256='2740dc243a440e7d32370a78f9258255faea6d900075901cf6009c651769e7bd')
    version('0.2.0', sha256='9497ca0fe6206c54d1da79f248d44c5faffc7d375b630091ef45dfca46c29628')

    depends_on('r@2.10:', type=('build', 'run'))
    depends_on('r@3.4.0:', type=('build', 'run'), when='@1.0.0:')
    depends_on('r-glue', type=('build', 'run'))
    depends_on('r-glue@1.6.2:', type=('build', 'run'), when='@1.0.0:')
    depends_on('r-rlang@0.4.2:', type=('build', 'run'))
    depends_on('r-rlang@1.0.2:', type=('build', 'run'), when='@1.0.0:')
    depends_on('r-tibble', type=('build', 'run'))
    depends_on('r-tibble@3.1.7:', type=('build', 'run'), when='@1.0.0:')
    depends_on('r-vctrs@0.3.0:', type=('build', 'run'))
    depends_on('r-vctrs@0.4.1:', type=('build', 'run'), when='@1.0.0:')
