### numpy, pandas, matplotlib, seaborn

conda update conda (or conda update --all)

conda create -n {name} python=3.x

conda activate {name}

conda install -c conda-forge opencv matplotlib jupyterlab scikit-image seaborn git

    1	conda deactivate multi
    2	conda create --name multi python=3.7.6
    3	conda activate multi 
    4	pip install ipykernel
    5	python -m ipykernel install --user --name multi --display-name "Python Multi"
    6	conda install -c conda-forge jupyterlab
    7 #conda env create -n multi -f env_project1.yaml
      
    #
    # To activate this environment, u
    #
    #     $ conda activate project1
    #
    # To deactivate an active environment, use
    #
    #     $ conda deactivate
    
    8   conda remove --name project1 --all
    
    # pip install -r requirements.txt
