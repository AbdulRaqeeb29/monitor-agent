import docker

def bytes_to_mb(bytes_value):
    return bytes_value / (1024*1024)

def monitor_containers():
    # Connect to Docker
    client = docker.from_env()
    containers = client.containers.list()

    print("docker connected")
    

    # Iterate through containers and insert data into MySQL
    for container in containers:
        print("container strarts")
        stats = container.stats(stream=False)
        container_id = container.id
        print(stats['name'])

        cpu_delta = stats['cpu_stats']['cpu_usage']['total_usage'] - stats['precpu_stats']['cpu_usage']['total_usage']
        system_delta = stats['cpu_stats']['system_cpu_usage'] - stats['precpu_stats']['system_cpu_usage']
        number_of_cores = stats['cpu_stats']["online_cpus"]
        cpu_percent = (cpu_delta / system_delta) * number_of_cores * 100
        print("CPU usage: ",cpu_percent)
        name = stats['name']
        # Calculate memory usage percentage
        total_memory_usage = stats['memory_stats']['usage']
        memory_usage = bytes_to_mb(total_memory_usage)
        print("Total memory usage: ",memory_usage)


if __name__ == "__main__":
    monitor_containers()

