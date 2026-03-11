from setuptools import setup, find_packages

setup(
    name="aws-athena-helper",
    version="0.0.20",
    description="AWS Athena Helper SDK",
    author="mamh1019",
    install_requires=["pandas", "boto3"],
    packages=find_packages(exclude=["tests*"]),
    keywords=["aws", "athena", "datacenter"],
    python_requires=">=3",
    classifiers=["Programming Language :: Python :: 3.7"],
)
