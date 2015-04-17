mkdir -p /scratch/$USER/mpi_mm
TIME_FILE=/scratch/$USER/mpi_mm/time.txt
rm -f $TIME_FILE

for nproc in 2 4 8
do
    oarsub \
        -l /core=$nproc,walltime=00:05:00 \
        "./rioc_script.sh $nproc"
done
