mkdir out

/usr/local/bin/python3 scripts/create_sections.py

lualatex -file-line-error -interaction=nonstopmode -synctex=1 -output-format=pdf -output-directory=out CV.tex

rm out/CV.aux out/CV.log out/CV.out out/CV.synctex.gz