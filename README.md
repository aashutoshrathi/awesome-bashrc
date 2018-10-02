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

* [C/C++ Compile and Run](#c-cpp)
* [git diff for JS Devs](#gd-js)
* [Upload package to PyPi.org](#py-up)
* [apt-get update](#apt-upd)

<a id="c-cpp"></a>

#### C/C++ compile and run

```sh
cpp() {
    echo "Compilig file..."
    g++ -o "$1" "$1.cpp"
    echo "Complied! Enter input:D"
    ./"$1"
}
# cpp filename

c() {
    echo "Compilig file..."
    gcc -o "$1" "$1.c"
    echo "Complied! Enter input:D"
    ./"$1"
}
# c filename

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

<a id="py-up"></a>

#### Upload your package to PyPi.org

This generates the repsective dist files and uploads them to PyPi.org by asking your credentials at the end.

```sh
alias pyup="python setup.py sdist bdist_wheel && twine upload dist/*"
```

<a id="apt-upd"></a>

#### apt-get update

```sh
alias update='sudo apt-get update'
```
---

## License

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

---

File Templates taken from [awesome-no-login-web-apps](https://github.com/aviaryan/awesome-no-login-web-apps)
<div>Icons made by <a href="http://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>
