# Jupyter Notebooks

We will be using [Jupyter Notebooks](https://jupyter.org/) in this class as a 
way to explore machine
learning concepts, complete in-class activities, and work on projects.

## Getting started

If you are familiar with Jupyter notebooks, you can use whatever environment you 
want to run them.  If you are not familiar with them, there are a few ways to get
started.

### JupyterLab Desktop (easiest)

If you don't already have a Jupyter notebook environment installed, this is what
I recommend to get started.  This will install a Jupyter notebook environment
that runs as a standalone application.

Download the installer:
- [macOS Installer](https://github.com/jupyterlab/jupyterlab-desktop/releases/latest/download/JupyterLab-Setup-macOS.dmg)
- [Windows Installer](https://github.com/jupyterlab/jupyterlab-desktop/releases/latest/download/JupyterLab-Setup-Windows.exe)
- [Debian, Ubuntu Linux Installer](https://github.com/jupyterlab/jupyterlab-desktop/releases/latest/download/JupyterLab-Setup-Debian.deb)
- [Red Hat, Fedora, SUSE Linux Installer](https://github.com/jupyterlab/jupyterlab-desktop/releases/latest/download/JupyterLab-Setup-Fedora.rpm)

Once you have downloaded and installed JupyterLab Desktop, run it how you would 
normally run applications on Mac or Windows.

### Run JupyterLab through Anaconda (2nd-easiest) 

If you have an Anaconda distribution of Python already downloaded and installed, you 
already have JupyterLab:

- Open Anaconda Navigator.  Find JupyterLab and click Launch.
  ![<# alt text #>]({{ site.baseurl }}/jupyter-anaconda.png "Screenshot")
- **Note:** You can use the link to "Notebook" rather than JupyterLab, but the interface is not as nice. 

### Run JupyterLab through the command line

If you feel comfortable at the command line and have a working Python installation, you can install Jupyterlab
using one of these methods:

- Via `pip`:
  - `pip install jupyterlab`
  
- Via `conda`:
  - `conda install -c conda-forge jupyterlab`
  
Run JupyterLab with the command `jupyter-lab`.

## Getting the notebooks for class

I will distribute notebooks for class via Git.  If you haven't used or Git or Github before, that's ok!  Here's the easy way to get set up:

- Download Github Desktop and install it: [https://desktop.github.com/](https://desktop.github.com/)
- Run the program and choose File -> Clone Repository.
  - Choose "URL," then enter `https://github.com/pkirlin/ml-s23-materials` for the repository URL.
  - Under "Local Path," click "Choose..." and find a place on your computer you want to store your notebooks for this class.  I recommend creating a new folder for this.
  - Then Click "Clone."
  
  ![<# alt text #>]({{ site.baseurl }}/github-clone.png "Screenshot")
- This will download a number of notebooks into the folder you chose.

### Updating the repository

- There will frequently be new notebooks for you to download.  The easiest way to update them is:
- Open Github Desktop and choose "Fetch origin" from the toolbar area at the top:
  ![<# alt text #>]({{ site.baseurl }}/github-fetch.png "Screenshot")
- Once you do that, if there are updates you haven't downloaded yet, the button will change to "Pull origin," and you can click it again to download the new notebooks.
  ![<# alt text #>]({{ site.baseurl }}/github-pull.png "Screenshot")