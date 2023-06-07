from setuptools import setup, find_namespace_packages

setup(name='clean_folder', # packege name
    version='0.0.1',
    description='Sorter of folder content',
    #url=args_dict['url'], #GitHab reference
    author='Mykhailo Ivanov',
    author_email='ivmv2007@gmail.com',
    license='MIT',
    classifires=[
        "Programming Language :: Python"
        "license :: OSI :: MIT license"
        "Operation System :: OS Independunt"],
    packages=find_namespace_packages(), # looking for all istalled packages
    data_files=['list of data files'], # not done yet
    install_requires='requires',#?
    entry_points={'console_scripts': ['start_sorting = clean_folder.clean:run']} # run : create function to start input of arguments?
    
    )

"""from setuptools import setup, find_namespace_packages

setup(
    name='useful',
    version='1',
    description='Very useful code',
    url='http://github.com/dummy_user/useful',
    author='Flying Circus',
    author_email='flyingcircus@example.com',
    license='MIT',
    packages=find_namespace_packages(),
    install_requires=['markdown'],
    entry_points={'console_scripts': ['helloworld = useful.some_code:hello_world']}
)"""