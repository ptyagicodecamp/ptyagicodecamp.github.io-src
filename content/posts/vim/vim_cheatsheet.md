Title: Vim Quick References
Date: 09/07/2022
Authors: ptyagi
Category: DevOps
Tags: devops, cli
Summary: A quick guide to Vim editor commands. I'm using macOS Terminal to run vim editor.



This article is a quick getting started guide to Vim editor commands. Vim editor is an improved version of classic `Vi` editor, hence named 'Vi Improved' or `Vim` in short.

__*Note*__: I'm using macOS Terminal to run vim editor.

## Installing Vim Editor (macOS)

You can download Vim editor on macOS using Homebrew package manager.

```
brew install vim
```

Verify the installation of Vim editor by checking its version as below:

```
vim --version
```

The above command will print the current version of Vim editor as below:

```
% vim --version
VIM - Vi IMproved 8.2 (2019 Dec 12, compiled Nov 13 2021 05:05:08)
macOS version - arm64
```

## Opening Vim editor

You can start opening the editor by using `vim` followed by the file name as below:

```
vim test_file
```
The above command will open the `test_file` in vim editor. Press `i` to change to insert mode to start writing into file.

## Modes of Vim

There are mainly three modes in Vim editor:

1. **Normal mode:** This is the mode `Vim` editor opens in. If you try to type in this mode, you would not be able to. That may leave you in bit confusion on how to edit this file. You would need to change into `Insert` mode discussed next.

2. **Insert Mode:** In order to write/edit the file, you will need to press `i`. This enables the editing mode for Vim. You will need to hit `escape` key to return back to Normal mode.

3. **Line Mode:** This mode is activated by hitting `escape` key when in Insert mode followed by colon `:`. This is used to perform operation on the file like saving and closing the file or just discarding the edits. 
    - `:w!`: This command is used to save the contents without closing the file.
    - `:wq!`: This command is for saving + closing the file.
    - `:q!`: This command is used for quiting out of file without saving any changes. Be careful using this command, since it will discard any changes to file that you might have made.

# References

1. [Installing Homebrew](https://formulae.brew.sh/formula/vim)


---
## NOTE
This article is in progress.
---

Follow me at [Medium](https://medium.com/@ptyagicodecamp)
Follow me at [twitter](https://twitter.com/ptyagi13)

![TODO]({attach}../../images/flutter/TODO.jpg)
