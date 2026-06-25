# XRF Geochemistry Notebook for the Anillo Obsidian Source (Arequipa, Peru)
Click "Launch Binder" to run this notebook in the browser.

[![Binder](http://mybinder.org/badge_logo.svg)](https://2i2c.mybinder.org/v2/gh/arf-berkeley/obsidian-source-anillo.git/HEAD?urlpath=%2Fdoc%2Ftree%2Fnotebooks%2Fobsidian-geochem.ipynb)  
Wait for 10+ seconds for launch.

## Notes
This notebook is intended to provide an analytical notebook for exploring Anillo Obsidian geochemistry and it can be repurposed for use with other geochemical analysis datasets.
Proceed through the Jupyter Notebook by clicking in the first cell then press Shift-Return to advance through the notebook.
The map and the plots are interactive.

The notebook and accompanying data are archived in eScholarship at

[XRF Analysis of samples from the Anillo Obsidian Source near Cotahuasi, Arequipa, Peru](https://escholarship.org/uc/item/6vb1790z)

https://escholarship.org/uc/item/6vb1790z

If you'd like to run this Jupyter Notebook locally:  
```bash
git clone https://github.com/arf-berkeley/obsidian-source-anillo.git
cd obsidian-source-anillo
conda env create -f .binder/environment.yml
conda activate obsidian-geochem
jupyter notebook notebooks/obsidian-geochem.ipynb