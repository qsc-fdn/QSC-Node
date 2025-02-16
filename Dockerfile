FROM ubuntu:20.04

COPY ./QSC-Node /qsc-node

WORKDIR /qsc-node

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    swig3.0 cmake pkg-config git --assume-yes\
    build-essential libboost-random-dev libssl-dev libffi-dev libhwloc-dev  ninja-build libboost-dev\
    python3.8 python3-dev python3-pip python3-setuptools \
    telnet wget\
    && pip3 install -U pip setuptools 
    
#RUN cd /qsc-node/src/qsc/crypto/xmssmt/xmss-reference \
#    && make \
#    && cd .. \
#    && pip3 install Cython \
#    && pip3 install .
RUN pip3 install xmssmt-wrapper

RUN pip3 install -r requirements.txt 
RUN pip3 install . 

RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* 
    #&& sed -i "s/TCP4ServerEndpoint(reactor, 8888, interface='127.0.0.1')/TCP4ServerEndpoint(reactor, 8888)/" /qsc-node/qrl/webwallet.py

#RUN sed -i "s/qsc.generated.qrlbase_pb2/qsc.generated.qscbase_pb2/" /usr/local/lib/python3.8/dist-packages/qsc/services/BaseService.py
#RUN sed -i "s/qsc.generated.qrlbase_pb2_grpc/qsc.generated.qscbase_pb2_grpc/" /usr/local/lib/python3.8/dist-packages/qsc/services/BaseService.py
#COPY ./QSC-Node/src/qsc/core/genesis.yml /usr/local/lib/python3.8/dist-packages/qsc/core/
RUN wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=1TfhaidovwlBSBYirvIw1VXY_O1W7jQAR' -O /usr/local/lib/python3.8/dist-packages/qsc/core/genesis.yml

EXPOSE 8080 8888 9000 19001 19009
