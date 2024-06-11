import os
import platform
import psutil
import GPUtil
import colorama
from colorama import Fore, Style
from tabulate import tabulate

# Initialize colorama
colorama.init(autoreset=True)

def get_system_info():
    uname = platform.uname()
    system_info = [
        [f"{Fore.YELLOW}System{Style.RESET_ALL}", uname.system],
        [f"{Fore.YELLOW}Node Name{Style.RESET_ALL}", uname.node],
        [f"{Fore.YELLOW}Release{Style.RESET_ALL}", uname.release],
        [f"{Fore.YELLOW}Version{Style.RESET_ALL}", uname.version],
        [f"{Fore.YELLOW}Machine{Style.RESET_ALL}", uname.machine],
        [f"{Fore.YELLOW}Processor{Style.RESET_ALL}", uname.processor]
    ]
    return system_info

def get_cpu_info():
    cpufreq = psutil.cpu_freq()
    cpu_info = [
        [f"{Fore.CYAN}Physical cores{Style.RESET_ALL}", psutil.cpu_count(logical=False)],
        [f"{Fore.CYAN}Total cores{Style.RESET_ALL}", psutil.cpu_count(logical=True)],
        [f"{Fore.CYAN}Max Frequency{Style.RESET_ALL}", f"{cpufreq.max:.2f}Mhz"],
        [f"{Fore.CYAN}Min Frequency{Style.RESET_ALL}", f"{cpufreq.min:.2f}Mhz"],
        [f"{Fore.CYAN}Current Frequency{Style.RESET_ALL}", f"{cpufreq.current:.2f}Mhz"]
    ]
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        cpu_info.append([f"{Fore.CYAN}Core {i}{Style.RESET_ALL}", f"{percentage}%"])
    cpu_info.append([f"{Fore.CYAN}Total CPU Usage{Style.RESET_ALL}", f"{psutil.cpu_percent()}%"])
    return cpu_info

def get_memory_info():
    svmem = psutil.virtual_memory()
    swap = psutil.swap_memory()
    memory_info = [
        [f"{Fore.GREEN}Total Memory{Style.RESET_ALL}", f"{get_size(svmem.total)}"],
        [f"{Fore.GREEN}Available Memory{Style.RESET_ALL}", f"{get_size(svmem.available)}"],
        [f"{Fore.GREEN}Used Memory{Style.RESET_ALL}", f"{get_size(svmem.used)}"],
        [f"{Fore.GREEN}Percentage{Style.RESET_ALL}", f"{svmem.percent}%"],
        [f"{Fore.GREEN}Total Swap{Style.RESET_ALL}", f"{get_size(swap.total)}"],
        [f"{Fore.GREEN}Free Swap{Style.RESET_ALL}", f"{get_size(swap.free)}"],
        [f"{Fore.GREEN}Used Swap{Style.RESET_ALL}", f"{get_size(swap.used)}"],
        [f"{Fore.GREEN}Percentage Swap{Style.RESET_ALL}", f"{swap.percent}%"]
    ]
    return memory_info

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def get_gpu_info():
    gpus = GPUtil.getGPUs()
    gpu_info = []
    for gpu in gpus:
        gpu_info.append([
            f"{Fore.MAGENTA}GPU ID{Style.RESET_ALL}", gpu.id
        ])
        gpu_info.append([
            f"{Fore.MAGENTA}GPU Name{Style.RESET_ALL}", gpu.name
        ])
        gpu_info.append([
            f"{Fore.MAGENTA}GPU Load{Style.RESET_ALL}", f"{gpu.load * 100}%"
        ])
        gpu_info.append([
            f"{Fore.MAGENTA}GPU Free Memory{Style.RESET_ALL}", f"{gpu.memoryFree}MB"
        ])
        gpu_info.append([
            f"{Fore.MAGENTA}GPU Used Memory{Style.RESET_ALL}", f"{gpu.memoryUsed}MB"
        ])
        gpu_info.append([
            f"{Fore.MAGENTA}GPU Total Memory{Style.RESET_ALL}", f"{gpu.memoryTotal}MB"
        ])
        gpu_info.append([
            f"{Fore.MAGENTA}GPU Temperature{Style.RESET_ALL}", f"{gpu.temperature} °C"
        ])
    return gpu_info

def display_info():
    system_info = get_system_info()
    cpu_info = get_cpu_info()
    memory_info = get_memory_info()
    gpu_info = get_gpu_info()
    
    print(f"{Fore.YELLOW}{'System Information':^50}{Style.RESET_ALL}")
    print(tabulate(system_info, tablefmt="fancy_grid"))
    print("\n")
    
    print(f"{Fore.CYAN}{'CPU Information':^50}{Style.RESET_ALL}")
    print(tabulate(cpu_info, tablefmt="fancy_grid"))
    print("\n")
    
    print(f"{Fore.GREEN}{'Memory Information':^50}{Style.RESET_ALL}")
    print(tabulate(memory_info, tablefmt="fancy_grid"))
    print("\n")
    
    print(f"{Fore.MAGENTA}{'GPU Information':^50}{Style.RESET_ALL}")
    print(tabulate(gpu_info, tablefmt="fancy_grid"))
    print("\n")

if __name__ == "__main__":
    display_info()
