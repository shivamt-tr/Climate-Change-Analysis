#!/bin/bash

cd code

tic=$SECONDS

jupyter nbconvert --to notebook --execute GHG_Cleaning.ipynb
jupyter nbconvert --to notebook --execute Population_Cleaning.ipynb
jupyter nbconvert --to notebook --execute GHG_Analytics.ipynb
jupyter nbconvert --to notebook --execute Glaciers_sealevel_plastics.ipynb
jupyter nbconvert --to notebook --execute Data_Cleaning_for_Temperature_Change.ipynb
jupyter nbconvert --to notebook --execute Temperature_and_Deforestation.ipynb
jupyter nbconvert --to notebook --execute natural_disaster_analysis.ipynb


toc=$SECONDS

echo "Time to run the full project = $((toc-tic)) seconds."