from setuptools import setup, find_packages

setup(
    name='flash_detect',
    version='0.1',
    description='A package for analyzing videos for flashing lights and contrasting light and dark patterns',
    url='https://github.com/LoopGlitch26/FlashDetect',
    author='Bravish Ghosh',
    author_email='bravish.ghosh@outlook.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'pytube',
        'opencv-python',
        'numpy',
        'matplotlib'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='video analysis flashing lights contrast',
)
