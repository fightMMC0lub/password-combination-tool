from setuptools import setup, find_packages

setup(
    name='password-combination-tool',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'password-combination-tool=password_combination_tool:main',
        ],
    },
    description='A tool for calculating password combinations',
    long_description="""
        For more details, check out the following:
        - **Official Website**: [FightMMC0lub](https://fightmmc0lub.github.io/)
        - **Blogger**: [The0xTechWorld](https://the0xtechworld.blogspot.com/)
    """,
    author='Fouad',
    author_email='jihgeharverserv@gmail.com',
    url='https://github.com/fightMMC0lub/password-combination-tool',
)
