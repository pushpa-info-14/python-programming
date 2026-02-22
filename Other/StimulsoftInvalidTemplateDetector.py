import os
import re

# ---- CONFIG ----
ROOT_FOLDER = r"C:\TransVirtual\Filesystem\FileDatabase\ReportTemplate"

# ---- PATTERNS ----

# Match <SqlCommand> blocks
sql_command_pattern = re.compile(
    r"<SqlCommand>(.*?)</SqlCommand>",
    re.IGNORECASE | re.DOTALL
)

# Match { ... } expressions inside SQL
expression_pattern = re.compile(
    r"\{(.*?)}",
    re.DOTALL
)

# Detect @Param.ToQueryString() inside expressions
to_query_pattern = re.compile(
    r'@\w+\.ToQueryString\s*\(',
    re.IGNORECASE
)

# Detect any @Variable inside expressions
at_variable_pattern = re.compile(
    r'(?<!@)@\w+',
    re.IGNORECASE
)


def scan_file(filepath):
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    issues = []

    # Extract SQL blocks
    for sql_block in sql_command_pattern.findall(content):

        # Extract { ... } expressions
        for expr in expression_pattern.findall(sql_block):

            if to_query_pattern.search(expr):
                issues.append("Found @Param.ToQueryString() inside {}")

            if at_variable_pattern.search(expr):
                issues.append("Found @Variable inside {}")

    return issues


def scan_directory(root):
    issues_found = False

    for root_dir, _, files in os.walk(root):
        for file in files:
            if file.lower().endswith(".mrt"):
                full_path = os.path.join(root_dir, file)
                matches = scan_file(full_path)

                if matches:
                    issues_found = True
                    print("\n⚠️ Invalid Template Found In:", full_path)
                    for issue in set(matches):
                        print("   →", issue)

    if not issues_found:
        print("✅ No invalid templates found.")


if __name__ == "__main__":
    scan_directory(ROOT_FOLDER)