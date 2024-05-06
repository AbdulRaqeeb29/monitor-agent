import time
import docker
import mysql.connector

def bytes_to_mb(bytes_value):
    return bytes_value / (1024*1024)

def monitor_containers():
    while True:
        try:
            
            client = docker.from_env()
            containers = client.containers.list()

            
            db_connection = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='root',
                database='monitor_agent',
                auth_plugin='mysql_native_password'
            )
            cursor = db_connection.cursor()

            # Iterate through containers and insert data into MySQL
            for container in containers:
                stats = container.stats(stream=False)
                container_id = container.id
                # cpu usage (%)
                cpu_delta = stats['cpu_stats']['cpu_usage']['total_usage'] - stats['precpu_stats']['cpu_usage']['total_usage']
                system_delta = stats['cpu_stats']['system_cpu_usage'] - stats['precpu_stats']['system_cpu_usage']
                number_of_cores = stats['cpu_stats']["online_cpus"]
                cpu_percent = (cpu_delta / system_delta) * number_of_cores * 100
                name = stats['name']

                # memory usage (mb)
                total_memory_usage = stats['memory_stats']['usage']
                memory_usage = bytes_to_mb(total_memory_usage)

                
                sql = "INSERT INTO container_stats (container_id, container_name, cpu_usage, memory_usage) VALUES (%s, %s, %s,  %s)"
                val = (container_id, name, cpu_percent, memory_usage)
                cursor.execute(sql, val)

            
            db_connection.commit()
            cursor.close()
            db_connection.close()

            print("Data inserted successfully.")

        except Exception as e:
            print(f"An error occurred: {str(e)}")

        # Insert data every two minutes.
        time.sleep(120)

if __name__ == "__main__":
    monitor_containers()
