#!/bin/bash

set -x

args=$1
job=`echo $args | sed -e 's/job.//g' -e 's/_.*//g'`
#service=`echo $args | sed -e 's/.*_service.//g' -e 's/_.*//g'`
service=`echo $args | sed -e 's/.*_service\.//g' -e 's/_.*//g'`
env=`echo $args | sed -e 's/.*_cluster.//g' -e 's/_.*//g'`


py_version="3.6.5"

## 安装pyenv (编译机)
#[[ ! -s "$HOME/.pyenv" ]] && \
#git clone git://github.com/yyuu/pyenv.git $HOME/.pyenv && \
#export PYENV_ROOT="$HOME/.pyenv"  && \
#export PATH="$PYENV_ROOT/bin:$PATH"  && \
#eval "$(pyenv init - $SHELL)"
#
## 设置python版本
#[[ ! `pyenv versions | grep $py_version` ]] && \
#pyenv install $py_version && pyenv local $py_version
#
## 安装virtualenv (编译机)
#export PATH=$HOME/.pyenv/versions/$py_version/bin:$PATH
#pip install virtualenv -i http://pypi.xiaomi.srv/pypi/simple
#pip install nose==1.3.7 -i http://pypi.xiaomi.srv/pypi/simple
#
## 生成应用环境
#rm -rf $service && \
#virtualenv $service
#build_path=`pwd`
#cp pip-req.txt* $service && \
#pushd $service && \
source ~/.bash_profile
/home/work/.pyenv/bin/pyenv local 3.6.5
export PATH=$HOME/.pyenv/versions/$py_version/bin:$PATH
build_path=`pwd`
cd /home/work
echo $build_path
virtualenv $service
cd $service
./bin/python -V

source bin/activate && \

pip install setuptools --upgrade  -i http://pypi.xiaomi.srv/pypi/simple
pip install pip==19.2.3  && \
pip install -r $build_path/requirements.txt -i http://pypi.xiaomi.srv/pypi/simple --trusted-host pypi.xiaomi.srv && \
deactivate && \
#popd

echo $build_path > env_build_path.txt

# 生成release
#git pull

#mkdir -p release/src && \
#cp -r  *  release/src
#cp -r deploy release/
#cp -r $service/* release/

cd $build_path
chmod +x run.sh
mkdir -p release/src  && \
cp -r  *  release/src
cp -r deploy release/
cp -rf /home/work/$service/* release/
exit 0
