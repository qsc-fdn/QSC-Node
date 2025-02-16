
# in docker container
sed -i "s/name = QSC/name = qsc_node_qscf/" setup.cfg

python3 setup.py bdist_wheel
python3 setup.py sdist
cp dist/qsc_node_qscf-1.0.0.tar.gz ~/.qsc
cp dist/qsc_node_qscf-1.0.0-py3-none-any.whl ~/.qsc

# out of docker container
sudo cp data/qsc_node_qscf-1.0.0-py3-none-any.whl dist/
sudo cp data/qsc_node_qscf-1.0.0.tar.gz dist/
sudo twine upload dist/*