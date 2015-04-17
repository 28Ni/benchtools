mpi_mm: mpi_mm.c
	mpicc -o $@ -O3 $<

run: mpi_mm
	mpirun -n 2 ./$<

bench:
	bash bench.sh

clean:
	rm -f mpi_mm
