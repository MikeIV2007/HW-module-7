from setuptools import setup, find_namespace_packages

setup(name='clean_folder', # packege name
    version='0.0.1',
    description='Sorter of folder content',
    url='https://github.com/MikeIV2007/HW-module-7/tree/main/clean_folder', #GitHab reference
    author='Mykhailo Ivanov',
    author_email='ivmv2007@gmail.com',
    license='MIT',
    classifires=[
        "Programming Language :: Python"
        "license :: OSI :: MIT license"
        "Operation System :: OS Independunt"],
    packages=find_namespace_packages(), # looking for all istalled packages
    #data_files=['list of data files'], # not done yet
    #include_package_data=True
    install_requires='requires',#?
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']} # main : created function to privide input of arguments by means of sysargv
    
    )

