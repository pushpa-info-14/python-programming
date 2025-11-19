import os
import subprocess
import xml.etree.ElementTree as ElementTree

solution_path = "C:\\Projects\\transvirtual-web-v1\\TransVirtual.Web.sln"

csproj_files = [
    "C:\\Projects\\transvirtual-web-v1\\Actions\\Actions.csproj",
    "C:\\Projects\\transvirtual-web-v1\\ThirdPartyWebServices\\ThirdPartyWebServices.csproj",
    "C:\\Projects\\transvirtual-web-v1\\TransVirtual.AspNet.Owin\\TransVirtual.AspNet.Owin.csproj",
    "C:\\Projects\\transvirtual-web-v1\\TransVirtual.Common\\TransVirtual.Common.csproj",
    "C:\\Projects\\transvirtual-web-v1\\TransVirtual.Common.Legacy\\TransVirtual.Common.Legacy.csproj",
    "C:\\Projects\\transvirtual-web-v1\\TransVirtual.Common.Tests\\TransVirtual.Common.Tests.csproj",
    "C:\\Projects\\transvirtual-web-v1\\TransVirtual.ConsoleTester\\TransVirtual.ConsoleTester.csproj",
    "C:\\Projects\\transvirtual-web-v1\\TransVirtual.Deployment\\TransVirtual.Deployment.csproj",
    "C:\\Projects\\transvirtual-web-v1\\TransVirtual.Infra\\TransVirtual.Infra.csproj",
    "C:\\Projects\\transvirtual-web-v1\\TransVirtual.ServerUtility\\TransVirtual.ServerUtility.csproj",
    "C:\\Projects\\transvirtual-web-v1\\TransVirtual.Service.Commander\\TransVirtual.Service.Commander.csproj",
    "C:\\Projects\\transvirtual-web-v1\\TransVirtual.Service.Common\\TransVirtual.Service.Common.csproj",
    "C:\\Projects\\transvirtual-web-v1\\TransVirtual.Service.Host\\TransVirtual.Service.Host.csproj",
    "C:\\Projects\\transvirtual-web-v1\\TransVirtual.Service.Manager\\TransVirtual.Service.Manager.csproj",
    "C:\\Projects\\transvirtual-web-v1\\TransVirtual.Services.Tests\\TransVirtual.Services.Tests.csproj",
    "C:\\Projects\\transvirtual-web-v1\\TransVirtual.Tcp\\TransVirtual.Tcp.csproj",
    "C:\\Projects\\transvirtual-web-v1\\TransVirtual.Web.Common\\TransVirtual.Web.Common.csproj",
    "C:\\Projects\\transvirtual-web-v1\\TransVirtual.Web.Controllers\\TransVirtual.Web.Controllers.csproj",
    "C:\\Projects\\transvirtual-web-v1\\TransVirtual.Web.Models\\TransVirtual.Web.Models.csproj",
    "C:\\Projects\\transvirtual-web-v1\\TransVirtual.Web.Tests\\TransVirtual.Web.Tests.csproj",
]


def get_nu1605_from_restore(project_or_solution):
    process = subprocess.Popen(
        ["dotnet", "restore", project_or_solution],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
    )

    nu1605 = []
    for line in process.stdout:
        if "error NU1605: Warning As Error:" in line:
            nu1605.append(line.strip())

    process.wait()
    return nu1605


def update_package_version(csproj_path, package_name, new_version):
    if not os.path.exists(csproj_path):
        print(f"[ERROR] File not found: {csproj_path}")
        return

    print(f"[INFO] Processing: {csproj_path}")

    ElementTree.register_namespace('', "http://schemas.microsoft.com/developer/msbuild/2003")

    tree = ElementTree.parse(csproj_path)
    root = tree.getroot()

    changed = False

    for item_group in root.findall("ItemGroup"):
        for pkg in item_group.findall("PackageReference"):
            include = pkg.attrib.get("Include")
            if include and include.lower() == package_name.lower():
                old_version = pkg.attrib.get("Version")
                if old_version != new_version:
                    pkg.set("Version", new_version)
                    changed = True
                    print(f"  → Updated {package_name}: {old_version} → {new_version}")
                else:
                    print(f"  → Already updated {package_name}: {new_version}")
    if changed:
        tree.write(csproj_path, encoding="utf-8", xml_declaration=True)
        print("[SUCCESS] Updated.")
    else:
        print("[WARN] Package not found in this project.")


def main():
    print("\n=== Bulk Package Version Fix ===")

    errors = get_nu1605_from_restore(solution_path)

    print("--- Updating Projects ---")
    for error in errors:
        # print(error)
        splits = error.split(': ')
        s2 = splits[4].split(' ')
        package_name = s2[0]
        new_version = s2[2]
        for csproj in csproj_files:
            update_package_version(csproj, package_name, new_version)

    print("DONE.")


if __name__ == "__main__":
    main()
