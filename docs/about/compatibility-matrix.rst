.. meta::
    :description: AMD Simulation compatibility matrix
    :keywords: ROCm, simulation, compatibility, AMD, Instinct, GPU, physics, numerical, solvers, Quadrants, Genesis, Warp, MJWarp, MuJoCo, Taichi, GSplat, Gaussian, Splatting, PyTorch, HIP, multi, scaling, high, performance, computing, HPC, real-time, rendering, volumetric, fluid, dynamics, rigid, body, particle, sparse, voxel, grids, differentiable, 3D, vision, computer, graphics, robotics, scientific, toolkit, accelerated

.. _simulation-compat-matrix:

**************************************************************************************
AMD Simulation compatibility matrix
**************************************************************************************

.. |github-icon| raw:: html

   <i class="fab fa-github"></i>

.. |docker-icon| raw:: html

   <i class="fab fa-docker"></i>

Use the following matrix to view the AMD Simulation compatibility and system requirements across releases:

.. role:: version-start

.. table::
   :width: 65%
   :widths: 20 10 16 12 6 8 6 10
   :align: left
   :class: compat-matrix format-big-table

   +------------------------------+----------------------------------------------------+------------------+--------------+--------+----------------------+----------------+--------------------------------------------+
   |    AMD Simulation version    |                     Component                      | AMD Instinct GPU | ROCm version | Ubuntu |       PyTorch        |     Python     |                   Source                   |
   +==============================+====================================================+==================+==============+========+======================+================+============================================+
   | :version-start:`26.10`       | `Quadrants 1.3.3                                   | MI300X,          | 10.1.0       | 24.04  | 2.13.0               | 3.12           | |github-icon| `Dockerfile                  |
   |                              | <https://rocm.docs.amd.com/projects/               | MI325X,          |              |        |                      |                | <https://github.com/AMD-Ecosystem/         |
   |                              | quadrants/en/docs-26.10/install/                   | MI350X,          |              |        |                      |                | quadrants/blob/rocm10.1.0_r26.10/          |
   |                              | quadrants-install.html>`__                         | MI355X           |              |        |                      |                | Dockerfile>`__                             |
   +                              +----------------------------------------------------+------------------+--------------+--------+----------------------+----------------+--------------------------------------------+
   |                              | `Genesis 1.4.3                                     | MI300X,          | 10.1.0       | 24.04  | 2.13                 | 3.12           | |github-icon| `Dockerfile                  |
   |                              | <https://rocm.docs.amd.com/projects/               | MI325X,          |              |        |                      |                | <https://github.com/AMD-Ecosystem/         |
   |                              | genesis/en/docs-26.10/install/                     | MI355X           |              |        |                      |                | Genesis/blob/rocm10.1.0_r26.10/            |
   |                              | genesis-install.html>`__                           |                  |              |        |                      |                | Dockerfile>`__                             |
   +                              +----------------------------------------------------+------------------+--------------+--------+----------------------+----------------+--------------------------------------------+
   |                              | `Warp 1.13.0                                       | MI325X,          | 7.2.0        | 24.04  | 2.9.1 (MI325X),      | 3.12           | |github-icon| `Dockerfile                  |
   |                              | <https://rocm.docs.amd.com/projects/               | MI350X,          | (MI325X),    |        | 2.14.0 (MI350X,      |                | <https://github.com/AMD-Ecosystem/         |
   |                              | warp/en/docs-26.10/install/                        | MI355X           | 10.1.0       |        | MI355X)              |                | warp/blob/v1.13.0/docker/rocm_ci/          |
   |                              | warp-install.html>`__                              |                  | (MI350X,     |        |                      |                | Dockerfile.rocm_ci>`__                     |
   |                              |                                                    |                  | MI355X)      |        |                      |                |                                            |
   +------------------------------+----------------------------------------------------+------------------+--------------+--------+----------------------+----------------+--------------------------------------------+
   | :version-start:`25.11`       | `Taichi Lang 1.8.0b2                               | MI355X,          | 7.0.0        | 24.04  | N/A                  | 3.12.3         | |docker-icon| `rocm/taichi                 |
   |                              | <https://rocm.docs.amd.com/projects/               | MI325X,          |              |        |                      |                | <https://hub.docker.com/r/rocm/            |
   |                              | taichi/en/docs-25.11/install/                      | MI300X,          |              |        |                      |                | taichi/tags>`__                            |
   |                              | taichi-install.html>`__                            | MI250X,          |              |        |                      |                |                                            |
   |                              |                                                    | MI210            |              |        |                      |                |                                            |
   +                              +----------------------------------------------------+------------------+--------------+--------+----------------------+----------------+--------------------------------------------+
   |                              | `GSplat 1.5.3b2                                    | MI325X,          | 7.0.0,       | 24.04, | 2.8,                 | 3.12,          | |github-icon| `release/1.5.3b2             |
   |                              | <https://rocm.docs.amd.com/projects/               | MI300X           | 6.4.3        | 22.04  | 2.6                  | 3.10           | <https://github.com/AMD-Ecosystem/         |
   |                              | gsplat/en/docs-25.11/install/                      |                  |              |        |                      |                | gsplat/blob/release/1.5.3b2/docs/          |
   |                              | gsplat-install.html>`__                            |                  |              |        |                      |                | install/gsplat-install.rst>`__             |
   +------------------------------+----------------------------------------------------+------------------+--------------+--------+----------------------+----------------+--------------------------------------------+
   | :version-start:`25.10`       | `Taichi Lang 1.8.0b1                               | MI250X,          | 6.3.2        | 22.04  | N/A                  | 3.10.12        | |docker-icon| `rocm/taichi                 |
   |                              | <https://rocm.docs.amd.com/projects/               | MI210            |              |        |                      |                | <https://hub.docker.com/r/rocm/            |
   |                              | taichi/en/docs-25.10/install/                      |                  |              |        |                      |                | taichi/tags>`__                            |
   |                              | taichi-install.html>`__                            |                  |              |        |                      |                |                                            |
   +                              +----------------------------------------------------+------------------+--------------+--------+----------------------+----------------+--------------------------------------------+
   |                              | `GSplat 1.5.3b1                                    | MI300X           | 6.4.3        | 24.04  | 2.6                  | 3.12           | |github-icon| `release/1.5.3b1             |
   |                              | <https://rocm.docs.amd.com/projects/               |                  |              |        |                      |                | <https://github.com/AMD-Ecosystem/         |
   |                              | gsplat/en/docs-25.10/install/                      |                  |              |        |                      |                | gsplat/blob/release/1.5.3b1/docs/          |
   |                              | gsplat-install.html>`__                            |                  |              |        |                      |                | install/gsplat-install.rst>`__             |
   +------------------------------+----------------------------------------------------+------------------+--------------+--------+----------------------+----------------+--------------------------------------------+
