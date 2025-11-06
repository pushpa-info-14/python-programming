import re
from typing import List

file_path = "input.txt"  # Replace with the actual path to your file
mp = {}
lines = []

try:
    with open(file_path, 'r') as file:
        for line in file:
            lines.append(line.strip())
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")


for line in lines:
    match = re.search(r'Include="([^"]+)"', line)
    if match:
        package_name = match.group(1).lower()
        mp[package_name] = line

for key in sorted(mp.keys()):
    print(mp[key])