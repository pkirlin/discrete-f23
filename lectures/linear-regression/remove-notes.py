import os
import subprocess

for filename in os.listdir():
    if filename.endswith(".ipynb") and filename[:-6].endswith("withnotes"):
        subprocess.run(["jupyter", "nbconvert", filename, "--TagRemovePreprocessor.enabled=True", \
		"--TagRemovePreprocessor.remove_cell_tags", "comment", "--to", "notebook", "--output=" + filename[:(-6 - 9 - 1)]])
        print(f"{filename} has been converted")


#jupyter nbconvert mynotebook.ipynb --TagRemovePreprocessor.enabled=True --TagRemovePreprocessor.remove_cell_tags remove_cell
