TIME_FILE=time.txt

rm -f $TIME_FILE

for nproc in 2 4 8
do
	/usr/bin/time \
        --format="nproc: $nproc real: %E user: %U sys: %S" \
        --output=$TIME_FILE \
        --append \
        mpirun -n $nproc ./mpi_mm
done
