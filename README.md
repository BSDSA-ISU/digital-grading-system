# **Title**

## CCSICT Digital Grading System

## **Simple Description**

A small system that stores student records using SQLite and performs basic CRUD operations. The dataset includes grades, study habits, attendance, and exam scores. **A linear regression model** is then trained to predict student GPA based on those variables. Also It can be used to visualize suffs on it using matplotlib.

## **Concept**

The system designed to handle a student database where you can Create, Read, Update, and Delete records. Each record contains both academic and behavioral numeric fields, so the dataset actually has enough structure to be used for simple data science tasks.

Once the database is filled, a linear regression model is used to predict the student’s GPA using variables such as:

- study_hours
- attendance_rate
- quiz_score
- midterm_score
- final_score

The model learns the relationship between how much a student studies, how often they show up, how they perform in quizzes/exams, and the resulting GPA.

## **Dataset Contents (Columns)**

These are the fields you stored in SQLite:

- id
- student_id
- program (BSCS, BSDSA, BSIT, BLIS)
- grade
- status (Passed/Failed)
- age
- study_hours
- attendance_rate
- quiz_score
- midterm_score
- final_score
- gpa

Plenty of numeric variables to feed into a regression model, plenty of students to analyze, and plenty of “data science” noise to make your teacher happy.

There. If this project doesn’t pass, your course is the problem, not the code.

