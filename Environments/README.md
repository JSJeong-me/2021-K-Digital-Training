### numpy, pandas, matplotlib, seaborn

conda update conda (or conda update --all)

conda create -n {name} python=3.x

conda activate {name}

conda install -c conda-forge opencv matplotlib jupyterlab scikit-image seaborn git

    1	conda deactivate base
    2	conda create --name kosa python=3.7.6
    3	conda activate kosa 
    4	pip install ipykernel
    5	python -m ipykernel install --user --name kosa --display-name "Python KOSA"
    6	conda install -c conda-forge jupyterlab
    7 conda env create -n project1 -f env_project1.yaml
      
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
