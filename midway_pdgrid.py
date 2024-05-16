from mpi4py import MPI
from pd_grid import batch_run

# set input parameters
height = 20
width = 20
schedule_type = 'Sequential'
iteration_num = 1
max_steps_num = 30
collection_frequency = 10

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank() # which core is being used. (0), (0, 1), ..., (0, 1, ..., 19)
size = comm.Get_size() # num of cores requested. 1, 2, ..., 20

sim_per_core = iteration_num // size
if rank == size - 1:
    sim_per_core += iteration_num % size

start_time = MPI.Wtime()
batch_run.batch_run(height, width, schedule_type, iteration_num, max_steps_num,collection_frequency)
end_time = MPI.Wtime()
compiled_duration = end_time - start_time

# Calculate total time spent across all ranks
total_compiled_duration = comm.reduce(compiled_duration, op=MPI.SUM, root=0)

# Print results from rank 0 and store the speedup data
if rank == 0:
    print("--------------------------------")
    print("Cores requested this run:", size)
    print("Total duration across all ranks:", total_compiled_duration)
