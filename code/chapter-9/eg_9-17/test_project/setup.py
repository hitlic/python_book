from setuptools import setup, find_packages

desc = '工具包的简要说明'
long_description = open('./README.md').read()

setup(
    name="testlibpy",
    version="0.0.3",
    author="pystudy",
    author_email="xxxxxx@xxxxxx.com",
    license='MIT',
    description=desc,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://xxxxxx.com/testlibpy",
    classifiers=[ 'Development Status :: 3 - Alpha',
                  'Programming Language :: Python :: 3',
                  'Operating System :: OS Independent'],
    packages=find_packages(include=['testlibpy']), 
    install_requires=['numpy > 1.15'],
    python_requires='>=3.6',
)