.. meta::
    :description: AMD Simulation installation
    :keywords: ROCm, simulation, AMD, Instinct, GPU, physics, numerical, solvers, Taichi, GSplat, Gaussian, Splatting, PyTorch, HIP, multi, scaling, high, performance, computing, HPC, real-time, rendering, volumetric, fluid, dynamics, rigid, body, particle, sparse, voxel, grids, differentiable, 3D, vision, computer, graphics, robotics, scientific, toolkit, accelerated

.. _linux-install:

**************************************************************************************
Install AMD Simulation
**************************************************************************************

This topic provides brief guidance and recommendations on setting up a ROCm-enabled 
environment for simulation workloads. This includes pulling and running a prebuilt 
ROCm Docker image for supported Ubuntu versions and installing components.

System requirements
======================================================================================

The AMD Simulation components are both supported on AMD Instinct™ MI325X and MI300X GPUs.

To use both Taichi Lang and GSplat, you need the following prerequisites:

- **ROCm version:** `7.0.0 <https://repo.radeon.com/rocm/apt/7.0/>`__ 
- **Operating system:** Ubuntu 22.04, 24.04
- **PyTorch:** `2.8 <https://github.com/ROCm/pytorch/tree/v2.8.0>`__ (ROCm-enabled)
- **Python:** `3.12.3 <https://www.python.org/downloads/release/python-3123/>`__, `3.10.12 <https://www.python.org/downloads/release/python-31012/>`__

.. note::

   If you are only installing Taichi Lang or GSplat, see the :ref:`simulation-compat-matrix` page.

Install AMD Simulation 
======================================================================================

After confirming your system meets the supported hardware and software configurations, follow these steps:

1. Install the supported ROCm version. To do this, pull a ROCm dev Docker image with a supported
   configuration (see `Docker Hub <https://hub.docker.com/u/rocm?page=1&search=dev-ubuntu-2>`__
   to browse available images).

   .. tab-set::

      .. tab-item:: Ubuntu 24.04
         :sync: ubuntu-24

         .. code-block:: shell

            docker pull rocm/dev-ubuntu-24.04:7.0-complete

         See `rocm/dev-ubuntu-24.04:7.0-complete
         <https://hub.docker.com/layers/rocm/dev-ubuntu-24.04/7.0-complete/images/sha256-ffd8ac00ca6c8e2dbfd0c364c7cc27542f90148f3f358d74efd028f67c33607b>`__
         on Docker Hub.

      .. tab-item:: Ubuntu 22.04
         :sync: ubuntu-22

         .. code-block:: shell

            docker pull rocm/dev-ubuntu-22.04:7.0-complete

         See `rocm/dev-ubuntu-22.04:7.0-complete
         <https://hub.docker.com/layers/rocm/dev-ubuntu-22.04/7.0-complete/images/sha256-b4be4b0b29e46d56e9bea2cd06500f4519aaac30dc5df02bd4710bbf393c1c4c>`__
         on Docker Hub.

2. Launch the Docker container.

   .. tab-set::

      .. tab-item:: Ubuntu 24.04
         :sync: ubuntu-24

         .. code-block:: shell

            docker run -it \
                  --cap-add=SYS_PTRACE \
                  --ipc=host \
                  --privileged=true \
                  --shm-size=128GB \
                  --network=host \
                  --device=/dev/kfd \
                  --device=/dev/dri \
                  --group-add video \
                  -v $HOME:$HOME \
                  --name rocm7 \
                  rocm/dev-ubuntu-24.04:7.0-complete

      .. tab-item:: Ubuntu 22.04
         :sync: ubuntu-22

         .. code-block:: shell

            docker run -it \
                  --cap-add=SYS_PTRACE \
                  --ipc=host \
                  --privileged=true \
                  --shm-size=128GB \
                  --network=host \
                  --device=/dev/kfd \
                  --device=/dev/dri \
                  --group-add video \
                  -v $HOME:$HOME \
                  --name rocm7 \
                  rocm/dev-ubuntu-22.04:7.0-complete

3. Install each AMD Simulation component. The installation instructions for each component can be found as follows: 

   * Taichi Lang on ROCm - `Installation instructions <https://rocm.docs.amd.com/projects/taichi/en/docs-25.11/install/taichi-install.html>`__
   * GSplat on ROCm - `Installation instructions <https://rocm.docs.amd.com/projects/gsplat/en/docs-25.11/install/gsplat-install.html>`__