import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def validate_manifest() -> list[str]:
    errors: list[str] = []
    path = ROOT / "project-manifest.json"
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"{path.relative_to(ROOT)}: {exc}"]

    for key in ("schema_version", "project", "capabilities", "requirements", "validation"):
        if key not in manifest:
            errors.append(f"project-manifest.json: missing required key {key!r}")
    return errors


def validate_local_links() -> list[str]:
    errors: list[str] = []
    for document in ROOT.rglob("*.md"):
        if ".git" in document.parts:
            continue
        for target in MARKDOWN_LINK.findall(document.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            clean_target = target.split("#", 1)[0]
            if not clean_target:
                continue
            resolved = (document.parent / clean_target).resolve()
            if not resolved.exists():
                errors.append(
                    f"{document.relative_to(ROOT)}: broken local link {target!r}"
                )
    return errors


def main() -> int:
    errors = validate_manifest() + validate_local_links()
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("Portfolio manifest and local links are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
