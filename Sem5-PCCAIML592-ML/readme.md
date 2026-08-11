For a clean Python environment with NumPy and Pandas:

```bash
# Create a virtual environment in the folder
python -m venv .venv

# Activate it
# macOS/Linux:
source .venv/bin/activate

# Windows:
.venv\Scripts\activate

# Upgrade pip
python -m pip install --upgrade pip

# Install NumPy and pandas
pip install numpy pandas
```

- Have a requirements.txt with `numpy` and `pandas` in it if you want reproducible environments

Then install everything with:

```bash
pip install -r requirements.txt
```

You can check your installed versions with:

```bash
pip show numpy pandas
```

- Use the MSYS2 UCRT64 terminal and pacman commands for downloading of libraries.
- I am importing python libraries from a native UCRT64 package:

```bash MSYS2 UCRT64 terminal
pacman -S mingw-w64-ucrt-x86_64-python-pandas mingw-w64-ucrt-x86_64-python-ipykernel
```

Then to check:

```bash
python -c "import pandas; print(pandas.__version__)"
python -c "import ipykernel; print(ipykernel.__version__)"
```