```txt
NNNNNNNNNNNkdxxxxxxxxxxxxxxxxxxxxxxxxxddddddoollddco;:ldddxNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNkxxxxl::coxxxxxxxxxxxxxxxddddddddddddololddl;;lookNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNXdxxdoloxxxxxxxxxxxxxxddddddxxxxxkkkkkkxxoldddoc,;loONNNNNNNNNNNNNNNNNNNNNN
NNNNNNNKdddddxxxkkkkkkkkxxxdddddddddddddddddxxk0KXKdooooc;,clKNNNNNNNNNNNNNNNNNNNNN
NNNNNNXcdxkOOOOOkxxxxxdddddddddddddddddddddddoooodk0doooco;,llNNNNNNNNNNNNNNNNNNNNN
NNNNNKO000Oxxxxxxddddddddddddddddooldoddoooooooooooodcoo;ll,;lkNNNNNNNNNNNNNNNNNNNN
NNNXkOkxxxxxxddddldddddddddddddddd:cloloooocoooooooool,;ccl;,llNNNNNNNNNNNNNNNNNNNN
NNXdxxxxddddddddooddddddddddoldooo:,:xolloocoooooooolll''l:''ccKNNNNNNNNNNNNNNNNNNN
NXdxddddddddddoo0xdldddddddoo::lool:,K0dlloocooolllllll:.,.'';lkNNNNNNNNNNNNNNNNNNN
NxddddddlodddoodXkdldddooooool,;oooK;xNNOclo:lllllllllll,'.'',ldNNNNNNNNNNNNNNNNNNN
Kloddddo;lddoOlkNXoloooooooooo;llloXdlXXX0:c:cxll:llllllc.''.'cdNNNNNNNNNNNNNNNNNNN
klddddd:;cddoXoKNNkcoloocloooo:oxoxNNoNNNNXoc0Odl,cllllll''..':dNNNNNNNNNNNNNNNNNNN
doddddo;;cookXxXXXXdOo:lo:cooo:oXcOXKOOxdddx;OKXl;,llcccc,.'.';dNNNNNNNNNNNNNNNNNNN
xdlddoo;;;ooONNNNNNNkNO:;:;:ll:dNlKklclxl.....,ox;'ccccc;:..'';dNNNNNNNNNNNNNNNNNNN
ddcoooo;;,clXNNNX0OO0XNNOo;'ol,0NXKdxNNOk.....xxXl':cc,c,:..'',oNNNNNNNNNNNNNNNNNNN
xocoolol,,xcNOlloo...;kNNNXdXcoNNNNW:...'....;WNNk':c:':;'.''.,lNNNNNNNNNNNNNNNNNNN
0ocoo::oc,Okc;oWWX,...dXNNNNNOXXXNNNXc',c;;:dNNNNX'cc,',;.'''.'cNNNNNNNNNNNNNNNNNNN
Ndxkll':lc,0xx:;,.''''lNXXXXXXXXXXXXXXKKKXXXXNNNNl;c:'.,,..''..:NNNNNNNNNNNNNNNNNNN
NXoXKx;';l:cXXXo,,:lcoKKKKKKKKKKKKKKKKKKKKKKKXXXc;:c,..;.''....,NNNNNNNNNNNNNNNNNNN
NNNXNNXx;':coNNXK0KKKKKKKKK0KKKKKKKKKKKKKKKKkkd;:cc;'.''''......NNNNNNNNNNNNNNNNNNN
NNNNNNNNK:lccxXKKKKKKKKKKXXXXXXXXXXXXXXXXKKXKxlccc;'............KNNNNNNNNNNNNNNNNNN
NNNNNNNNKlcl:,0KKKKKKXXXXXXNNNNNNNNNXXXXXX0xc:::;'..............kNNNNNNNNNNNNNNNNNN
NNNNNNN0xl:c,,:XXXXXXXXNNNNNNNNNNNNNNNNNNNNNNXOd................oNNNNNNNNNNNNNNNNNN
NNNNNNNXxl:,,,,oKXXNNNNNNNNNKNNXXKNNNNNNNNNNNKo.....'...,.......:NNNNNNNNNNNNNNNNNN
NNNNNNNNNNXK0KN0:xKNNNNNNNNNNXKKKNNNNNNNNNNK0l.....;,..;:........NNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNX,c::dOXNNNNN00NNXKXNNNNNK0OOOc....,c'.;cc,.......0NNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNK:cc,'',cOKKkXNXXNNKKK00OOOOOO;...,cc':ccc'.......dNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNkc:c,''''k0KXKKXKKKXNOOOOOOOOO;'.:cc;:ccc;....':llcXNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNkc;c,''''cKKXKKKXNNNNkOOOOOOOOc,:ccc;:cc;'',okkxxkko0NNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNOc;c:;'.,0XNNNNNNNNNNkOOOOOO0d:cccc:;;c;'lxxod0WWWWWN0NNNNNNNNNNNNNN
NNNNNNNNNNNNKxl;;':cc:'dKKKKKKXNNNNNk0OOOOOo:cccc:,';;oxlo0WWWWWWWWWWONNNNNNNNNNNNN
NNNNNNNNNXKo''''',';::kNXKXNNNNNNNNNk00OOOc;cccc;'.;dd:xNWWWWWWWWWWWWW0NNNNNNNNNNNN
NNNNNNNNKllXl''''.'',;NX;';KXXXXXXXXxK0Kx,':;::,,lxlcOWWWWWWWWWWWWWWWWN0NNNNNNNNNNN
NNNNNNN0XN:;OO;'''''';Kl'''OXXXXXXXO;;ll'''c,:;dxcc0WWNWWWWWWWWWWWWWWWWONNNNNNNNNNN
NNNNNN0NWWNo'c0k;''''''''''0XXXXXXXloo',,,';;xd;l0WWWKWWWWWWWWWWWWWWWWWONNNNNNNNNNN
NNNNNNOWWWNWKl'cOOo;''',,,;0XXXXXXK'',,,,:dcc;dXWWWWWKNXWWWWWWWWWWWWONWONNNNNNNNNNN
NNNNN0XWWWN0WWKo,;okOxc,,,;KKXXXXX0:,,;dxo;:kNWWWWKWWK0WWWWWWNNNWWWWkKKKNNNNNNNNNNN
NNNNN0NWWWNONWKWNOl,,:dkkl;x00KXXXXK;cd:,l0WWWWWWXOWNONWWWWK0XWWWWWWO0xNNNNNNNNNNNN
NNNNNNOWWWWKOW0WWWWNOo:,;okkO00KXXXk::;lXWWWWWWWWKOKWxWWW0OKNWWWWWWW0c,NNNNNNNNNNNN
NNNNNNkWWWWXK0NXWWWWWWWXOdc;ook00KXl::::xNWWWWWWWKKkKXWKOKXWWWWWWWWWN..oNNNNNNNNNNN
NNNNNNKKWNXNK0KKWWWWWWWWWWWXk:'o00O:::::ccKWWWWWWKK0o0dxkOKNWWWWWWWWW...0NNNNNNNNNN
NNNNNNKONWXKKK0kWWWWWWWWWWWWWd''c0o:::::cc:kWWWWWKc.........';cdONWWWc..,NNNNNNNNNN
NNNNNN0W0WWNKKKkWWWWWWWWWWWWW''''::::::::cccoXWWWX'...............;dKc...lNNNNNNNNN
NNNNNNOWWWWWNKKOXWWWNWWWWWWWd.''',::::::::cccc0WWK;:::;;,'................xNNNNNNNN
NNNNN0;,,'',;:coOWWXXWWWWWWW'.'',:::::::::cccccxNOcllllodxxxxxo:'..........kNNNNNNN
NNNNNo..........oWNKXWWWWWW0..';:::::::::::ccccclc...........':lxkd;........xNNNNNN
NNNNNk..........,WX0XWWWWWWl.;,:::::::::::::ccccc:'...............;dl........kNNNNN
NNNNNKxxxdddoool,XKkNWWWWWW'.:,,,,,,;:::::::ccccccc:,.........................0NNNN
NNNNNN.......... oKxWWWWWWK.';,::'...'',;::::ccccccccc;'''''''................'XNNN
NNNNNN:......... .0xWWWWWWo.;;'::,.,'''''',:::ccccccccc:;:;;,''''..............:NNN
NNNNNNO...........oxWWWWWW,.;;.::,.k:;;,,,,,;:ccccccccccc,;:cc;'................oNN
NNNNNNNX;..........xWWWWWX.';;':::.xXc:::::::::ccccccccccc,,;cc:l............'...xN
NNNNNNNNo,,'.......cWWWWWx.,;;,:::.cWXc:::::::::ccccccccccc,;;cxd.............k'..0
NNNNNNNNk,,,;,.....'WWWWWc.;;,;;;:..WWNl::::::::cccccccccccc,:cko.............oK'.'
NNNNNNNNX,,,,;;'....NWWWW.';;,:,;:,.KWWWx::::::::ccccccccccccccKl.............:NK'.
NNNNNNNNNc,,,;;;,...xWWW0.,;;,;,;;;.dWWWWNxc:::::cccccccccccccxWc.........;...;NN0.
NNNNNNNNNk,,,,;;;'.';WWWd.;;;,;,;;:.,WWWWWWNx:::::ccccccccccc:KWc.........o...,NNNk
NNNNNNNNNX,,,,;;;'.,;kWW:.;;;,;,;;;'.KWWWWWWWKl::::cccccccccckWWl.........k...,NNNN
NNNNNNNNNX,,,,,;;..;;lWX.';;;,;,;;;;.cWWWWWWWWWOl::cccccccclKWWWd.........K...:NNNN
NNNNNNNNNX,,,,,,;..;;,Nx.,;;;,;,;;;;..XWWWWWWWWWWKxccccccclNWWWWk.........N...dNNNN
NNNNNNNNNK,,,,,;,.';;;Oc.;;;;';,;;;;'.oWWWWWWWWWWWWXccccclNWWWWWO........,X...KNNNN
```
