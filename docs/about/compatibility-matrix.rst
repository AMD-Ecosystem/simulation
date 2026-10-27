.. meta::
    :description: AMD Simulation compatibility matrix
    :keywords: ROCm, simulation, compatibility, AMD, Instinct, GPU, physics, numerical, solvers, Quadrants, Genesis, Warp, MJWarp, MuJoCo, Taichi, GSplat, Gaussian, Splatting, PyTorch, HIP, multi, scaling, high, performance, computing, HPC, real-time, rendering, volumetric, fluid, dynamics, rigid, body, particle, sparse, voxel, grids, differentiable, 3D, vision, computer, graphics, robotics, scientific, toolkit, accelerated

.. _simulation-compat-matrix:

**************************************************************************************
AMD Simulation compatibility matrix
**************************************************************************************

Use the following matrix to view the AMD Simulation compatibility and system requirements across releases:

.. role:: version-start

.. |quadrants-1-3-3-26-10-src| raw:: html

   <a href="https://github.com/AMD-Ecosystem/quadrants/blob/rocm10.1.0_r26.10/Dockerfile" aria-label="Dockerfile"><i class="fab fa-github"></i></a>

.. |genesis-1-4-3-26-10-src| raw:: html

   <a href="https://github.com/AMD-Ecosystem/Genesis/blob/rocm10.1.0_r26.10/Dockerfile" aria-label="Dockerfile"><i class="fab fa-github"></i></a>

.. |warp-1-13-0-26-10-src| raw:: html

   <a href="https://github.com/AMD-Ecosystem/warp/blob/release/v1.13.0/docker/rocm_ci/Dockerfile.rocm_ci" aria-label="Dockerfile"><i class="fab fa-github"></i></a>

.. |mjwarp-3-8-1-26-10-src| raw:: html

   <a href="https://github.com/AMD-Ecosystem/mujoco_warp/blob/release/v3.8.1/docker/rocm/Dockerfile" aria-label="Dockerfile"><i class="fab fa-github"></i></a>

.. |taichi-lang-1-8-0b2-25-11-src| raw:: html

   <a href="https://hub.docker.com/r/rocm/taichi/tags" aria-label="rocm/taichi"><i class="fab fa-docker"></i></a>

.. |gsplat-1-5-3b2-25-11-src| raw:: html

   <a href="https://github.com/AMD-Ecosystem/gsplat/blob/release/1.5.3b2/docs/install/gsplat-install.rst" aria-label="release/1.5.3b2"><i class="fab fa-github"></i></a>

.. |taichi-lang-1-8-0b1-25-10-src| raw:: html

   <a href="https://hub.docker.com/r/rocm/taichi/tags" aria-label="rocm/taichi"><i class="fab fa-docker"></i></a>

.. |gsplat-1-5-3b1-25-10-src| raw:: html

   <a href="https://github.com/AMD-Ecosystem/gsplat/blob/release/1.5.3b1/docs/install/gsplat-install.rst" aria-label="release/1.5.3b1"><i class="fab fa-github"></i></a>

