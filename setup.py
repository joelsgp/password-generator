import setuptools
import password


##with open('README.md', 'r', encoding='utf-8') as readme_file:
##    long_description = readme_file.read()

setuptools.setup(
    name='password-generator',
    version=password.__version__,
    author='JMcB',
    author_email='joel.mcbride1@live.com',
    description='Simple python password generator',
##    long_description=long_description,
##    long_description_content_type='text/markdown',
    url='https://github.com/JMcB17/password-generator',
    packages=setuptools.find_packages(),
    package_data={
        '': ['words.json'],
    },
    entry_points={
        'console_scripts': [
            'passwordgen=password:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Environment :: Console',
    ],
    python_requires='>=3',
    install_requires=[
        'pyperclip>=1,<2'
    ],
    **{
        'license': 'GPLv3',
    }
)
