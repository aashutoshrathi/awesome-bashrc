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
    - [git_status alias](#git-status)
    - [git diff for JS Devs](#git-diff-for-js-devs)
    - [Upload your package to PyPi.org](#upload-your-package-to-pypiorg)
    - [apt-get update](#apt-get-update)
    - [open](#open)
    - [ll](#ll)
    - [git branch](#git-branch)
    - [git.io alias](#gitio-alias)
    - [tree alias](#tree-alias)
    - [Fast upwards navigation](#fast-upwards-navigation)
    - [Download music from youtube video](#download-music-from-youtube-video)
    - [Get saved WiFi keys](#get-saved-wifi-keys)
    - [Take Screenshot of connected ADB Device](#take-screenshot-of-connected-adb-device)
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

<a id="ll"></a>

#### ll


```sh
alias ll='ls -laht'
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

#### Fast upwards navigation

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

---

## License

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

---

File Templates taken from [awesome-no-login-web-apps](https://github.com/aviaryan/awesome-no-login-web-apps)
<div>Icons made by <a href="http://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>
