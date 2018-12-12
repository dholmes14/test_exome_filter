import os
x = os.system("""awk -F'\t' '{
if ($1=="gnomadAltFreq_afr:") {afrcounter++}

if ($1=="gnomadAltFreq_amr:") {amrcounter++}

if ($1=="gnomadAltFreq_eas:") {eascounter++}

if ($1=="gnomadAltFreq_sas:") {sascounter++}

if ($1=="gnomadAltFreq_nfe:") {nfecounter++}

if ($1=="Blank            :") {blankcounter++}

if ($1=="Common           :") {commoncounter++}
total = (afrcounter + amrcounter + eascounter + sascounter + nfecounter + blankcounter)
print (" afr: " afrcounter "\t" " amr: " amrcounter "\t" " eas: " eascounter "\t" " sas: " sascounter "\t" " nfe: " nfecounter "\t" " Blank: " blankcounter "\t" " Common: " commoncounter "\t" " total: "total)

}' populations.txt""")
print x
