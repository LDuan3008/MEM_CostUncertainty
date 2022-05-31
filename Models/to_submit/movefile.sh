#!/bin/bash

for idx in {84..93} 
do 
    echo 'moving file: time_transient_ensemble'${idx}
    mv /data/carnegie/leiduan/cesm_archive/MEM_CostUncertainty/time_transient_ensemble${idx}_year* /data/carnegie/leiduan/cesm_archive/MEM_CostUncertainty/Transient/
done 
