# Rate My Professor class for data scraping and searching

Python class for scraping and searching Rate My Professor data from all professors of a single University.  This class can have numerous uses, and can be easily modified for use in your RMP applications.

### Getting Started

University objects need to be initialized with their corresponding Rate My Professor university ID. 

```python
WilliamPatersonUniversity = RateMyProfScraper(1205) #WPUNJ Object
MassInstTech = RateMyProfScraper(580)   #MIT Object
```
This ID number can be obtained by visiting the Rate My Professor page for your University. This number can be easily obtained from the URL.  

```
http://www.ratemyprofessors.com/campusRatings.jsp?sid=1205
http://www.ratemyprofessors.com/campusRatings.jsp?sid=580
```



