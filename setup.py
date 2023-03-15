from setuptools import setup, find_packages

setup(
    name='flashdetect',
    version='1.0.0',
    author='Bravish Ghosh',
    author_email='bravish.ghosh@outlook.com',
    description='Detects flashing lights and contrasting patterns in videos',
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'numpy',
        'matplotlib',
        'pytube',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ],
)
