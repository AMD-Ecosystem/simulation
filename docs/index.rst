.. meta::
  :description: Learn about the features and capabilities of AMD Simulation
  :keywords: ROCm, simulation, AMD, Instinct, GPU, physics, numerical, solvers, Quadrants, Genesis, Warp, MJWarp, MuJoCo, PyTorch, HIP, multi, scaling, high, performance, computing, HPC, real-time, rendering, volumetric, fluid, dynamics, rigid, body, particle, sparse, voxel, grids, differentiable, 3D, vision, computer, graphics, robotics, scientific, toolkit, accelerated

.. amd-simulation-index:

********************************************************************
AMD Simulation documentation
********************************************************************

AMD Simulation is an open-source software toolkit built on the ROCm™ platform,
enabling high-performance physical simulations and advanced computational graphics
on AMD GPUs. This toolkit enables workloads such as scientific computing, computer
graphics, robotics, and AI-driven simulation to run on AMD Instinct™ GPUs and benefit
from the optimizations available on those GPUs. AMD Simulation builds on the core
ROCm libraries to combine frameworks and specialized libraries that accelerate
physics-based and numerical simulations.

These tools use ROCm's HIP runtime, optimized math libraries, and PyTorch
integration to deliver high throughput for compute-intensive tasks. This provides
you with efficient, scalable solutions for real-time and offline simulation workloads.
Physical simulation workloads, such as fluid mechanics, rigid-body dynamics, and
volumetric rendering, require significant computational resources. By leveraging
ROCm's open-source GPU stack together with the AMD Instinct product line, you gain
performance from optimized kernels, flexibility from integration with Python and
machine learning frameworks, and scalability with multi-GPU clusters and high-
performance computing (HPC) support.

AMD Simulation provides a cohesive set of libraries and frameworks that support
the simulation workflow, from physics kernels and numerical solvers to
rendering and multi-GPU scaling. Each component is optimized for GPU performance 
on AMD Instinct GPUs while offering Python-friendly APIs and integrations with
popular tools such as PyTorch, so that you can plug simulation workloads into existing 
research and production pipelines with minimal friction.


.. grid:: 2
  :gutter: 3

  .. grid-item-card:: Install

    * :ref:`linux-install`

  .. grid-item-card:: Components

    * `Quadrants <https://rocm.docs.amd.com/projects/quadrants/en/docs-26.10/>`__
    * `Genesis <https://rocm.docs.amd.com/projects/genesis/en/docs-26.10/>`__
    * `Warp <https://rocm.docs.amd.com/projects/warp/en/docs-26.10/>`__
    * `MuJoCo Warp <https://rocm.docs.amd.com/projects/mujoco-warp/en/docs-26.10/>`__


