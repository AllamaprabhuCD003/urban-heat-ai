from setuptools import setup, find_packages

setup(
    name='urban-heat-ai',
    version='0.1.0',
    description='A comprehensive automation system for Urban Heat Index detection, forecasting, and recommendations using satellite imagery and machine learning.',
    author='Urban Heat AI Team',
    author_email='team@urbanheatai.com',
    python_requires='>=3.9',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.21.0',
        'pandas>=1.3.0',
        'scikit-learn>=1.0.0',
        'tensorflow>=2.10.0',
        'opencv-python>=4.5.0',
        'matplotlib>=3.4.0',
        'seaborn>=0.11.0',
        'pyyaml>=5.4.0',
        'requests>=2.26.0',
        'python-dotenv>=0.19.0',
        'Pillow>=8.3.0',
    ],
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'pytest-cov>=3.0.0',
            'black>=22.0.0',
            'flake8>=4.0.0',
            'mypy>=0.950',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
