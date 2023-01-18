# Deep-Reinforcement-Learning-Jan.2023

As reinforcement learning materials conducted from January, I mainly studied through Reinforcement Learning with Python and Keras, author Lee Woong-won, and Wikibooks.
(Book information : http://www.yes24.com/Product/Goods/44136413)

By reading related papers, we are laying the foundation for reinforcement learning, and we intend to apply it to hardware implementation.

# 1. Before we start it...

Install the Anaconda Library. (Installization : https://www.anaconda.com/products/individual)

Installation can be done by default.

When the anaconda installation is complete, turn on the anaconda prompt and enter 'conda env list'. (env = environment)

Caution: Command recognition is possible only when 'conda' is added to the front.

# 2. Configuring the Anaconda Basic Environment

If you enter 'conda env list', you can see that only the base exists.

Enter 'conda create -n [virtual environment name] python=3.7' to proceed in a new virtual environment (that is the purpose of Anaconda).

A new environment with the virtual environment name is then created in python 3.7 version.

If you enter 'conda env list' again in base, you can check the name of the productive virtual environment just now.

Finally, you can enter the virtual environment directory created in the base directory by entering 'condactivate'.

# 3. Download libraries and packages required for learning

If you've just finished creating and entering a virtual environment, you should now download what you need to learn.

You can download it by typing it in the next search box. (Download : https://anaconda.org/)

ex) To download the tensorflow, enter 'conda install -conda-forge tensorflow' at the command prompt to install.

Enter y or enter when asking 'y/n' during installation.

Since the required library is different depending on the learning purpose, the library is selected and downloaded according to the learning purpose.

Caution: It depends on your computer environment (or GPU), so you need to see and install the version carefully.

# 4. Install PyCharm IDE

IDE is an integrated development environment, meaning can be found at https://en.wikipedia.org/wiki/Integrated_development_environment).

It is important to look at English materials as much as possible while studying, and once you read them carefully, it will be very helpful for development.

Among them, PyCharm is one of the most used environments. (Actually, I think I use Visual Studio Code more, but it doesn't matter.)

Download it from https://www.jetbrains.com/ko-kr/pycharm/download/#section=windows.

It can also be installed as default like anaconda.

# 5. PyCharm Interpreter setting

Once the installation is complete, you can select a page where you can proceed with the new project.

At the selection stage, you will select Python interpreters, which can be done through the anaconda you just installed.

Select the virtual environment name file that you created in the user's envs file and select 'python.exe' there.

Occasionally, the interpreter changes while proceeding, and the library is not recognized, so the code does not work, so you need to check it through settings.

At the end of this stage, it can be said that preparations for basic use are completed.

*This file was translated by Papago (https://papago.naver.com/)*
