set nocompatible

" remap key
" insert mode
inoremap " ""<Esc>i
inoremap ' ''<Esc>i
inoremap ( ()<Esc>i
inoremap [ []<Esc>i
inoremap {<CR> {<CR>}<Esc>ko
inoremap jj <Esc>

" normal mode
nnoremap <F4> :set invrnu!<CR>


" indent
set tabstop=4
set smartindent
set shiftwidth=4
set expandtab
set softtabstop=4
filetype indent on
filetype plugin indent on
set backspace=indent,eol,start

" syntex
syntax enable
set hlsearch incsearch
set showmatch

" abbr
iab clsS class Solution:<CR>def

" ruler
set rnu

" style setting
set ruler
set colorcolumn=80
highlight ColorColumn ctermbg=5
