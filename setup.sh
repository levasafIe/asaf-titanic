# Bash script
# To run it:
#
# $ source setup.sh

echo "Installing miniforge3..."
pyenv install miniforge3

export PYENV_VERSION=miniforge3

echo "Creating environment..."
conda create -n titanic39 python=3.9 --yes

# NOTE: Because of how conda activate works,
# this is difficult to make work inside a script,
# conda activate titanic39
# pip install -e .[dev]
echo "Now run 'conda activate titanic39' from the outside"
