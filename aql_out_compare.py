import Flow
import sys
import os
import re
import xml.etree.ElementTree as et;
class run_result:
    def __init__(self):
        self.set_recreates=[]
        self.recreates=[]
        self.deterministic=True;

files_suf = [1,2,3,4,5]

cur_dir = os.getcwd()
results = dict()
##flowdroid_droidbench_all_run2/flowdroid/droidbench/campaign0/
for x in files_suf:
    r_dir = cur_dir+"/flowdroid_droidbench_all_run"+str(x)+"/flowdroid/droidbench/campaign0/"
    if not os.path.exists(r_dir):
        break
    files = os.listdir(r_dir)
    for f in files:
        if f.endswith(".apk.raw"):
            results[f] = run_result();
for result_file in results:
    file_vals=[];
    for i in files_suf:
        infile = cur_dir+"/flowdroid_droidbench_all_run"+str(i)+"/flowdroid/droidbench/campaign0/"+result_file;
        if os.path.exists(infile):
            file_vals.append(Flow(et.parse(infile)));
            results[result_file].recreates.append("0");
        else:
            results[result_file].recreates.append("-1");
            results[result_file].setrecreates.append("-1");
    flow_start= file_vals[0];
    for flow in file_vals:
        if(flow_start != flow){
            results[result_file].deterministic = False;
        }
        results[result_file].set_recreates = (flow_start == flow);

print("configuration,project,setequality");
for x in results:
    run_result = results[x];
    a = "";
    a += x[0:x.index("_"):]+","
    a += x[x.index("_"):x.index(".raw")]+",";
    a += run_result.deterministic;