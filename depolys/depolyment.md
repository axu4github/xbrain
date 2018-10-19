## 1. 升级python

```bash
# 检查现有python版本
> python -V
Python 2.6.6
```

### 1.1 安装Python3系统依赖

```bash
> yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
[...]
Installed:
  bzip2-devel.x86_64 0:1.0.5-7.el6_0                          ncurses-devel.x86_64 0:5.7-3.20090208.el6         
  openssl-devel.x86_64 0:1.0.1e-15.el6                        readline-devel.x86_64 0:6.0-4.el6                 
  sqlite-devel.x86_64 0:3.6.20-1.el6                          tk-devel.x86_64 1:8.5.7-5.el6                     
  xz-devel.x86_64 0:4.999.9-0.3.beta.20091007git.el6          zlib-devel.x86_64 0:1.2.3-29.el6                  

Dependency Installed:
  fontconfig-devel.x86_64 0:2.8.0-3.el6                 freetype-devel.x86_64 0:2.3.11-14.el6_3.1                
  keyutils-libs-devel.x86_64 0:1.4-4.el6                krb5-devel.x86_64 0:1.10.3-10.el6_4.6                    
  libX11-devel.x86_64 0:1.5.0-4.el6                     libXau-devel.x86_64 0:1.0.6-4.el6                        
  libXft-devel.x86_64 0:2.3.1-2.el6                     libXrender-devel.x86_64 0:0.9.7-2.el6                    
  libcom_err-devel.x86_64 0:1.41.12-18.el6              libselinux-devel.x86_64 0:2.0.94-5.3.el6_4.1             
  libsepol-devel.x86_64 0:2.0.41-4.el6                  libxcb-devel.x86_64 0:1.8.1-1.el6                        
  tcl.x86_64 1:8.5.7-6.el6                              tcl-devel.x86_64 1:8.5.7-6.el6                           
  tk.x86_64 1:8.5.7-5.el6                               xorg-x11-proto-devel.noarch 0:7.6-25.el6                 

Complete!
```

### 1.2 创建安装目录

```bash
> mkdir -p /usr/local/python3
> ll -d /usr/local/python3/
drwxr-xr-x 2 root root 4096 Oct 16 16:33 /usr/local/python3/
```

### 1.3 编译安装

```bash
# 将安装包拷贝至opt目录下
> mv Python-3.6.6.tgz /opt/

# 检查
> ls /opt/Python-3.6.6.tgz

# 切换目录
> cd /opt/

# 解压安装包
> tar -zxvf Python-3.6.6.tgz

# 检查
> ll Python-3.6.6
total 1044
-rw-r--r--  1 ftpuser ccicall  13335 Jun 27 07:39 aclocal.m4
-rwxr-xr-x  1 ftpuser ccicall  44259 Jun 27 07:39 config.guess
-rwxr-xr-x  1 ftpuser ccicall  36515 Jun 27 07:39 config.sub
-rwxr-xr-x  1 ftpuser ccicall 492104 Jun 27 07:39 configure
-rw-r--r--  1 ftpuser ccicall 164278 Jun 27 07:39 configure.ac
drwxr-xr-x 18 ftpuser ccicall   4096 Jun 27 13:47 Doc
drwxr-xr-x  2 ftpuser ccicall   4096 Jun 27 07:39 Grammar
drwxr-xr-x  2 ftpuser ccicall   4096 Jun 27 07:39 Include
-rwxr-xr-x  1 ftpuser ccicall   7122 Jun 27 07:39 install-sh
drwxr-xr-x 33 ftpuser ccicall   4096 Jun 27 07:39 Lib
-rw-r--r--  1 ftpuser ccicall  12763 Jun 27 07:39 LICENSE
drwxr-xr-x  8 ftpuser ccicall   4096 Jun 27 07:39 Mac
-rw-r--r--  1 ftpuser ccicall  61317 Jun 27 07:39 Makefile.pre.in
drwxr-xr-x  2 ftpuser ccicall   4096 Jun 27 13:47 Misc
drwxr-xr-x 13 ftpuser ccicall   4096 Jun 27 07:39 Modules
drwxr-xr-x  4 ftpuser ccicall   4096 Jun 27 07:39 Objects
drwxr-xr-x  2 ftpuser ccicall   4096 Jun 27 07:39 Parser
drwxr-xr-x  6 ftpuser ccicall   4096 Jun 27 07:39 PC
drwxr-xr-x  2 ftpuser ccicall   4096 Jun 27 07:39 PCbuild
drwxr-xr-x  2 ftpuser ccicall   4096 Jun 27 07:39 Programs
-rw-r--r--  1 ftpuser ccicall  42152 Jun 27 07:39 pyconfig.h.in
drwxr-xr-x  3 ftpuser ccicall   4096 Jun 27 07:39 Python
-rw-r--r--  1 ftpuser ccicall   9720 Jun 27 07:39 README.rst
-rw-r--r--  1 ftpuser ccicall 104570 Jun 27 07:39 setup.py
drwxr-xr-x 23 ftpuser ccicall   4096 Jun 27 07:39 Tools

# 切换目录
> cd /opt/Python-3.6.6

# 执行安装配置
> ./configure --prefix=/usr/local/python3
configure: creating ./config.status
config.status: creating Makefile.pre
config.status: creating Modules/Setup.config
config.status: creating Misc/python.pc
config.status: creating Misc/python-config.sh
config.status: creating Modules/ld_so_aix
config.status: creating pyconfig.h
creating Modules/Setup
creating Modules/Setup.local
creating Makefile


If you want a release build with all stable optimizations active (PGO, etc),
please run ./configure --enable-optimizations

# 编译安装
> make && make install
[...]
Collecting setuptools
Collecting pip
Installing collected packages: setuptools, pip
Successfully installed pip-10.0.1 setuptools-39.0.1
```

