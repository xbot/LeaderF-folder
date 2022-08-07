# LeaderF-folder

This plugin use [LeaderF](https://github.com/Yggdroot/LeaderF) to open a subfolder.

![](image/screencast.gif)

## Requirements

- [LeaderF](https://github.com/Yggdroot/LeaderF)
- [fd](https://github.com/sharkdp/fd)
- [Dirbuf](https://github.com/elihunter173/dirbuf.nvim): Optional, can be changed to other file managers.

## Setup

This plugin takes [Dirbuf](https://github.com/elihunter173/dirbuf.nvim) as the default solution to open the chosen subfolder. You can use the following option to customize it:

```vim
let g:Lf_FolderAcceptSelectionCmd = 'Dirbuf'
```

## Usage

```vim
:LeaderfFolder
```

Press `F1` to get more help

## LICENSE

MIT
