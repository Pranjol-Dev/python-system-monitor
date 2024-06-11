# System Information Display Script

This Python script retrieves and displays detailed system information including CPU, memory, and GPU details using `psutil`, `GPUtil`, `colorama`, and `tabulate` libraries.

## Features

- **System Information:** Displays OS platform, node name, release version, machine type, and processor information.
- **CPU Information:** Shows physical and total core count, maximum and minimum CPU frequency, current frequency for each core, and total CPU usage percentage.
- **Memory Information:** Provides total memory, available memory, used memory, memory usage percentage, total swap space, free swap space, used swap space, and swap usage percentage.
- **GPU Information:** Retrieves GPU ID, name, load percentage, free memory, used memory, total memory, and temperature for each GPU installed.

## Libraries Used

- **psutil:** Used to fetch information on system utilization (CPU, memory, disks, network, sensors).
- **GPUtil:** Provides GPU information such as load, memory utilization, and temperature.
- **colorama:** For colored terminal text and styles.
- **tabulate:** Formats the retrieved data into neat tables for better readability in the terminal.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Pranjol-Dev/python-system-monitor.git
   cd your-repository
   ```

2. Install dependencies:
   ```bash
   pip install psutil GPUtil colorama tabulate
   ```

## Usage

Run the script `main.py`:
```bash
python main.py
```

The script will output detailed system information formatted in tables with colored text for clarity.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
