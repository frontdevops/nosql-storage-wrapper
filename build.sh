#!/usr/bin/env bash

#python setup.py sdist bdist_wheel
#twine upload --repository-url https://test.pypi.org/legacy/ dist/*
# check-manifest

git pull origin main && git add --all . && git ci -m "Upfix" && tag -a v0.1.3 && git push origin main && git push origin --tags


echo "Delete current dist..."
rm -vrf dist
rm -vrf nosql_storage_wrapper/*.egg-info

python -m build

#python -m twine upload --verbose --repository testpypi dist/*
python -m twine upload --verbose dist/*
