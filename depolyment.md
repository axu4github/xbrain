## 1. 升级Python3

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

将 **如下内容** 写入到 `~/.bash_profile` 最后一行

```bash
export PYTHON_HOME="/usr/local/python3"
export PATH=${PATH}:${PYTHON_HOME}/bin
```

使得配置生效

```bash
source ~/.bash_profile
```

### 1.6 检查

```bash
> python3 -V
Python 3.6.6
```



