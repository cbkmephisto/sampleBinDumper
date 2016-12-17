# sampleBinDumper [![Build Status](https://travis-ci.org/cbkmephisto/sampleBinDumper.svg?branch=master)](https://travis-ci.org/cbkmephisto/sampleBinDumper)
Trivial tool to print out content of a binary MCMC sample file for [BOLT software](http://www.thetasolutionsllc.com/bolt-software.html).

The SBR and SAMP binary formats are described in [BOLT wiki page](http://104.236.183.143/mediawiki/index.php/User_Guide#SBR).

## Compile and Install
#### C++
```
make
```
and Copy/move the executable to somewhere in your PATH environment variable.
#### Python3
Copy/move the executable ```sampleBinDumper.py``` to somewhere in your PATH environment variable. May need adding executable permission in \*nix system
```
chomod +x sampleBinDumper.py
```
