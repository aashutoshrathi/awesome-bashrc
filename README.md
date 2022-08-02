<p align="center"><img src="https://image.flaticon.com/icons/svg/977/977504.svg" width="150"><p>
<h1 align="center">awesome-bashrc</h1>

<p align="center">
<a href="https://github.com/sindresorhus/awesome">
    <img align="center" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg">
</a>

<a href="/CONTRIBUTING.md">
    <img align="center" src="https://img.shields.io/badge/contributors-needed-yellow.svg">
</a>
<p>
<hr>

🚀 Curated list of awesome bashrc snippets that will make your work easier.

#### Inspiration

Working with bash in daily life, it is very irritating writing the same command multiple times.
To avoid that we write aliases/snippets for bashrc and make our life easier.

This repository will have collection of such aliases. Read [Contribution Guidelines](CONTRIBUTING.md) before contributing.

## Contents

- [Contents](#contents)
    - [C/C++ compile and run](#cc-compile-and-run)
    - [git diff for JS Devs](#git-diff-for-js-devs)
    - [git status](#git-status)
    - [Upload your package to PyPi.org](#upload-your-package-to-pypiorg)
    - [apt-get update](#apt-get-update)
    - [open](#open)
    - [List files](#list-files)
    - [Tally](#tally)
    - [Check free space on disks](#check-free-space-on-disks)
    - [Safe operations with files](#safe-operations-with-files)
    - [git branch](#git-branch)
    - [git.io alias](#gitio-alias)
    - [tree alias](#tree-alias)
    - [Fast upwards navigation (comes with ZSH)](#fast-upwards-navigation-comes-with-zsh)
    - [Download music from youtube video](#download-music-from-youtube-video)
    - [Get saved WiFi keys](#get-saved-wifi-keys)
    - [Take Screenshot of connected ADB Device](#take-screenshot-of-connected-adb-device)
    - [Bootstrap your CF Round](#bootstrap-your-cf-round)
    - [Run Matlab scripts](#run-matlab-scripts)
    - [Convert GIF to WebM](#convert-gif-to-webm)
- [License](#license)

<a id="c-cpp"></a>

#### C/C++ compile and run

```sh
cpp-run() {
    echo "Compiling file..."
    g++ -o "$1" "$1.cpp"
    echo "Compiled! Enter input :D"
    ./"$1"
}
# cpp-run filename

c-run() {
    echo "Compiling file..."
    gcc -o "$1" "$1.c"
    echo "Compiled! Enter input :D"
    ./"$1"
}
# c-run filename

```

<a id="gd-js"></a>

#### git diff for JS Devs

```sh
alias gd="git diff --ignore-all-space 
                    --ignore-space-at-eol 
                    --ignore-space-change 
                    --ignore-blank-lines -- . 
                    ':(exclude)*package-lock.json'"

# Write gd to ignore not important differences.
# Credits: https://www.reddit.com/r/javascript/comments/9i6hl3/alias_for_open_source_js_devs/
```

<a id="git-status"></a>

#### git status

```sh
alias s="git status"

```

<a id="py-up"></a>

#### Upload your package to PyPi.org

This generates the respective dist files and uploads them to PyPi.org by asking your credentials at the end.

```sh
alias pyup="python setup.py sdist bdist_wheel && twine upload dist/*"
```

<a id="apt-upd"></a>

#### apt-get update

```sh
alias update='sudo apt-get update'
```
<a id="open"></a>

#### open

Open any file using its default program (eg. pdfs, torrents, etc).

```sh
alias open="xdg-open"
```

<a id="list-files"></a>

#### List files


```sh
alias ll='ls -laht'
alias l='ls -aC'
```

<a id="tally"></a>

#### Tally

```sh
tally() {
  if [[ $1 == '--help' ]]; then
    echo "Usage: ls | tally";
    return 0;
  fi
  
  sort | uniq -c | sort -n
}
```


<a id="check-free-space-on-disks"></a>

#### Check free space on disks
```sh
alias df='df -h'
```

<a id="safe-operations-with-files"></a>

#### Safe operations with files
```sh
alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'
```

<a id="git-branch"></a>

#### git branch

This will display the current git branch of any repository you're in.

```sh
# Add git branch if its present to PS1
parse_git_branch() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
}

# Pass the function to the color parser of the terminal to colorize the branch name.
if [ "$color_prompt" = yes ]; then
    if [[ ${EUID} == 0 ]] ; then
        PS1='${debian_chroot:+($debian_chroot)}\[\033[01;31m\]\h\[\033[01;34m\] \W $(parse_git_branch)\$\[\033[00m\] '
    else
        PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\] \[\033[01;34m\]\w $(parse_git_branch)\$\[\033[00m\] '
    fi
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h \w \$ '
fi
unset color_prompt force_color_prompt
```

<a id="git-io"></a>

#### git.io alias

Get shortened git.io URLs from a single command

```sh
gurl() {
    curl -i https://git.io -F "url=$1" \
    -F "code=$2"
}

# Usage
# gurl https://github.com/anshumanv anshumanv
```

After these steps, https://git.io/anshumanv will redirect you to https://github.com/anshumanv

<a id="tree-alias"></a>

#### tree alias

Get representation of underlying files and folders as a tree.

```sh
alias tree="find . -print | sed -e 's;[^/]*/;|____;g;s;____|; |;g'"
```

<a id="fastupwardsnavigation"></a>

#### Fast upwards navigation (comes with ZSH)

```sh
alias ..='cd ..'
alias ...='cd ../../../'
alias ....='cd ../../../../'
alias .....='cd ../../../../'
```

<a id="youtube-mp3"></a>

#### Download music from youtube video

You will need mp3-lame library and youtube-dl utility.

```sh
alias youtube-mp3="youtube-dl --extract-audio --audio-format mp3"
# Usage
# youtube-mp3 https://youtube.com/{id}
```

<a id="password-wifi"></a>

#### Get saved WiFi keys

```sh
alias wifikey="sudo grep -r '^psk=' /etc/NetworkManager/system-connections/"
# Usage (requires sudo)
# wifikey
```

<a id="take-screenshot-of-connected-adb-device"></a>

#### Take Screenshot of connected ADB Device

```sh
alias cap="adb shell screencap -p /sdcard/screen.png && \
           adb pull /sdcard/screen.png && \
           adb shell rm /sdcard/screen.png"
# Usage (requires connected device)
# Saves the screenshot with name screen.png
# cap
```

<a id="cf-round"></a>

#### Bootstrap your CF Round

```sh
cf() {
    mkdir "CF#$1" &&\
    cd "CF#$1" &&\
    touch inp.txt &&\
    touch out.txt && \
    curl -L "https://files.aashutosh.dev/cpp.cpp" -o A.cpp
}

# Usage: cf 549
# The above command initialzes, Your CF Round folder and downloads your sample template.
# https://files.aashutosh.dev/cpp.cpp refers to link of your template
```

<a id="run-matlab-scripts"></a>

#### Run Matlab scripts

```sh
matlab-run() {
    matlab -nodesktop -nosplash -r "$1"
}
# matlab-run filename
```

<a id="gif2webm"></a>

#### Convert GIF to WebM

Why?
=> Read [this](https://bit.ly/gif-mp4) (You can save upto 90% on size of media)

```sh
gif2webm() {
    ffmpeg -i $1.gif -c vp9 -b:v 0 -crf 41 $1.webm
}
# gif2webm gif-name-without-format
```

---
#### Python 

Framework used for coming up with aliases for Python: 

* To create / make a directory, `mkdir` is used and to remove a directory `rmdir` is used. Extending this logic of using `mk` and `rm` for aliases.

For example: 
1) `pirm` : pip remove a package 
2) `mkvenv` : To create / make a virtual environment


First defining a custom print function to pretty print alias output. This will help us distinguish between command output and alias output

```bash 

function repeat {
    num="${2:-100}"; printf -- "$1%.0s" $(seq 1 $num);
}

# custom print function for pretty printing aliases/ functions
function print {
    terminalCols=$(tput cols)
    argLen=${#1}
    offset=$(((terminalCols-argLen)/2))

    printf "\n"
    repeat '#' $((offset-1))
    printf " $1 "
    repeat '#' $((offset-1))
    printf "\n"     
}

```

###### Aliases specific to python: 
```bash 
alias 'py'='python'
alias 'pirm'='pip uninstall -y'
alias 'sdist'='rm -rf dist/ ; py setup.py sdist'
alias 'bdist'='rm -rf dist/ ; py setup.py bdist_wheel'

# Pip install 
function pi {
    if [ -z "$1" ]
    then 
        # Looks for setup.py in the current directory and installs the package
        print "Installing from local setup.py file in the current directory"
        pip install .
    else 
        # Installs the package from PyPI 
        print "Fetching from PyPI"
        pip install "$1"
    fi
}

alias 'pii'='pi'
```

##### Python virtual environments 

###### To create a python virtual environment in the current directory:

```bash 
# Create new venv using python3
# If no name is passed will default to .venv
function mkvenv {
    if [ -z "$1" ]
    then
        print "Creating virtualenv: .venv"
        python3 -m venv .venv
        avenv
    else
        print "Creating virtualenv: $1"
        python3 -m venv "$1"
        avenv "$1"
    fi

    print "Upgrading pip"
    pip install pip --upgrade

    print "Installing wheel package"
    pip install wheel
    print "Activated virtualenv"
}

alias 'mkenv'='mkvenv'

```
###### To remove a python virtual environment in the current directory

```bash 
# Remove a virtual env.
# If no name is passed will default to .venv
function rmvenv {
    if [ -z "$1" ]
    then
        print "Removing virtualenv: .venv"
        python3 -m venv .venv
        rm -rf .venv
    else
        print "Removing virtualenv: $1"
        rm -rf "$1"
    fi
}

alias 'rmenv'='rmvenv'
```

###### To activate a virtual environment in the current directory.

Going by the general assumption that python virtual environments are named as: 
* .venv : Local virtual environemnt
* .venv37 : Local virtual environment with Python 3.7
* .venv38 : Local virtual environment with Python 3.8


The below alias uses `fzf` to choose a virtual environment to activate when there are multiple virtual environments in the 
current directory.

```bash

# Activate virtual env
# If no name is passed will default to .venv
function avenv {
    # If no paramerter is passed try to activate .venv first. If .venv doesnt exist try with the next closest one. If both .venv37 and .venv38 exist. It will pick .venv37
    # If parameter is passed, try to activate that one
    if [ -z "$1" ]
    then

        if [ -d ".venv" ] 
        then
            source .venv/bin/activate 
            print "Activated virtualenv: .venv" 

        else   
            # Piping the output of find command to fzf to select a virtual env.
            virtual_env=$(find -maxdepth 2  -type d -name ".venv*"  | fzf)  
            print "Activated virtualenv: $virtual_env" 
            source "$virtual_env"/bin/activate
        fi 

    else
         source "$1"/bin/activate; print "Activated virtualenv: $1" || print "Failed to activate virtualenv: $1"

    fi
}

alias 'aenv'='avenv'
```
###### To deactivate a virtual environment
```bash

# Deactivate virtual env

function dvenv {

    if [ -z "$1" ]
    then
        deactivate || print "Failed to deactivate virtualenv: .venv"
        print "Deactivated virtualenv"
    else
        deactivate "$1" || print "Failed to deactivate virtualenv: $1"
        print "Deactivated virtualenv" 
    fi
}
alias 'denv'='dvenv'

```

##### Anaconda Python 

Utilizes the `mamba` executable wherever possible to improve anaconda command execution times. 

Follows a similar style of aliases as the above set of python aliases. 

Only difference is, aliases are prefixed with `c`.

```bash
#  MAMBA: Currently, only install, create, list, search, run, info and clean are supported through mamba.

#list envs
alias 'clsenv'='mamba env list'
alias 'clsvenv'='clsenv'
```

###### To create a conda environment
```bash 
#create new venv
function cmkvenv {
   mkdir -p /usr/softwares/miniconda3/envs/"$1"
#  mamba create -n "$1" --prefix=/usr/softwares/miniconda3/envs/"$1" python="$2" -y
  conda create  --prefix=/usr/softwares/miniconda3/envs/"$1" python="$2" -y
}
alias 'cmkenv'='cmkvenv'
```

###### To remove a conda environment
```bash 
# remove arbitrary number of conda virtual envs
function crmenv {
  mamba env remove -n "$@"
}

alias 'crmvenv'='crmenv'
```

###### To activate/ deactivate a conda environment
```bash
#activate venv.
#Can't use mamba for activation and deactivation of env
function caenv {
  conda activate "$1"
}

#deactivate venv
alias "cdvenv"="conda deactivate"
alias "cdenv"="cdvenv"
```
###### To add/remove and list conda channel(s)
```bash
#add channels in conda
function caddc {
    if [ -z "$1" ]
    then
        echo "Provide a channel name to add!"
        #exit 1;
    else
        mamba config --add channels "$1"
    fi
}

#list channels in conda
function clsch {
  conda config --show channels
}

# remove a channel
function crmch {
    conda config --remove channels "$1"
}
```

###### To install / remove a conda package 
```bash
#Conda install a package
function ci {
    if [ -z "$2" ]
    then
        /usr/softwares/miniconda3/condabin/mamba install -y "$1"
    else
         /usr/softwares/miniconda3/condabin/mamba install -c "$2" "$1"
    fi
}

#Conda remove a package
alias 'crm'='mamba uninstall -y'
```

## License

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

---

File Templates taken from [awesome-no-login-web-apps](https://github.com/aviaryan/awesome-no-login-web-apps)
<div>Icons made by <a href="http://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>
