# Bulk Collage Maker (OpenCV)

A small Python utility that builds a single **collage from a folder of images** using **OpenCV** and **NumPy**, sized to fit your screen. It automatically works out the best grid, resizes every image to fit, stacks them, and displays the finished collage in an OpenCV window.

---

## How It Works

1. **Detects your screen resolution** using Tkinter (`winfo_screenwidth` / `winfo_screenheight`), so the collage is sized to your display.
2. **Chooses the grid** — finds the largest divisor between 2 and 9 that divides the number of images evenly, giving the number of rows/columns that packs the images cleanly. (If the count doesn't divide neatly, it retries with `count + 1`.)
3. **Computes per‑image dimensions** by dividing the screen width/height by that grid factor (memoised with `functools.lru_cache`).
4. **Resizes** every image to those dimensions with `cv2.resize`.
5. **Stacks** images horizontally into rows (`np.hstack`) once a row is full, then stacks the rows vertically (`np.vstack`) into the final collage.
6. **Displays** the result in an OpenCV window (`cv2.imshow`); press any key to close.

---

## Tech Stack

| Component | Purpose |
|-----------|---------|
| Python 3 | Runtime |
| OpenCV (`opencv-contrib-python` 4.10) | Image read/resize/stack/display |
| NumPy 2.0 | Array stacking (`hstack` / `vstack`) |
| Tkinter | Screen‑resolution detection |

---

## Project Structure

```
opencv-collage-maker/
├── main.py            # The collage script (entry point)
├── requirements.txt   # numpy, opencv-contrib-python, tk
└── README.md
```

---

## Getting Started

### Prerequisites

- **Python 3.9+** (with Tkinter available — bundled with most Python installs; on some Linux distros install `python3-tk`)

### Installation

```bash
git clone https://github.com/alexander01202/opencv-collage-maker.git
cd opencv-collage-maker

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate         # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Usage

1. Create an `images/` folder in the project root and drop your pictures into it:

   ```bash
   mkdir images
   # add .jpg / .png files to ./images
   ```

2. Run the script:

   ```bash
   python main.py
   ```

3. The collage opens in a window. Press any key to close it.

---

## Notes & Tips

- **Image count matters.** The grid logic looks for a divisor between 2 and 9, so counts with a clean factor (e.g. 9, 12, 16, 20) produce the tidiest grids. Awkward counts (like primes) fall back to `count + 1`, and any remainder images that don't complete a final row are not stacked — add or remove an image if the bottom row looks off.
- The collage is sized to your **screen resolution**, so very large image sets are scaled down substantially.
- Only files directly inside `images/` are read; make sure the folder contains images OpenCV can decode.

Possible enhancements: save the collage to disk (`cv2.imwrite`) instead of only displaying it, support configurable grid sizes, and skip/validate non‑image files.

---

## License

No license file is included. Add one (e.g. MIT) if you intend others to reuse the code.
