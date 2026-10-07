.. meta::
  :description: Learn about the features and capabilities of AMD Simulation
  :keywords: ROCm, simulation, AMD, Instinct, GPU, physics, numerical, solvers, Taichi, GSplat, Gaussian, Splatting, PyTorch, HIP, multi, scaling, high, performance, computing, HPC, real-time, rendering, volumetric, fluid, dynamics, rigid, body, particle, sparse, voxel, grids, differentiable, 3D, vision, computer, graphics, robotics, scientific, toolkit, accelerated

.. rocmds-index:

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

The Simulation Domain includes the following components:

* Taichi Lang is an open-source, imperative, and parallel programming language
  embedded in Python, designed for high-performance numerical computation
  and real-time physical simulation. It uses just-in-time (JIT) compilation
  frameworks such as LLVM to accelerate compute-intensive Python code by
  compiling it into optimized GPU or CPU instructions. Taichi Lang is widely
  used in domains such as fluid dynamics, particle-based simulations, robotics,
  computer vision, augmented reality, artificial intelligence, and visual effects
  for gaming and film.

* GSplat (Gaussian splatting) is an open-source library for GPU-accelerated
  differentiable rasterization of 3D Gaussians with Python bindings. It is
  inspired by the SIGGRAPH paper `"3D Gaussian Splatting for Real-Time
  Rendering of Radiance Fields" <https://dl.acm.org/doi/10.1145/3592433>`__.
  The ROCm-enabled release of GSplat is built on top of PyTorch, enabling
  innovators working at the intersection of computer graphics, machine learning,
  and 3D vision to leverage GPU acceleration for building, research, and
  innovation with Gaussian Splatting.


.. grid:: 2
  :gutter: 3

  .. grid-item-card:: Install

    * :ref:`linux-install`

  .. grid-item-card:: Components

    * `Taichi Lang <https://rocm.docs.amd.com/projects/taichi/en/docs-25.11/>`__
    * `GSplat <https://rocm.docs.amd.com/projects/gsplat/en/docs-25.11/>`__

  .. grid-item-card:: Resources

    * `Taichi Lang on ROCm blog <https://rocm.blogs.amd.com/artificial-intelligence/taichi_mi300x/README.html>`__
    * `GSplat on ROCm blog <https://rocm.blogs.amd.com/software-tools-optimization/gsplat/README.html>`__


