#!/usr/bin/env python3
"""Export the standalone HTML deck to a pixel-faithful PDF.

Chrome's native print-to-pdf reflows the page under print media. That can clip
slides whose screen layout intentionally uses viewport sizing. This exporter
captures each slide at 1280x720 and combines the screenshots into a PDF, so the
PDF matches the browser presentation frame-by-frame.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import tempfile
import time
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parent
DEFAULT_CHROME = Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")


def find_chrome() -> str:
    candidates = [
        DEFAULT_CHROME,
        shutil.which("google-chrome"),
        shutil.which("chromium"),
        shutil.which("chromium-browser"),
    ]
    for candidate in candidates:
        if candidate and Path(candidate).exists():
            return str(candidate)
    raise SystemExit("Chrome executable was not found.")


def slide_ids(html: str) -> list[str]:
    ids = re.findall(r'<section class="[^"]*\bslide\b[^"]*" id="(slide-\d{2})"', html)
    if not ids:
        raise SystemExit("No slide sections found in index.html.")
    return ids


def capture_slide(chrome: str, html_path: Path, slide_id: str, output: Path, timeout: int) -> None:
    profile_dir = output.parent / f"profile-{slide_id}"
    url = f"{html_path.resolve().as_uri()}?export=pdf#{slide_id}"
    cmd = [
        chrome,
        "--headless=new",
        "--disable-gpu",
        "--disable-background-networking",
        "--disable-extensions",
        "--no-first-run",
        "--no-default-browser-check",
        "--hide-scrollbars",
        "--run-all-compositor-stages-before-draw",
        "--force-device-scale-factor=1",
        "--virtual-time-budget=2600",
        "--window-size=1280,720",
        f"--user-data-dir={profile_dir}",
        f"--screenshot={output}",
        url,
    ]
    process = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    deadline = time.monotonic() + timeout
    try:
        while time.monotonic() < deadline:
            if output.exists() and output.stat().st_size > 0:
                return
            if process.poll() is not None:
                break
            time.sleep(0.25)
        if output.exists() and output.stat().st_size > 0:
            return
        raise TimeoutError(f"Screenshot was not created for {slide_id} within {timeout}s.")
    finally:
        if process.poll() is None:
            process.terminate()
            try:
                process.wait(timeout=2)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait(timeout=2)


def images_to_pdf(image_paths: list[Path], output: Path) -> None:
    images = [Image.open(path).convert("RGB") for path in image_paths]
    first, rest = images[0], images[1:]
    first.save(output, "PDF", resolution=96.0, save_all=True, append_images=rest)
    for image in images:
        image.close()


def main() -> int:
    parser = argparse.ArgumentParser(description="Export presentation_html/index.html to PDF.")
    parser.add_argument("--input", type=Path, default=ROOT / "index.html")
    parser.add_argument("--output", type=Path, default=ROOT / "index.pdf")
    parser.add_argument("--chrome", default=find_chrome())
    parser.add_argument("--timeout", type=int, default=120)
    parser.add_argument("--keep-screenshots", action="store_true")
    args = parser.parse_args()

    html = args.input.read_text(encoding="utf-8")
    ids = slide_ids(html)

    temp_dir = Path(tempfile.mkdtemp(prefix="data-yanolja-slides-"))
    image_paths: list[Path] = []
    try:
        for index, slide_id in enumerate(ids, start=1):
            output = temp_dir / f"{index:02d}-{slide_id}.png"
            capture_slide(args.chrome, args.input, slide_id, output, args.timeout)
            image_paths.append(output)
            print(f"captured {slide_id}")

        args.output.parent.mkdir(parents=True, exist_ok=True)
        images_to_pdf(image_paths, args.output)
        print(f"wrote {args.output} ({len(image_paths)} pages)")
    finally:
        if args.keep_screenshots:
            print(f"screenshots kept at {temp_dir}")
        else:
            shutil.rmtree(temp_dir, ignore_errors=True)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
