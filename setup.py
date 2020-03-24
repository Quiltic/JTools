import setuptools

setuptools.setup(
     name='JTools',  
     version='1.1',
    
     author="Joshua Zack",
     author_email="jbot237@gmail.com",
     
    description="Mysc Usfull tools",
    long_description=open('README.md').read(),
    license='MIT',
    
    url="https://github.com/Quiltic/JTools",
    packages=setuptools.find_packages(),
    include_package_data = True,
    
    classifiers=[
         "Programming Language :: Python :: 3,
         "Operating System :: OS Independent",
     ],
 )