### 1.4 创建软连接

```bash
> ln -s /usr/local/python3/bin/python3 /usr/bin/python3
> ll /usr/bin/python3
lrwxrwxrwx 1 root root 30 Oct 16 16:40 /usr/bin/python3 -> /usr/local/python3/bin/python3
```

### 1.5 添加到PATH中

将 **如下内容** 写入到 `~/.bash_profile` **最后一行**

```bash
export PYTHON_HOME="/usr/local/python3"
export PATH=${PATH}:${PYTHON_HOME}/bin
```

**使得配置生效**

```bash
source ~/.bash_profile
```

### 1.6 检查

```bash
> python3 -V
Python 3.6.6

> pip3 -V
pip 10.0.1 from /usr/local/python3/lib/python3.6/site-packages/pip (python 3.6)
```

## 2. 创建python虚拟环境

### 2.1 安装virtualenv

```bash
# 切换目录
> cd /opt/xbrain/depolys

# 解压文件
> tar -zxvf virtualenv-16.0.0.tar.gz 
[...]

# 进入安装目录
> cd virtualenv-16.0.0
> ll
total 156
-rw-r--r-- 1 ftpuser games  1224 May 17 07:36 AUTHORS.txt
drwxr-xr-x 2 ftpuser games  4096 May 17 07:36 bin
drwxr-xr-x 2 ftpuser games  4096 May 17 07:36 docs
-rw-r--r-- 1 ftpuser games  1180 May 17 07:36 LICENSE.txt
-rw-r--r-- 1 ftpuser games   345 May 17 07:36 MANIFEST.in
-rw-r--r-- 1 ftpuser games  3240 May 17 07:36 PKG-INFO
-rw-r--r-- 1 ftpuser games  1135 May 17 07:36 README.rst
drwxr-xr-x 2 ftpuser games  4096 May 17 07:36 scripts
-rw-r--r-- 1 ftpuser games    67 May 17 07:36 setup.cfg
-rw-r--r-- 1 ftpuser games  4047 May 17 07:36 setup.py
drwxr-xr-x 2 ftpuser games  4096 May 17 07:36 tests
drwxr-xr-x 2 ftpuser games  4096 May 17 07:36 virtualenv.egg-info
drwxr-xr-x 2 ftpuser games  4096 May 17 07:36 virtualenv_embedded
-rwxr-xr-x 1 ftpuser games 99548 May 17 07:36 virtualenv.py
drwxr-xr-x 2 ftpuser games  4096 May 17 07:36 virtualenv_support

# 执行安装命令
> python3 setup.py install
[...] 
Installing virtualenv script to /usr/local/python3/bin

Installed /usr/local/python3/lib/python3.6/site-packages/virtualenv-16.0.0-py3.6.egg
Processing dependencies for virtualenv==16.0.0
Finished processing dependencies for virtualenv==16.0.0

# 检查安装版本
> virtualenv --version
16.0.0
```

