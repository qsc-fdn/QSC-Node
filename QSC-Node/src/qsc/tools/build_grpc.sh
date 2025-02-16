#!/usr/bin/env bash
pushd . > /dev/null
cd $( dirname "${BASH_SOURCE[0]}" )
cd ..

python -m grpc_tools.protoc -I=qsc/protos --python_out=qsc/generated --grpc_python_out=qsc/generated qsc/protos/qsc.proto
python -m grpc_tools.protoc -I=qsc/protos/qsc.proto -I=qsc/protos --python_out=qsc/generated --grpc_python_out=qsc/generated qsc/protos/qsclegacy.proto
python -m grpc_tools.protoc -I=qsc/protos --python_out=qsc/generated --grpc_python_out=qsc/generated qsc/protos/qscbase.proto
python -m grpc_tools.protoc -I=qsc/protos --python_out=qsc/generated --grpc_python_out=qsc/generated qsc/protos/qscmining.proto

python -m grpc_tools.protoc -I=qsc/protos --python_out=qsc/generated --grpc_python_out=qsc/generated qsc/protos/qscstateinfo.proto
python -m grpc_tools.protoc -I=qsc/protos --python_out=qsc/generated --grpc_python_out=qsc/generated qsc/protos/qscbase.proto
python -m grpc_tools.protoc -I=qsc/protos --python_out=qsc/generated --grpc_python_out=qsc/generated qsc/protos/qscwallet.proto
python -m grpc_tools.protoc -I=qsc/protos --python_out=qsc/generated --grpc_python_out=qsc/generated qsc/protos/qscdebug.proto

# Patch import problem in generated code
sed -i 's|import qsc_pb2 as qsc__pb2|import qsc.generated.qsc_pb2 as qsc__pb2|g' qsc/generated/qsc_pb2_grpc.py
sed -i 's|import qsc_pb2 as qsc__pb2|import qsc.generated.qsc_pb2 as qsc__pb2|g' qsc/generated/qsclegacy_pb2.py
sed -i 's|import qsc_pb2 as qsc__pb2|import qsc.generated.qsc_pb2 as qsc__pb2|g' qsc/generated/qscmining_pb2.py

sed -i 's|import qsc_pb2 as qsc__pb2|import qsc.generated.qsc_pb2 as qsc__pb2|g' qsc/generated/qscstateinfo_pb2.py
sed -i 's|import qsc_pb2 as qsc__pb2|import qsc.generated.qsc_pb2 as qsc__pb2|g' qsc/generated/qscbase_pb2.py
sed -i 's|import qsc_pb2 as qsc__pb2|import qsc.generated.qsc_pb2 as qsc__pb2|g' qsc/generated/qscwallet_pb2.py
sed -i 's|import qsc_pb2 as qsc__pb2|import qsc.generated.qsc_pb2 as qsc__pb2|g' qsc/generated/qscdebug_pb2.py

sed -i 's|import qsclegacy_pb2 as qsclegacy__pb2|import qsc.generated.qsclegacy_pb2 as qsclegacy__pb2|g' qsc/generated/qsclegacy_pb2_grpc.py
sed -i 's|import qscbase_pb2 as qscbase__pb2|import qsc.generated.qscbase_pb2 as qscbase__pb2|g' qsc/generated/qscbase_pb2_grpc.py
sed -i 's|import qscmining_pb2 as qscmining__pb2|import qsc.generated.qscmining_pb2 as qscmining__pb2|g' qsc/generated/qscmining_pb2_grpc.py

sed -i 's|import qscstateinfo_pb2 as qscstateinfo__pb2|import qsc.generated.qscstateinfo_pb2 as qscstateinfo__pb2|g' qsc/generated/qscstateinfo_pb2_grpc.py
sed -i 's|import qscbase_pb2 as qscbase__pb2|import qsc.generated.qscbase_pb2 as qscbase__pb2|g' qsc/generated/qscbase_pb2_grpc.py
sed -i 's|import qscwallet_pb2 as qscwallet__pb2|import qsc.generated.qscwallet_pb2 as qscwallet__pb2|g' qsc/generated/qscwallet_pb2_grpc.py
sed -i 's|import qscdebug_pb2 as qscdebug__pb2|import qsc.generated.qscdebug_pb2 as qscdebug__pb2|g' qsc/generated/qscdebug_pb2_grpc.py

find qsc/generated -name '*.py'|grep -v migrations|xargs autoflake --in-place

#docker run --rm \
#  -v $(pwd)/docs/proto:/out \
#  -v $(pwd)/qsc/protos:/protos \
#  pseudomuto/protoc-gen-doc --doc_opt=markdown,proto.md
#
#docker run --rm \
#  -v $(pwd)/docs/proto:/out \
#  -v $(pwd)/qsc/protos:/protos \
#  pseudomuto/protoc-gen-doc --doc_opt=html,index.html

popd > /dev/null
