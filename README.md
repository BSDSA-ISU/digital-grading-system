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
                                                                           
                                                                           
                      ..',,,,,'....        ....',,,,,'.                    
                     .,;,;;;;;;;;;;,'...',,;;,,;;;;;;;;'                   
                     .,,,,,,;;;,,;:ccccccc::;,,;;;,,,;;;                   
                        ',;,;:cldolc:;c:cldddolc;,,;,.                     
                      .',:clollc:',,,,,;:;,,cloddoc:;'...                  
                  .,,,:lol::::c:;,,,,,,:c;,,,,;;:ldddoc;;c:'               
                'cddlol;',;,;:;,;;,;,,;,',;,,;,;;',:lddddoddo;.            
             .;ldddlc,,;::,,,,,;,;::c;';;;';cc:;,,,;';coddddddo;           
           .:odddc;,,,,;c:;',;,',:c:,;;,,,;;,;:;,;,,;,;;:ldddddd:          
          .odddd:;,;;,;;',;;,;,;;,',;,,:::,,;,';;,;;,;;',,cdddddd;         
         .lddddl'':cc:'';:.,:cc;.:;,'::c:c:,';;,';:c:',;:''odddddd'        
         .dddddl,;,,;,;;',;;,;,;;'',;',;:;';,',,;;'',;,,,,;;ddddddl        
         'dddddo,,,;;,';::;;:;ccclllllooodooolllc::;,':cc;''ddddddo        
          dddddd,,;;::cloddddddddddddddddddddddddddddolcc,,'ddddddd        
          ;ddddo:lodddddddddddddddddddddddddddddddddddddddl,odddddc        
         :lddxlldddddddddddddddddddddddddddddddddddddddddodOOdkxd:         
        : oNN0lddddddddddddddddddddddddddddddddddddddddookXNNkKNNO         
      '  ,XNNodddddddddddddddddddddddddddddddddddddddodOXNNNNNdXNN,        
        .00NXlddddddoooddd:dkoklkOxokxodooodddddddlxxdNNNNNNNNXkNNk        
        lOONXcoooxkkcOkXNOdOKoxdNWWkKNxXNX0OlkddcodWWkkNNXNNNNNkXNK        
        kdXNN0o0XNNxONkcKdKWWKoKWWWWxOkONNNk0NNWKxkWWNkkNk0NNNNKONN.       
       .kKNNNXkNNNKdNWX0o0K0KKOWWWWWWOodNKKxWWNKKkkNWWWOkkxNNNNNkNN,       
        'KNNNXxNNNoKW0l;:,'';oONWWWWWWXlNdlWWNOdc,',;;lO0odXNNNNkNXl       
       ..oXNNNxXNOxXc.ll,..oX0lWWWWWWWWKd0XWWWc'..oK0d:.:koXXOxNxNNo       
         .NNNNkXNcK,.xo,'..:X0cxWWWWWWWWWWWWWx:...lN0:Od.'xXOKxXxNNo       
          KNN0Xd0;o.,W:........:WWWWWWWWWWWWW'........oN'.cOxNXkkNNo       
          dNXxNXdoOKxMk.,:;lxo.OWWWWWWWWWWWWWx.;l:ld:.0Mxxkd0NNkxNNl       
          ;XNkXNNklWWWWKdlxKKOKWWWWWWWWWWWWWWWOllOK0kXWWWkoxXNXxNNNc       
          .NNKONNK:WWWWWWWWWWWWWWWWWWWNWWWWWWWWWWXNWWWWWWNdkNNXkNNN,       
           XNXxXNXoKWWWNNXNNWWWWWWWWWWWWWWWWWWWWWNNNNNWWWXoKNNNxXNN.       
           0NNxXNO0lxWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW0xdkXNKONNX        
           xNXkNNOOc:0WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWK::OdNNxXNNK        
           lNNxNNXoxc:xNWWWWWWWWWWWWWWNXWWWWWWWWWWWWWXx:c:KxNNdNNNx        
           ;XNkXNNd0;cc:okKWWWWWWWWWWWWWWWWWWWWWWWXOd:cccdkXNNdXNNx        
           ,NX0ONNXxlccccc:coxk0KNWWWWWWWWWNX0Oxdl:ccccc;KkNNXxNNNx        
           ;NNXxNNNxO:ccccccc,;:::::cokkol;;::c,:cccccc:dkXNNO0NNNx        
           oNNNdNNN0;l:cc::c:;;coddooKK0xlddddc;;:::ccccOdNNNkNNNNO        
           kNNNdONNX;c:::lddddolclllldxxdldddolooddoc:;x;ONN0xNNNNK.       
          .XNNNdxKNNd:,:dddddddddlcclc:::cc:oddddddddlo:;XNNxkNNNNN,       
          oNNNNd0oXNX:d;odddddddddlcooooooo:ddddddddoclcoNNOkdNNNNNk       
         ,KNNNXc0,XNNdddloddddddolccll,,olcclddddddo:odlXNX,0:ONNNNXo      
        .0NNNN0cdclXNKlddldddddddddddc',cddddddddddcddoxXNd:kclXNNNNNc     
        ONNNNNxc:doxNNxdddddddddddddl0:lodddddddddddddcXN0cooccONNNNNK.    
       cNNX0NXllKdclxXXldddddddddddoO0.,0ldddddddddddlKN0olx:ccdNNXXNNx    
       ONXoONK:NWXlKxlXXldddddddddokMx..N0odddddddddlONOld:ld;clXNKoXNX.   
       0Xd xNOcoWWNNWdck0ldddddddokMMo..KMxodddddddlkKdlol;c:cccXNK dXN.   
       0k. .NkccoNWWWNc;OxokddodxKMMM;.'xMWkoddooooxOdxKXXccccccKNc .xN.   
       cl   :OccclNWWWxdXWMMMMWMMMMMW'..cMMMNK0KXWMMXKdWWWK:;cccX0   cK    
        ;    .occc:XWNkNMMMMMMMMMMMMO'..,WMMMMMMMMMMXXXOWWW0:cco:    c.    
               .c:dWNOWMMMMMMMMMMMMMo.'.'KMMMMMMMMMNXWMNkNWWk'             
                oOWNxWMMMMMMMMMMMMMW;.,,.oMMMMMMMMWNWMMMWOWWWc             
                   dWWMMMMMMMMMMMMMK';lc.,WMMMMMMMMMMMMMMXKWWX'            
                  .KWWMMMMMMMMMMMMMo,lll'.0MMMMMMMMMMMMMMMOWWWx            
                  .dk0NWMMMMMMMMMMW,:lll;'lWMMMMMMMMMMMNKOdkWNK            
                  .',;,:lk0XWWMMMMd'lllll,'NMMMMMWX0xl:;;:cl0Ol            
                 ':lll;lc::,,:clod,,lllll:'ldolc;;;::lc:llllcl             
                 .lllccllllccllcc:;:lllll:c:cccl;clllllc:ll.               
                        clc;llllll:cllllll:lllllc:llc:                     
                        ;kkxxxddddoo'    ,loooddkkkkO;                     
                        'NNWWWNNX0Ok.    'kO0XXNWWWWW.                     
                        .WWWWWWWWWWN.    .NWWWWWWWWWN                      
                         WWWWWWWWWWW     .WWWWWWWWWWX                      
                        .WWWWWWWWWWK      WWWWWWWWWWX                      
                        .WWWWWWWWWWx      KWWWWWWWWWN                      
                        .WWWWWWWWWWl      xWWWWWWWWWW                      
                        .NWWWWWWWWN'      cWWWWWWWWWX                      
                         ,;:::cc::;       .;:ccccc:;'                      
                         .'''''''''        '''''''''.                      
                          '''''''''       .'''''''''                       
                          .''''''',       .''''''''.                       
                           ''''''',       .''''''''                        
                           .'''''''.      .'''''''                         
                            '''''''.      .''''''.                         
                            .''''''.      '''''''                          
```
