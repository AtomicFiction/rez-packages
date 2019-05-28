name = "flann"

version = "1.9.1"

authors = [
    "Marius Muja"
]

description = \
    """
    FLANN is a library for performing fast approximate nearest neighbor searches in high dimensional spaces.
    """

private_build_requires = [
    "gcc-4.8+<5",
]

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-7"]
]

uuid = "c867cfe7-52b2-4883-afbb-363ee2292eda"
