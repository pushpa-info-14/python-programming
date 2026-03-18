import xml.etree.ElementTree as ET
from collections import defaultdict
import os

solution_path = r"C:\Projects\transvirtual-web-v1\TransVirtual.Web.sln"

csproj_files = [
    r"C:\Projects\transvirtual-web-v1\Actions\Actions.csproj",
    r"C:\Projects\transvirtual-web-v1\ThirdPartyWebServices\ThirdPartyWebServices.csproj",
    r"C:\Projects\transvirtual-web-v1\TransVirtual.AspNet.Owin\TransVirtual.AspNet.Owin.csproj",
    r"C:\Projects\transvirtual-web-v1\TransVirtual.Common\TransVirtual.Common.csproj",
    r"C:\Projects\transvirtual-web-v1\TransVirtual.Common.Legacy\TransVirtual.Common.Legacy.csproj",
    r"C:\Projects\transvirtual-web-v1\TransVirtual.Common.Tests\TransVirtual.Common.Tests.csproj",
    r"C:\Projects\transvirtual-web-v1\TransVirtual.ConsoleTester\TransVirtual.ConsoleTester.csproj",
    r"C:\Projects\transvirtual-web-v1\TransVirtual.Deployment\TransVirtual.Deployment.csproj",
    r"C:\Projects\transvirtual-web-v1\TransVirtual.Infra\TransVirtual.Infra.csproj",
    r"C:\Projects\transvirtual-web-v1\TransVirtual.ServerUtility\TransVirtual.ServerUtility.csproj",
    r"C:\Projects\transvirtual-web-v1\TransVirtual.Service.Commander\TransVirtual.Service.Commander.csproj",
    r"C:\Projects\transvirtual-web-v1\TransVirtual.Service.Common\TransVirtual.Service.Common.csproj",
    r"C:\Projects\transvirtual-web-v1\TransVirtual.Service.Host\TransVirtual.Service.Host.csproj",
    r"C:\Projects\transvirtual-web-v1\TransVirtual.Service.Manager\TransVirtual.Service.Manager.csproj",
    r"C:\Projects\transvirtual-web-v1\TransVirtual.Services.Tests\TransVirtual.Services.Tests.csproj",
    r"C:\Projects\transvirtual-web-v1\TransVirtual.Tcp\TransVirtual.Tcp.csproj",
    r"C:\Projects\transvirtual-web-v1\TransVirtual.Web.Common\TransVirtual.Web.Common.csproj",
    r"C:\Projects\transvirtual-web-v1\TransVirtual.Web.Controllers\TransVirtual.Web.Controllers.csproj",
    r"C:\Projects\transvirtual-web-v1\TransVirtual.Web.Models\TransVirtual.Web.Models.csproj",
    r"C:\Projects\transvirtual-web-v1\TransVirtual.Web.Tests\TransVirtual.Web.Tests.csproj",
]


def extract_packages(csproj_path):
    packages = []

    try:
        tree = ET.parse(csproj_path)
        root = tree.getroot()

        for elem in root.iter():
            if "PackageReference" in elem.tag:
                name = elem.attrib.get("Include")
                version = elem.attrib.get("Version")

                # Handle <Version> inside node
                if version is None:
                    for child in elem:
                        if "Version" in child.tag:
                            version = child.text

                if name and version:
                    packages.append((name, version))

    except Exception as e:
        print(f"Error reading {csproj_path}: {e}")

    return packages


def find_version_mismatches(csproj_files):
    package_map = defaultdict(lambda: defaultdict(list))

    for proj in csproj_files:
        packages = extract_packages(proj)

        for name, version in packages:
            package_map[name][version].append(os.path.basename(proj))

    mismatches = {}

    for pkg, versions in package_map.items():
        if len(versions) > 1:
            mismatches[pkg] = versions

    return mismatches


def print_report(mismatches):
    if not mismatches:
        print("✅ No version mismatches found.")
        return

    print("\n❌ Package Version Mismatches Found:\n")

    for pkg, versions in sorted(mismatches.items()):
        print(f"Package: {pkg}")

        for version, projects in versions.items():
            print(f"  Version: {version}")
            for proj in projects:
                print(f"    - {proj}")

        print("-" * 50)


if __name__ == "__main__":
    mismatches = find_version_mismatches(csproj_files)
    print_report(mismatches)