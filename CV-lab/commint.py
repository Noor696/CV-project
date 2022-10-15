
# test=Chronological_Resumes_cv()
# print (test)
# class Functional_cv (CV):
#     def __init__(self):
#         super().__init__()

#     def about_Functional():
#         print("""Functional resumes tend to highlight skills and their application relating to the job description, When building a functional resume, you will list these skills and certifications first and how you have used them in practical situations and highlight how you could use them in a paid position.""")

# class Combination_cv (CV):
    
    
#     def __init__(self, Education_sentence, Education_template, Experiance_sentence, Experiance_template ):
#         super().__init__(self)
#         self.Education_sentence = Education_sentence
#         self.Education_template = Education_template
#         self.Education_input = []
#         self.Education = None
#         self.Experiance_sentence = Experiance_sentence
#         self.Experiance_template = Experiance_template
#         self.Experiance_input = []
#         self.Experiance = None


#     def about_Combination():
#         print("""Combination resume type is a combination of both chronological and functional. Typically this means that both a robust work history and a built-out skills section are listed within the resume. Creating a combination resume is easier with significant work and education experience.""")

#     @classmethod
#     def get_Education_template(cls,name, path=None):
#         if not path:
#             path = cls.path
#         fpath = os.path.join(path, name)
#         with open(fpath, "r") as f:
#             data = json.load(f)
#             # print(data)
#         cvEducationPart = cls(**data)
#         return cvEducationPart

#     def get_Education_from_user(self):

#         print("please provide the following information About your Education")
        
#         for e in self.Education_sentence:
#           input_Education_sentence = input(e + " ")
#           self.Education_input.append(input_Education_sentence)
#         return self.Education_input

#     def build_Education(self):

#         self.Education = self.Education_template.format(*self.Education_input)
#         return (self.Education)

#     def show_Education(self):
#         print(Education)


# cvEducationPart = Combination_cv.get_Education_template(temp_name)
# sentences_Education= cvEducationPart.get_Education_from_user()
# Education = cvEducationPart.build_Education()
# cvEducationPart.show_Education()

# "Education_sentence" : ["Education","School","City","Start date", "End date"],
# "Education_template" : "{} {} {} {} {}",
# "Experiance_sentence" : ["Experiance", "Company", "Duration", "Description"],
# "Experiance_template" : "{} {} {} {}"

# "Education_sentence" : ["Education","School","City","Start date", "End date"],
# "Education_template" : "{} {} {} {} {}",
# "Experiance_sentence" : ["Experiance", "Company", "Duration", "Description"],
# "Experiance_template" : "{} {} {} {}"




 
# ------------------------------------------------------

# we need welcome messege function (Super Class)

# we need Bio function take from user basic information: (Super Class)
# (name, familyName, Date of Birth, Email address, Phone number, Address, Nationality, Gender)

# we need Language function take from user this information: (Super Class)
# (language, level)

# we need Education function take from user information for each Edu: (Sub Class)
# [Education, School, ..]


# we need Skills function take from user list of skills: [s1,s2,s3,s4,s5] (Sub 