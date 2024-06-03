import os
import glob
import subprocess

def run_mrcc(fort55_file, minp_file):
    if os.path.isfile(fort55_file) and os.path.isfile(minp_file):
        with open("mrcc-output.txt", "w") as output_file:
            subprocess.run(["dmrcc", fort55_file, minp_file], stdout=output_file)
    else:
        if not os.path.isfile(fort55_file):
            print(f"{fort55_file} file not found.")
        if not os.path.isfile(minp_file):
            print(f"{minp_file} file not found.")
