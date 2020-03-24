import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='JTools',  
     version='1.1',
    
     author="Joshua Zack",
     author_email="jbot237@gmail.com",
     
    description="Mysc Usfull tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    
    url="https://github.com/Quiltic/JTools",
    packages=setuptools.find_packages(),
    include_package_data = True,
    
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