.. table::
   :widths: 10 22 14 12 8 16 8 10
   :align: left
   :class: compat-matrix format-big-table

   +------------------------+-----------------------------------------------------+---------------------------------------+-----------------------------------------+--------------+-----------------------------------------+------------+---------------------------------+
   | AMD Simulation version | Component                                           | AMD Instinct GPU                      | ROCm version                            | Ubuntu       | PyTorch                                 | Python     | Source                          |
   +========================+=====================================================+=======================================+=========================================+==============+=========================================+============+=================================+
   | :version-start:`26.10` | `Quadrants 1.3.3 <quadrants-1-3-3-26-10_>`_         | MI300X, MI350X, MI355X                | 10.1.0                                  | 24.04        | 2.13.0                                  | 3.12       | |quadrants-1-3-3-26-10-src|     |
   +                        +-----------------------------------------------------+---------------------------------------+-----------------------------------------+--------------+-----------------------------------------+------------+---------------------------------+
   |                        | `Genesis 1.4.3 <genesis-1-4-3-26-10_>`_             | MI300X, MI350X, MI355X                | 10.1.0                                  | 24.04        | 2.13.0                                  | 3.12       | |genesis-1-4-3-26-10-src|       |
   +                        +-----------------------------------------------------+---------------------------------------+-----------------------------------------+--------------+-----------------------------------------+------------+---------------------------------+
   |                        | `Warp 1.13.0 <warp-1-13-0-26-10_>`_                 | MI325X, MI350X, MI355X                | 7.2.0 (MI325X), 10.1.0 (MI350X, MI355X) | 24.04        | 2.9.1 (MI325X), 2.14.0 (MI350X, MI355X) | 3.12       | |warp-1-13-0-26-10-src|         |
   +                        +-----------------------------------------------------+---------------------------------------+-----------------------------------------+--------------+-----------------------------------------+------------+---------------------------------+
   |                        | `MJWarp 3.8.1 <mjwarp-3-8-1-26-10_>`_               | MI325X, MI350X, MI355X                | 7.2.0 (MI325X), 10.1.0 (MI350X, MI355X) | 24.04        | 2.9.1 (MI325X), 2.14.0 (MI350X, MI355X) | 3.12       | |mjwarp-3-8-1-26-10-src|        |
   +------------------------+-----------------------------------------------------+---------------------------------------+-----------------------------------------+--------------+-----------------------------------------+------------+---------------------------------+
   | :version-start:`25.11` | `Taichi Lang 1.8.0b2 <taichi-lang-1-8-0b2-25-11_>`_ | MI355X, MI325X, MI300X, MI250X, MI210 | 7.0.0                                   | 24.04        | N/A                                     | 3.12       | |taichi-lang-1-8-0b2-25-11-src| |
   +                        +-----------------------------------------------------+---------------------------------------+-----------------------------------------+--------------+-----------------------------------------+------------+---------------------------------+
   |                        | `GSplat 1.5.3b2 <gsplat-1-5-3b2-25-11_>`_           | MI325X, MI300X                        | 7.0.0, 6.4.3                            | 24.04, 22.04 | 2.8.0, 2.6.0                            | 3.12, 3.10 | |gsplat-1-5-3b2-25-11-src|      |
   +------------------------+-----------------------------------------------------+---------------------------------------+-----------------------------------------+--------------+-----------------------------------------+------------+---------------------------------+
   | :version-start:`25.10` | `Taichi Lang 1.8.0b1 <taichi-lang-1-8-0b1-25-10_>`_ | MI250X, MI210                         | 6.3.2                                   | 22.04        | N/A                                     | 3.10       | |taichi-lang-1-8-0b1-25-10-src| |
   +                        +-----------------------------------------------------+---------------------------------------+-----------------------------------------+--------------+-----------------------------------------+------------+---------------------------------+
   |                        | `GSplat 1.5.3b1 <gsplat-1-5-3b1-25-10_>`_           | MI300X                                | 6.4.3                                   | 24.04        | 2.6.0                                   | 3.12       | |gsplat-1-5-3b1-25-10-src|      |
   +------------------------+-----------------------------------------------------+---------------------------------------+-----------------------------------------+--------------+-----------------------------------------+------------+---------------------------------+

.. _quadrants-1-3-3-26-10: https://rocm.docs.amd.com/projects/quadrants/en/docs-26.10/install/quadrants-install.html
.. _genesis-1-4-3-26-10: https://rocm.docs.amd.com/projects/genesis/en/docs-26.10/install/genesis-install.html
.. _warp-1-13-0-26-10: https://rocm.docs.amd.com/projects/warp/en/docs-26.10/install/warp-install.html
.. _mjwarp-3-8-1-26-10: https://rocm.docs.amd.com/projects/mujoco-warp/en/docs-26.10/install/mujoco-warp-install.html
.. _taichi-lang-1-8-0b2-25-11: https://rocm.docs.amd.com/projects/taichi/en/docs-25.11/install/taichi-install.html
.. _gsplat-1-5-3b2-25-11: https://rocm.docs.amd.com/projects/gsplat/en/docs-25.11/install/gsplat-install.html
.. _taichi-lang-1-8-0b1-25-10: https://rocm.docs.amd.com/projects/taichi/en/docs-25.10/install/taichi-install.html
.. _gsplat-1-5-3b1-25-10: https://rocm.docs.amd.com/projects/gsplat/en/docs-25.10/install/gsplat-install.html
