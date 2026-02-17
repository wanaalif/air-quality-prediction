"""
Setup configuration for Air Quality Prediction package.
"""

from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Read requirements
with open('requirements.txt') as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name='air-quality-prediction',
    version='1.0.0',
    author='Smart City Group',
    author_email='wanalifdanial03@gmail.com',
    description='Air Quality Prediction for Smart Cities using Multi-Layer Perceptron',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/wanaalif/air-quality-prediction',
    project_urls={
        'Bug Reports': 'https://github.com/yourusername/air-quality-prediction/issues',
        'Source': 'https://github.com/yourusername/air-quality-prediction',
        'Documentation': 'https://github.com/yourusername/air-quality-prediction/blob/main/README.md',
    },
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.8',
    install_requires=requirements,
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'pytest-cov>=3.0.0',
            'black>=22.0.0',
            'flake8>=4.0.0',
            'mypy>=0.950',
        ],
        'docs': [
            'sphinx>=4.0.0',
            'sphinx-rtd-theme>=1.0.0',
        ],
    },
    entry_points={
        'console_scripts': [
            'airquality-train=src.train:main',
            'airquality-predict=src.predict:main',
            'airquality-evaluate=src.evaluate:main',
        ],
    },
    include_package_data=True,
    package_data={
        '': ['*.txt', '*.md'],
    },
    keywords='air-quality machine-learning deep-learning environmental-monitoring smart-cities',
    zip_safe=False,
)
