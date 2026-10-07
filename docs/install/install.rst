.. meta::
    :description: AMD Simulation installation
    :keywords: ROCm, simulation, AMD, Instinct, GPU, physics, numerical, solvers, Taichi, GSplat, Gaussian, Splatting, PyTorch, HIP, multi, scaling, high, performance, computing, HPC, real-time, rendering, volumetric, fluid, dynamics, rigid, body, particle, sparse, voxel, grids, differentiable, 3D, vision, computer, graphics, robotics, scientific, toolkit, accelerated

.. _linux-install:

**************************************************************************************
Install AMD Simulation
**************************************************************************************

This topic provides brief guidance and recommendations on setting up a ROCm-enabled 
environment for simulation components.

.. note::

   For the 25.10 release, the AMD Simulation components must be installed separately
   and have unique hardware requirements. Ensure you have the system requirements 
   listed below to proceed.

System requirements
======================================================================================

To use Taichi Lang, you need the following prerequisites:

- **ROCm version:** `6.3.2 <https://repo.radeon.com/rocm/apt/6.3.2/>`__  (recommended)
- **Operating system:** Ubuntu 22.04
- **GPU platform:** AMD Instinct™ MI250X, MI210
- **Python:** `3.10.12 <https://www.python.org/downloads/release/python-31012/>`__

To use GSplat (Gaussian splatting), you need the following prerequisites:

- **ROCm version:** `6.4.3 <https://repo.radeon.com/rocm/apt/6.4.3/>`__ (recommended)
- **Operating system:** Ubuntu 24.04
- **GPU platform:** AMD Instinct™ MI300X
- **PyTorch:** `2.6 <https://github.com/ROCm/pytorch/tree/v2.6.0>`__ (ROCm-enabled)
- **Python:** `3.12.0 <https://www.python.org/downloads/release/python-3120/>`__


Install AMD Simulation components
======================================================================================

Each AMD Simulation 25.10 component must be separately installed as needed. The installation
instructions for each component can be found as follows: 

* Taichi Lang on ROCm - `Installation instructions <https://rocm.docs.amd.com/projects/taichi/en/docs-25.10/install/taichi-install.html>`__
* GSplat on ROCm - `Installation instructions <https://rocm.docs.amd.com/projects/gsplat/en/docs-25.10/install/gsplat-install.html>`__