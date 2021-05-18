import os, sys
import subprocess
import logging as log
from types import resolve_bases


def get_readability_level(readability_score):
    if readability_score <= 0.4:
        return "LOW"
    elif readability_score > 0.4 and readability_score <= 0.6:
        return "MEDIUM"
    elif readability_score > 0.6:
        return "HIGH"
    else:
        return ""


# list java source files
rootdir = sys.argv[1]

java_files = list()
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file.endswith('.java'):
            java_files.append(os.path.join(subdir, file))

# start CoRed
process_out = list()
p = subprocess.Popen(f'java -jar rsm.jar {" ".join(java_files)}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in p.stdout.readlines():
    process_out.append(line.decode('utf-8').strip())
status = p.wait()

output = list()
if status == 0:
    for line in process_out:
        try:
            row = line.split('\t')
            row.append(get_readability_level(float(row[-1])))
            output.append(row)
            print(', '.join(row))
        except:
            log.error("CoRed parsing error")
else:
    log.error(process_out)

with open("report.csv", 'w') as out:
    out.write("file_name,score,level\n")
    for row in output:
        out.write(",".join(row) + "\n")
