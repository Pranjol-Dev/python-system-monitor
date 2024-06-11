# Python System Monitor

Python script to display detailed system information including CPU, memory, and GPU stats using `psutil`, `GPUtil`, `colorama`, and `tabulate` libraries. Provides clear, formatted output in the terminal.

![System Information Screenshot](https://i.imgur.com/nhFXw0I_d.webp?maxwidth=760&fidelity=grand)

![GPU Information Screenshot](https://i.imgur.com/4QAVvoX_d.webp?maxwidth=760&fidelity=grand)

## Features

- **System Information:** Displays OS platform, node name, release version, machine type, and processor information.
- **CPU Information:** Shows physical and total core count, maximum and minimum CPU frequency, current frequency for each core, and total CPU usage percentage.
- **Memory Information:** Provides total memory, available memory, used memory, memory usage percentage, total swap space, free swap space, used swap space, and swap usage percentage.
- **GPU Information:** Retrieves GPU ID, name, load percentage, free memory, used memory, total memory, and temperature for each GPU installed.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Pranjol-Dev/python-system-monitor.git
   cd python-system-monitor
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
