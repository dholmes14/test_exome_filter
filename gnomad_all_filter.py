import os

x = os.system("""awk -F'\t' ' {if ($78<0.001 && $78>=0) { counter++ };
if(!$78) {counter++};
print ("Gnomad_freq_all: " $78 "\t" "Filter count: " counter) }' WE_EX1807150-WE_EX1807151-WE_EX1807152.alamut.txt""")
print x
