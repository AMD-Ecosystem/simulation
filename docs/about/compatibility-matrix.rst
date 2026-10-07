.. meta::
    :description: AMD Simulation compatibility matrix
    :keywords: ROCm, simulation, compatibility, AMD, Instinct, GPU, physics, numerical, solvers, Taichi, GSplat, Gaussian, Splatting, PyTorch, HIP, multi, scaling, high, performance, computing, HPC, real-time, rendering, volumetric, fluid, dynamics, rigid, body, particle, sparse, voxel, grids, differentiable, 3D, vision, computer, graphics, robotics, scientific, toolkit, accelerated

.. _simulation-compat-matrix:

**************************************************************************************
AMD Simulation compatibility matrix
**************************************************************************************

Use this matrix to view the AMD Simulation compatibility and system requirements across releases:

+---------------------------+---------------------------+-------------------------+-------------------------+-----------------------------------------------+----------------------------------------------+
| AMD Simulation version    | Ubuntu                    | ROCm version            | Python version          | AMD Instinct GPU                              | Component                                    |
+===========================+===========================+=========================+=========================+===============================================+==============================================+
| 25.11                     | 24.04                     | 7.0.0                   | 3.12.3                  | MI355X,                                       | `Taichi Lang v1.8.0b2                        |
|                           |                           |                         |                         | MI325X,                                       | <https://rocm.docs.amd.com/projects/         |
|                           |                           |                         |                         | MI300X,                                       | taichi/en/docs-25.11/install/                |
|                           |                           |                         |                         | MI250X,                                       | taichi-install.html>`__                      |
|                           |                           |                         |                         | MI210                                         |                                              |
+                           +---------------------------+-------------------------+-------------------------+-----------------------------------------------+----------------------------------------------+
|                           | 24.04,                    | 7.0.0,                  | 3.12                    | MI325X,                                       | `GSplat v1.5.3b2                             |
|                           | 22.04                     | 6.4.3                   | 3.10                    | MI300X                                        | <https://rocm.docs.amd.com/projects/         |
|                           |                           |                         |                         |                                               | gsplat/en/docs-25.11/install/                |
|                           |                           |                         |                         |                                               | gsplat-install.html>`__                      |
+---------------------------+---------------------------+-------------------------+-------------------------+-----------------------------------------------+----------------------------------------------+
| 25.10                     | 22.04                     | 6.3.2                   | 3.10.12                 | MI250X,                                       | `Taichi Lang v1.8.0b1                        |
|                           |                           |                         |                         | MI210                                         | <https://rocm.docs.amd.com/projects/         |
|                           |                           |                         |                         |                                               | taichi/en/docs-25.10/install/                |
|                           |                           |                         |                         |                                               | taichi-install.html>`__                      |
+                           +---------------------------+-------------------------+-------------------------+-----------------------------------------------+----------------------------------------------+
|                           | 24.04                     | 6.4.3                   | 3.12                    | MI300X                                        | `GSplat v1.5.3b1                             |
|                           |                           |                         |                         |                                               | <https://rocm.docs.amd.com/projects/         |
|                           |                           |                         |                         |                                               | gsplat/en/docs-25.10/install/                |
|                           |                           |                         |                         |                                               | gsplat-install.html>`__                      |
+---------------------------+---------------------------+-------------------------+-------------------------+-----------------------------------------------+----------------------------------------------+