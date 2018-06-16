import requests
import json
import math

def search_list(search_name, professorlist):# function searches for professor in list
    for i in range(0, len(professorlist)):
        if (search_name == (professorlist[i]['tFname'] + " " + professorlist[i]['tLname'])):
            return i
    return False #Return False is not found

def print_professor(indexnumber,professorlist):#print search professor's name and RMP score
    if indexnumber == False:
        print("not found")
    else:
        prof_name = professorlist[indexnumber]['tFname'] + " " + professorlist[indexnumber]['tLname']
        print("Search Result:")
        print(indexnumber)
        print(prof_name)
        print(professorlist[indexnumber]['overall_rating'])
        print("______")

def get_num_of_prof(id): #function returns the number of professors in the university of the given ID.
    page = requests.get("http://www.ratemyprofessors.com/filter/professor/?&page=1&filter=teacherlastname_sort_s+asc&query=*%3A*&queryoption=TEACHER&queryBy=schoolId&sid=" + str(id))  # get request for page
    temp_jsonpage = json.loads(page.content)
    num_of_prof = temp_jsonpage['remaining'] + 20  # get the number of professors at William Paterson University
    return num_of_prof

search_name ="Scott McDonough" #name of professor to search for
university_id = 1205#RMP university ID for university where professor will be searched.
num_of_prof = get_num_of_prof(university_id)
num_of_pages = math.ceil(num_of_prof / 20)

print ("Number of prosf:" , num_of_prof)
print ("Number of pages:", num_of_pages)

professorlist = []

#the loop insert all professor into list
i = 1


while( i <= num_of_pages):
    page = requests.get("http://www.ratemyprofessors.com/filter/professor/?&page="+str(i)+"&filter=teacherlastname_sort_s+asc&query=*%3A*&queryoption=TEACHER&queryBy=schoolId&sid=1205")
    temp_jsonpage = json.loads(page.content)
    temp_list = temp_jsonpage['professors']
    professorlist.extend(temp_list)
    i+=1

indexnumber = search_list(search_name, professorlist) #calls function to search for professor and returns index of profesor in the list.
print_professor(indexnumber, professorlist) #calls function to display professor's full name and RMP score

"""
import requests
import json
import math

class RateMyProfScraper:

        def __init__(self,name,schoolid):
            self.ProfessorName = name
            self.UniversityId = schoolid
            self.professorlist = self.updateprofessorlist()
            self.indexnumber = self.search_list()
            self.print_professor()

        def search_list(self):  # function searches for professor in list
            for i in range(0, len(self.professorlist)):
                if (self.ProfessorName == (self.professorlist[i]['tFname'] + " " + self.professorlist[i]['tLname'])):
                    return i
            return False  # Return False is not found

        def updateprofessorlist(self):
            tempprofessorlist = []
            num_of_prof = self.get_num_of_prof(self.UniversityId)
            num_of_pages = math.ceil(num_of_prof / 20)
            i = 1
            while (i <= num_of_pages):# the loop insert all professor into list
                page = requests.get("http://www.ratemyprofessors.com/filter/professor/?&page=" + str(
                    i) + "&filter=teacherlastname_sort_s+asc&query=*%3A*&queryoption=TEACHER&queryBy=schoolId&sid=1205")
                temp_jsonpage = json.loads(page.content)
                temp_list = temp_jsonpage['professors']
                tempprofessorlist.extend(temp_list)
                i += 1
            return tempprofessorlist

        def get_num_of_prof(self,id):  # function returns the number of professors in the university of the given ID.
            page = requests.get(
                "http://www.ratemyprofessors.com/filter/professor/?&page=1&filter=teacherlastname_sort_s+asc&query=*%3A*&queryoption=TEACHER&queryBy=schoolId&sid=" + str(
                    id))  # get request for page
            temp_jsonpage = json.loads(page.content)
            num_of_prof = temp_jsonpage[
                              'remaining'] + 20  # get the number of professors at William Paterson University
            return num_of_prof

        def print_professor(self):  # print search professor's name and RMP score
            if self.indexnumber == False:
                print("not found")
            else:
                prof_name = self.professorlist[self.indexnumber]['tFname'] + " " + self.professorlist[self.indexnumber]['tLname']
                print("Search Result:")
                print(self.indexnumber)
                print(prof_name)
                print(self.professorlist[self.indexnumber]['overall_rating'])
                print("______")


WilliamPaterson = RateMyProfScraper("Scott McDonough",1205)
WilliamPaterson.print_professor()

"""

