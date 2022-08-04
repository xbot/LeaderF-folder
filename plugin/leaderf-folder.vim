if !exists('g:Lf_Extensions')
    let g:Lf_Extensions = {}
endif

let g:Lf_Extensions.folder = {
            \ 'source': 'leaderf#folder#source',
            \ 'accept': 'leaderf#folder#accept',
            \ 'highlights_def': {
            \ 'Lf_hl_folderScore': '^\d\+\.\d\+',
            \ 'Lf_hl_folderDirectory': '^\d\+\.\d\+\t\zs.*',
            \ },
            \ 'highlights_cmd': [
            \ 'hi link Lf_hl_folderScore Number',
            \ 'hi link Lf_hl_folderDirectory Directory',
            \ ],
            \ }

