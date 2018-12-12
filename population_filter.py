import os
x = os.system("""awk -F'\t' '{
max_maf = 0
if($79>max_maf) {max_maf=$79
    population = "gnomadAltFreq_afr"};

if($80>max_maf) {max_maf=$80
    population = "gnomadAltFreq_amr"};

if($82>max_maf) {max_maf=$82
    population = "gnomadAltFreq_eas"};

if($83>max_maf) {max_maf=$83
    population = "gnomadAltFreq_sas"};

if($84>max_maf) {max_maf=$84
    population = "gnomadAltFreq_nfe"};

if(max_maf >= 0.001) {population = "Common           "};

if(max_maf < 0.001 && max_maf > 0)
  { counter++ };

if(!$78) {counter++
    population = "Blank            "};

print (population":""\t" max_maf "\t" "Filter count: ""\t" counter " afr: "$79 "\t" "amr: "$80 "\t" "eas: "$82 "\t" "sas: "$83 "\t" "nfe: "$84 "\t" " all: " $78);


}' WE_EX1807150-WE_EX1807151-WE_EX1807152.alamut.txt""")
print x
