# Rate My Professor class for data scraping and searching

Python class for scraping and searching Rate My Professor data from all professors of a single University.  This class can have numerous uses, and can be easily modified for use in your RMP applications.

### Getting Started

University objects need to be initialized with their corresponding Rate My Professor university ID. 

```python
WilliamPatersonUniversity = RateMyProfScraper(1205) #WPUNJ Object
MassInstTech = RateMyProfScraper(580)   #MIT Object
```
This ID number can be easily obtained by visiting the Rate My Professor page for your University. At this page, the URL contains the ID number for that University. 

```url
http://www.ratemyprofessors.com/campusRatings.jsp?sid=1205
http://www.ratemyprofessors.com/campusRatings.jsp?sid=580
```
### Some Functions

```
WilliamPatersonUniversity.SearchProfessor("Cyril Ku")  
```
The function above will return and print basic information on the searched professor. In this case, we search for the RMP data on Professor Cyril Ku. The printed and the returned dictionary can be found below.

```
{
'tDept': 'Computer Science', 
'tSid': '1205', 
'institution_name': 'William Paterson University', 
'tFname': 'Cyril', 
'tMiddlename': '', 
'tLname': 'Ku', 
'tid': 97904, 
'tNumRatings': 21, 
'rating_class': 'good', 
'contentType': 'TEACHER', 
'categoryType': 'PROFESSOR', 
'overall_rating': '4.3'
}
```

```
MassInstTech.PrintProfessorDetail("overall_rating")    
```
The above funtion will print out and return the requested value. The result is below.

```
4.3
```
This class can be easily edited to use in your project.
