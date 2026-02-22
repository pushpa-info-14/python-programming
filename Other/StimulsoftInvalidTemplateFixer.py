import os
import re
import shutil
from datetime import datetime

# -------- CONFIG --------
ROOT_FOLDER = r"C:\TransVirtual\Filesystem\FileDatabase\ReportTemplate"
CREATE_TIMESTAMPED_BACKUP = True
DRY_RUN = True  # Set True to preview changes only
# ------------------------

sql_block_pattern = re.compile(
    r"(<SqlCommand>)(.*?)(</SqlCommand>)",
    re.IGNORECASE | re.DOTALL
)

# Match { ... } blocks (Stimulsoft expressions)
expression_pattern = re.compile(
    r"\{(.*?)}",
    re.DOTALL
)

# Match @Param.ToQueryString()
to_query_pattern = re.compile(
    r'@(\w+)\.ToQueryString\s*\(\s*\)',
    re.IGNORECASE
)

# Match @Param (ONLY inside {})
at_param_pattern = re.compile(
    r'(?<!@)@(\w+)',
    re.IGNORECASE
)


def backup_file(filepath):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    backup_path = f"{filepath}.{timestamp}.bak"
    shutil.copy2(filepath, backup_path)
    return backup_path


def fix_expression(expr_text):
    changes = 0

    # Remove .ToQueryString()
    def replace_to_query(match):
        nonlocal changes
        changes += 1
        return match.group(1)

    expr_text = to_query_pattern.sub(replace_to_query, expr_text)

    # Remove @ only inside expression
    def replace_at(match):
        nonlocal changes
        changes += 1
        return match.group(1)

    expr_text = at_param_pattern.sub(replace_at, expr_text)

    return expr_text, changes


def fix_sql(sql_text):
    total_changes = 0

    def replace_expression(match):
        nonlocal total_changes
        inner = match.group(1)

        fixed_inner, changes = fix_expression(inner)
        total_changes += changes

        return "{" + fixed_inner + "}"

    updated_sql = expression_pattern.sub(replace_expression, sql_text)

    return updated_sql, total_changes


def process_file(filepath):
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    total_changes = 0

    def replace_sql_block(match):
        nonlocal total_changes
        start_tag, sql_body, end_tag = match.groups()

        fixed_sql, changes = fix_sql(sql_body)
        total_changes += changes

        return f"{start_tag}{fixed_sql}{end_tag}"

    updated_content = sql_block_pattern.sub(replace_sql_block, content)

    if total_changes > 0:
        print(f"\n✔ Fixing: {filepath}")
        print(f"   → Changes: {total_changes}")

        if not DRY_RUN:
            backup_path = backup_file(filepath)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(updated_content)
            print(f"   → Backup: {backup_path}")

    return total_changes


def scan_directory(root):
    files_modified = 0
    total_changes = 0

    for root_dir, _, files in os.walk(root):
        for file in files:
            if file.lower().endswith(".mrt"):
                full_path = os.path.join(root_dir, file)
                changes = process_file(full_path)

                if changes > 0:
                    files_modified += 1
                    total_changes += changes

    print("\n======== SUMMARY ========")
    print(f"Files modified: {files_modified}")
    print(f"Total replacements: {total_changes}")
    print("=========================")


if __name__ == "__main__":
    scan_directory(ROOT_FOLDER)