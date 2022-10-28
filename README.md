# cmaker
CLI to generate cmake project

## Usage

`cmaker name_of_the_project` Creates an executable cmake project

`cmaker name_of_the_project -l` Creates a static library cmake project

`cmaker name_of_the_project -s 11` Creates an executable cmake project with C++11 standard

`cmaker name_of_the_project -cv 3.24` Creantes an executable cmake project with cmake version 3.24

### Linux

To install

1. Clone the repository and navigate there.
2. Open your terminal and type `bash ./install.sh`
3. After that open and close the terminal and type `cmaker -h` and see help

In case of error try adding ~/.bin to .bashrc.
Refer to this link https://askubuntu.com/questions/402353/how-to-add-home-username-bin-to-path  

To uninstall

1. Navigate to the cloned repository
2. Open your terminal and type `bash ./uninstall.sh`


