import os

from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension


ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
ESIM_CUDA_FILE_PATH = os.path.join(ROOT_PATH, "src/esim_torch/esim_cuda_kernel.cu")
ESIM_CPP_FILE_PATH = os.path.join(ROOT_PATH, "src/esim_torch/esim_cuda.cpp")

assert os.path.exists(
    ESIM_CUDA_FILE_PATH
), f"ESIM_CUDA_FILE_PATH not found: {ESIM_CUDA_FILE_PATH}"

setup(
    name="esim_torch",
    package_dir={"": "src"},
    packages=["esim_torch"],
    ext_modules=[
        CUDAExtension(
            name="esim_cuda",
            sources=[
                # ESIM_CPP_FILE_PATH,
                ESIM_CUDA_FILE_PATH,
            ],
            extra_compile_args={
                "cxx": ["-g"],
                "nvcc": ["-O3", "-use_fast_math", "-allow-unsupported-compiler"],
            },
        )
    ],
    cmdclass={"build_ext": BuildExtension.with_options(use_ninja=False)},
)
