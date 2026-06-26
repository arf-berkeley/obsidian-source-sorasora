import json
from pathlib import Path

path = Path('obsidian-geochem.ipynb')
text = path.read_text(encoding='utf-8', errors='replace')
nb = json.loads(text)

# Fix configuration constants cell if needed
for cell in nb['cells']:
    if cell.get('cell_type') == 'code' and any('SRC_CHEM_FILE' in line for line in cell.get('source', [])):
        cell['source'] = [
            '# Configuration\n',
            '# Optional: Load tables from Google Sheets when USE_GOOGLE_SHEETS = True\n',
            'USE_GOOGLE_SHEETS = False  # Toggle between Google Sheets and local CSV\n',
            '\n',
            '# Local CSV file names in ../data\n',
            'SRC_CHEM_FILE = "South_Am_ObsSrcs_Chem_15-25Lat_only.csv"\n',
            'SRC_COORD_FILE = "South_Am_ObsSrcs_Locs_15-25Lat_only.csv"\n',
            'STUDY_FILE = "study_samples.csv"\n',
            '\n',
            '# SHEET_ID = unique ID from Drive URL between the two slashes after "spreadsheets/d/"\n',
            'SHEET_ID = "1R4PlMACBn0l8ZguwtYDlZLnbvORzH5CHhKGFBezjSvk"\n'
        ]
        break

# Fix the actual malformed dataset loading cell
for cell in nb['cells']:
    if cell.get('cell_type') == 'code' and 'read_csv_with_encodings' in ''.join(cell.get('source', [])):
        cell['source'] = [
            '# Load data from Google Sheets or local CSV\n',
            'DATA_DIR = Path("../data") # Directory for local CSV files\n',
            '\n',
            'def read_csv_with_encodings(path):\n',
            '    for encoding in ("utf-8", "latin1", "cp1252"):\n',
            '        try:\n',
            '            return pd.read_csv(path, encoding=encoding)\n',
            '        except UnicodeDecodeError:\n',
            '            continue\n',
            '    # Fallback if the file still fails with standard text encodings\n',
            '    return pd.read_csv(path, encoding="latin1")\n',
            '\n',
            'def get_df(source, sheet_name=None):\n',
            '    """\n',
            '    Load dataframe from Google Sheets or local CSV.\n',
            '    \n',
            '    Parameters\n',
            '    ----------\n',
            '    source : str\n',
            '        Sheet ID (if USE_GOOGLE_SHEETS=True) or CSV filename\n',
            '    sheet_name : str, optional\n',
            '        Required when USE_GOOGLE_SHEETS=True\n',
            '    """\n',
            '    if USE_GOOGLE_SHEETS:\n',
            '        if sheet_name is None:\n',
            '            raise ValueError("sheet_name required when USE_GOOGLE_SHEETS=True")\n',
            '        url = (\n',
            '            f"https://docs.google.com/spreadsheets/d/{source}/gviz/tq"\n',
            '            f"?tqx=out:csv&sheet={sheet_name}"\n',
            '        )\n',
            '        return pd.read_csv(url)\n',
            '    else:\n',
            '        path = DATA_DIR / source\n',
            '        if not path.exists():\n',
            '            raise FileNotFoundError(f"Missing local file: {path.resolve()}")\n',
            '        return read_csv_with_encodings(path)\n',
            '\n',
            '# Load datasets\n',
            'if USE_GOOGLE_SHEETS:\n',
            '    srcs = get_df(SHEET_ID, "KRA21_sources")\n',
            '    srcs_locs = get_df(SHEET_ID, "source_coords")\n',
            '    study = get_df(SHEET_ID, "samples")\n',
            'else:\n',
            '    srcs = get_df(SRC_CHEM_FILE)\n',
            '    srcs_locs = get_df(SRC_COORD_FILE)\n',
            '    study = get_df(STUDY_FILE)\n',
            '\n',
            '# Normalize location fields for the Sora Sora dataset\n',
            'rename_map = {\n',
            '    "Chem_Group": "Group",\n',
            '    "Latitude": "Lat",\n',
            '    "Longitude": "Long",\n',
            '    "Source": "Name"\n',
            '}\n',
            'srcs_locs = srcs_locs.rename(columns=rename_map)\n',
            'if "Name" not in srcs_locs.columns and "Group" in srcs_locs.columns:\n',
            '    srcs_locs["Name"] = srcs_locs["Group"].astype("string")\n'
        ]
        break

path.write_text(json.dumps(nb, indent=1, ensure_ascii=False), encoding='utf-8')
print('Notebook repaired')
