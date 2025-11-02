mkdir -p out

pip install PyYAML # replace with requirements.txt
python tools/create_sections.py

env --chdir=src -S lualatex -file-line-error -interaction=nonstopmode -synctex=1 -output-format=pdf -output-directory=../out CV.tex

rm out/CV.aux out/CV.log out/CV.out out/CV.synctex.gz