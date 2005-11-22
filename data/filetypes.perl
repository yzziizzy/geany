[styling]
# foreground;background;bold
default=0x000000;0xffffff;false
error=0x0000ff;0xffffff;false
commentline=0x0000ff;0xffffff;false
number=0x007F00;0xffffff;false
word=0x991111;0xffffff;true
string=0x1E90FF;0xffffff;false
character=0x1E90FF;0xffffff;false
preprocessor=0x7F7F00;0xffffff;false
operator=0x101030;0xffffff;false
identifier=0x100000;0xffffff;false
scalar=0x00007F;0xffffff;false
pod=0x000000;0xe0c0e0;false
regex=0x905010;0xffffff;false
array=0x905010;0xffffff;false
hash=0x905010;0xffffff;false
symboltable=0x905010;0xffffff;false
backticks=0x000000;0xe0c0e0;false

[keywords]
primary=NULL __FILE__ __LINE__ __PACKAGE__ __DATA__ __END__ AUTOLOAD BEGIN CORE DESTROY END EQ GE GT INIT LE LT NE CHECK abs accept alarm and atan2 bind binmode bless caller chdir chmod chomp chop chown chr chroot close closedir cmp connect continue cos crypt dbmclose dbmopen defined delete die do dump each else elsif endgrent endhostent endnetent endprotoent endpwent endservent eof eq eval exec exists exit exp fcntl fileno flock for foreach fork format formline ge getc getgrent getgrgid getgrnam gethostbyaddr gethostbyname gethostent getlogin getnetbyaddr getnetbyname getnetent getpeername getpgrp getppid getpriority getprotobyname getprotobynumber getprotoent getpwent getpwnam getpwuid getservbyname getservbyport getservent getsockname getsockopt glob gmtime goto grep gt hex if index int ioctl join keys kill last lc lcfirst le length link listen local localtime lock log lstat lt m map mkdir msgctl msgget msgrcv msgsnd my ne next no not oct open opendir or ord our pack package pipe pop pos print printf prototype push q qq qr quotemeta qu qw qx rand read readdir readline readlink readpipe recv redo ref rename require reset return reverse rewinddir rindex rmdir s scalar seek seekdir select semctl semget semop send setgrent sethostent setnetent setpgrp setpriority setprotoent setpwent setservent setsockopt shift shmctl shmget shmread shmwrite shutdown sin sleep socket socketpair sort splice split sprintf sqrt srand stat study sub substr symlink syscall sysopen sysread sysseek system syswrite tell telldir tie tied time times tr truncate uc ucfirst umask undef unless unlink unpack unshift untie until use utime values vec wait waitpid wantarray warn while write x xor y
