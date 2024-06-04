echo [$(date)]: "START"
echo [$(date)]: "Creating conda env with python 3.10"
conda create --prefix ./env python=3.10 -y
#pyenv virtualenv 3.11.3 ./env 
pyenv virtualenv 3.10.5 ./env
echo [$(date)]: "activate env"
source activate ./env
#source myvenv/bin/activate
echo [$(date)]: "intalling dev requirements"
#https://stackoverflow.com/questions/77189121/pip-install-subprocess-to-install-build-dependencies-did-not-run-successfully
pip install --platform -r requirements_dev.txt 
echo [$(date)]: "END"
