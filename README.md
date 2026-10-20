# AMD Simulation Domain

This platform is an open-source GPU computing ecosystem designed for high-performance workloads. The AMD Simulation Toolkit focuses on enabling physical simulations and advanced computational graphics on AMD GPUs. This toolkit enables areas such as scientific computing, computer graphics, robotics, and AI-driven simulations to run on AMD Instinct™ GPUs and benefit from all of the advantages offered by these.

AMD Simulation brings together frameworks and specialized libraries that accelerate physics-based and numerical simulations. These tools leverage the HIP runtime, optimized math libraries, and PyTorch integration to deliver high throughput for compute-intensive tasks. This provides developers with efficient and scalable solutions for real-time and offline simulation workloads.

Physical simulation workloads such as fluid mechanics, rigid body dynamics, and volumetric rendering require enormous computational resources. By leveraging the open-source GPU stack along with the the powerful Instinct product line, developers gain performance through optimized kernels, flexibility through integration with Python and machine learning frameworks, and scalability with support for multi-GPU clusters and HPC environments.

## Quadrants

Quadrants is a multi-platform compiler for physics simulation. Kernels are written in Python and lowered to parallel code for AMD ROCm (HIP), NVIDIA CUDA, Vulkan, Apple Metal, and x86 and ARM64 CPUs. Genesis uses Quadrants for the numeric kernels inside its solvers, collision code, and linear algebra. This ROCm edition tracks upstream Quadrants 1.3.3 on the `rocm10.1.0_r26.10` branch.

## Genesis

Genesis is a simulation platform for physical AI. It combines a unified multi-physics engine, camera rendering, and a Python scene API so the same scene can step rigid robots, deformable materials, fluids, and coupled solvers. Numeric kernels are compiled with Quadrants. This ROCm edition tracks upstream Genesis 1.4.3 on the `rocm10.1.0_r26.10` branch.

## Warp

Warp is a single library hosted at [AMD-Ecosystem/warp](https://github.com/AMD-Ecosystem/warp). It takes regular Python functions and JIT-compiles them to efficient kernel code for physics simulation, perception, robotics, and geometry processing, and runs MuJoCo Warp workloads on AMD Instinct GPUs. This release tracks upstream Warp 1.13.0.

## MJWarp

MJWarp (MuJoCo Warp) is a GPU-accelerated version of the MuJoCo physics simulator hosted at [AMD-Ecosystem/mujoco_warp](https://github.com/AMD-Ecosystem/mujoco_warp). It is written in Warp and simulates many independent worlds in parallel on AMD Instinct GPUs for reinforcement learning, motion planning, and large-scale evaluation. This release tracks upstream MJWarp 3.8.1 on the `release/v3.8.1` branch.

## Taichi

Taichi is an open-source, imperative, and parallel programming language embedded in Python, designed for high-performance numerical computation and real-time physical simulation. It uses just-in-time compilation frameworks such as LLVM to accelerate compute-intensive Python code by compiling it into optimized GPU or CPU instructions. This approach allows developers to write concise, high-level algorithms while leaving performance optimization to Taichi’s compiler.

## GSplat

gsplat (Gaussian Splatting) is an open-source library for GPU-accelerated differentiable rasterization of 3D gaussians with Python bindings. It is inspired by the SIGGRAPH paper “3D Gaussian Splatting for Real-Time Rendering of Radiance Fields” [1]. gsplat is built on top of PyTorch, enabling innovators working at the intersection of computer graphics, machine learning, and 3D vision to leverage GPU acceleration with AMD Instinct™ GPUs to build, research, and innovate with Gaussian Splatting.


## Documentation

Refer to the individual component pages for documentation on system requirements, installation instructions and examples.

- [Quadrants](https://rocm.docs.amd.com/projects/quadrants/en/latest/)
- [Genesis](https://rocm.docs.amd.com/projects/genesis/en/latest/)
- [Warp](https://rocm.docs.amd.com/projects/warp/en/latest/)
- [MJWarp](https://rocm.docs.amd.com/projects/mujoco-warp/en/latest/)
- [GSplat](https://rocm.docs.amd.com/projects/gsplat/en/latest/)
- [Taichi](https://rocm.docs.amd.com/projects/taichi/en/latest/)
