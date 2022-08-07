" Definition of 'arguments' can be similar as
" https://github.com/Yggdroot/LeaderF/blob/master/autoload/leaderf/Any.vim#L85-L140
let s:extension = {
      \   "name": "folder",
      \   "help": "navigate folder repos",
      \   "manager_id": "leaderf#Folder#managerId",
      \   "arguments": [
      \   ]
      \ }

" In order that `Leaderf folder` is available
call g:LfRegisterPythonExtension(s:extension.name, s:extension)

command! -bar -nargs=0 LeaderfFolder Leaderf folder

" In order to be listed by :LeaderfSelf
call g:LfRegisterSelf("LeaderfFolder", "navigate folder repos")

if !exists("g:Lf_FolderAcceptSelectionCmd")
    let g:Lf_FolderAcceptSelectionCmd = 'Dirbuf'
endif
