from setuptools import setup, find_packages

setup(
    name="COVID_CT_Classifier",
    version="0.1",
    description="A classifier for COVID and Non-COVID CT scan images using Fastai, Seaborn, and Scikit-learn.",
    author="Raghav Tigadi",
    author_email="raghavtigadi@fmail.com",
    url="https://github.com/ragztigadi/Classification-of-COVID-Non-COVID-CT-Scan-Images-",
    packages=find_packages(),
    install_requires=[
        "fastai",
        "seaborn",
        "scikit-learn",
        "numpy",     # Other dependencies if needed
        "pandas",
        "matplotlib"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
