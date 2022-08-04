function! leaderf#folder#source(args) abort "{{{
    return split(system('fd -t directory -I'), '\n')
endfunction "}}}

function! leaderf#folder#accept(line, args) abort "{{{
    let l:path = fnameescape(a:line)

    if exists('g:leaderf#folder#explorer')
        execute g:leaderf#folder#explorer l:path
    elseif exists(':Dirbuf') == 2
        execute 'Dirbuf' l:path
    elseif exists(':Defx') == 2
        execute 'Defx' l:path
    elseif exists(':LeaderfFiler') == 2
        execute 'LeaderfFiler' l:path
    elseif exists(':CocCommand') == 2
        execute 'CocCommand explorer' l:path
    elseif exists(':Explore') == 2
        execute 'Explore' l:path
    else
        call leaderf#folder#open(l:path)
    endif
endfunction "}}}

function! leaderf#folder#open(path) abort "{{{
    if has('win32')
        let l:cmd = "!start rundll32 url.dll,FileProtocolHandler"
    elseif has('mac')
        let l:cmd = "open"
    elseif executable('xdg-open')
        let l:cmd = "xdg-open"
    endif
    call system(l:cmd .. a:path)
endfunction "}}}

