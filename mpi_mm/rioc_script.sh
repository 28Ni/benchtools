TIME_FILE=/scratch/$USER/mpi_mm/time.txt

nproc=$1

/usr/bin/time \
    --format="nproc: $nproc real: %E user: %U sys: %S" \
    --output=$TIME_FILE \
    --append \
    /cm/shared/apps/openmpi/1.8.4/bin/mpirun \
        -machinefile $OAR_FILE_NODES \
        -mca plm_rsh_agent "oarsh" \
        -np $nproc \
        ./mpi_mm
