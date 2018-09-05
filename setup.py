from setuptools import setup


def readme():
    with open("README.rst") as f:
        return f.read()


setup(name="configoptions",
      version="1.0.0",
      description="configoptions",
      author="Roy Zhong",
      license="GPL3",
      packages=["configoptions"],
      zip_safe=False)