### 2.2 创建虚拟化环境

```bash
# 创建虚拟化环境目录
> mkdir ~/.venvs

# 检查
> ll -d ~/.venvs/
drwxr-xr-x 2 root root 4096 Oct 17 11:13 /root/.venvs/

# 创建项目虚拟化环境目录
> mkdir ~/.venvs/xbrain

# 检查
> ll -d ~/.venvs/xbrain/
drwxr-xr-x 2 root root 4096 Oct 17 11:14 /root/.venvs/xbrain/

# 创建虚拟化环境
> virtualenv -p /usr/local/python3/bin/python3 ~/.venvs/xbrain/
Running virtualenv with interpreter /usr/local/python3/bin/python3
Using base prefix '/usr/local/python3'
New python executable in /root/.venvs/xbrain/bin/python3
Also creating executable in /root/.venvs/xbrain/bin/python
Installing setuptools, pip, wheel...done.

# 检查
> source ~/.venvs/xbrain/bin/activate
(xbrain) > python -V
Python 3.6.6

# 退出虚拟化环境
(xbrain) > deactivate
> python -V
Python 2.6.6
```

## 3. 安装项目依赖组件

```bash
# 进入虚拟化环境
> source ~/.venvs/xbrain/bin/activate

# 检查
(xbrain) > python -V
Python 3.6.6

# 更新组件版本
(xbrain) > cd /opt/xbrain
(xbrain) > pip install -f packages/ -r requirements.txt
[...]
```

## 4. 启动项目

```bash
# 删除缓存
(xbrain) > rm -rf /opt/xbrain/tests/__pycache__

# 运行测试
(xbrain) > sbin/run_tests.sh
============================================== test session starts ==============================================
platform linux -- Python 3.6.6, pytest-3.8.1, py-1.6.0, pluggy-0.7.1 -- /root/.venvs/xbrain/bin/python
cachedir: .pytest_cache
rootdir: /opt/xbrain, inifile: setup.cfg
collected 17 items                                                                                              

tests/test_env.py::test_version PASSED                                                                    [  5%]
tests/test_factory.py::test_config PASSED                                                                 [ 11%]
tests/test_participles.py::TestJiebaParticiple::test_jieba_participle_perform_segment_empty PASSED        [ 17%]
tests/test_participles.py::TestJiebaParticiple::test_jieba_participle_perform_segment PASSED              [ 23%]
tests/test_participles.py::TestJiebaParticiple::test_jieba_participle_perform_segment_business_vocabs PASSED [ 29%]
tests/test_participles.py::TestJiebaParticiple::test_jieba_participle_perform_segment_stopwords_vocabs PASSED [ 35%]
tests/test_participles.py::TestJiebaParticiple::test_jieba_participle_best_practices PASSED               [ 41%]
tests/test_participles.py::TestJiebaParticiple::test_jieba_participle_corpus_file PASSED                  [ 47%]
tests/test_participles.py::TestJiebaParticiple::test_jieba_participle_corpus_dir PASSED                   [ 52%]
tests/test_similarity.py::TestWord2VectorSimilarity::test_most_similar PASSED                             [ 58%]
tests/test_similarity.py::TestWord2VectorSimilarityApi::test_similarity PASSED                            [ 64%]
tests/test_word2vectors.py::TestGensimWord2Vector::test_train_model_is_not_segment PASSED                 [ 70%]
tests/test_word2vectors.py::TestGensimWord2Vector::test_train_model_is_segment PASSED                     [ 76%]
tests/test_word2vectors.py::TestGensimWord2Vector::test_train_model_segment_business_word_dics PASSED     [ 82%]
tests/test_word2vectors.py::TestGensimWord2Vector::test_train_model_segment_stop_word_dics PASSED         [ 88%]
tests/test_word2vectors.py::TestGensimWord2Vector::test_train_model_save_model PASSED                     [ 94%]
tests/test_word2vectors.py::TestGensimWord2Vector::test_load_model PASSED                                 [100%]

==================================== 17 passed, 13 warnings in 2.66 seconds =====================================

# 启动服务
(xbrain) > nohup sbin/run_server.sh &
```



