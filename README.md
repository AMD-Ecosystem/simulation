# AMD Simulation Domain

This platform is an open-source GPU computing ecosystem designed for high-performance workloads. The AMD Simulation Toolkit focuses on enabling physical simulations and advanced computational graphics on AMD GPUs. This toolkit enables areas such as scientific computing, computer graphics, robotics, and AI-driven simulations to run on AMD Instinct™ GPUs and benefit from all of the advantages offered by these.

AMD Simulation brings together frameworks and specialized libraries that accelerate physics-based and numerical simulations. These tools leverage the HIP runtime, optimized math libraries, and PyTorch integration to deliver high throughput for compute-intensive tasks. This provides developers with efficient and scalable solutions for real-time and offline simulation workloads.

Physical simulation workloads such as fluid mechanics, rigid body dynamics, and volumetric rendering require enormous computational resources. By leveraging the open-source GPU stack along with the the powerful Instinct product line, developers gain performance through optimized kernels, flexibility through integration with Python and machine learning frameworks, and scalability with support for multi-GPU clusters and HPC environments.

## Taichi

Taichi is an open-source, imperative, and parallel programming language embedded in Python, designed for high-performance numerical computation and real-time physical simulation. It uses just-in-time compilation frameworks such as LLVM to accelerate compute-intensive Python code by compiling it into optimized GPU or CPU instructions. This approach allows developers to write concise, high-level algorithms while leaving performance optimization to Taichi’s compiler.

Taichi is widely used in domains such as fluid dynamics, particle-based simulations, robotics, computer vision, augmented reality, artificial intelligence, and visual effects for gaming and film. For example, simulating a cloth falling onto a sphere, a system with tens of thousands of mass points and springs, can be implemented in Taichi with only a few dozen lines of Python code thanks to its data-oriented design and automatic parallelization. Taichi also supports advanced techniques like hierarchical sparse voxel grids for large-scale simulations, enabling efficient handling of spatially sparse data structures in 3D visual computing.

Taichi is officially supported for AMD Instinct™ GPUs, making it a powerful tool for developers who need both flexibility and performance. To get started, developers can easily get started using prebuilt Taichi Docker images and explore examples in ROCm blogs and Taichi documentation.

## GSplat

gsplat is an open-source library for GPU-accelerated differentiable rasterization of 3D gaussians with Python bindings. It is inspired by the SIGGRAPH paper “3D Gaussian Splatting for Real-Time Rendering of Radiance Fields” [1],

gsplat is built on top of PyTorch, enabling innovators working at the intersection of computer graphics, machine learning, and 3D vision to leverage GPU acceleration with AMD Instinct™ GPUs to build, research, and innovate with Gaussian Splatting.

Gaussian Splatting, often abbreviated as GSplat, is a novel and highly efficient technique for real-time rendering of 3D scenes. It has emerged as a compelling alternative to traditional methods like neural radiance fields (NeRFs), offering significant advantages in terms of rendering speed and quality. Unlike NeRFs, which represent a scene as a complex neural network, Gaussian Splatting models a scene as a collection of 3D Gaussians—ellipsoidal shapes with associated color and opacity properties. This simple yet powerful representation allows for direct and rapid rendering, making it ideal for applications requiring interactive frame rates, such as virtual reality (VR), augmented reality (AR), and video games.

## Documentation

Refer to the individual component pages for documentation on system requirements, installation instructions and examples.

- [GSplat](https://github.com/rocm/gsplat)
- [Taichi](https://github.com/rocm/taichi) 
