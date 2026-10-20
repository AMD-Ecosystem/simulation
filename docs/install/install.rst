.. meta::
    :description: AMD Simulation installation
    :keywords: ROCm, simulation, AMD, Instinct, GPU, physics, numerical, solvers, Quadrants, Genesis, Warp, MJWarp, MuJoCo, Taichi, GSplat, Gaussian, Splatting, PyTorch, HIP, multi, scaling, high, performance, computing, HPC, real-time, rendering, volumetric, fluid, dynamics, rigid, body, particle, sparse, voxel, grids, differentiable, 3D, vision, computer, graphics, robotics, scientific, toolkit, accelerated

.. _linux-install:

**************************************************************************************
Install AMD Simulation
**************************************************************************************

This topic provides brief guidance and recommendations on setting up a ROCm-enabled
environment for simulation workloads. This includes verifying prerequisites before
installing AMD Simulation components.

System requirements
======================================================================================

AMD Simulation components support a range of AMD Instinct GPUs and ROCm versions.
Individual components also support additional software configurations.

Before installing any AMD Simulation component, verify that your system meets the
hardware and software prerequisites for that component, as outlined in the
:ref:`simulation-compat-matrix` page.

Install AMD Simulation
======================================================================================

Each component has distinct prerequisite and environment requirements. To avoid
dependency conflicts and configuration errors, components must be installed
individually rather than through a unified installation process.

The installation instructions for each component can be found as follows:

* `Quadrants on ROCm <https://rocm.docs.amd.com/projects/quadrants/en/docs-26.10/install/quadrants-install.html>`__
* `Genesis on ROCm <https://rocm.docs.amd.com/projects/genesis/en/docs-26.10/install/genesis-install.html>`__
* `Warp on ROCm <https://rocm.docs.amd.com/projects/warp/en/docs-26.10/install/warp-install.html>`__
* `MJWarp on ROCm <https://rocm.docs.amd.com/projects/mujoco-warp/en/docs-26.10/install/mujoco-warp-install.html>`__
