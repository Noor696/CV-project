import json
import os

class CV:
    path="/home/noor/AdvPy-401/CV-project/CV-lab/templates"
    def __init__(self, Bio_sentence , Bio_template , lang_sentence, lang_template):
        self.Bio_template = Bio_template
        self.Bio_sentence = Bio_sentence
        self.BioInfo_input = []
        self.Bio = None
        self.lang_sentence = lang_sentence
        self.lang_template = lang_template
        self.language_input = []
        self.language = None

# ----------- Bio Part --------------
    
    @classmethod
    def getBio_template(cls,name, path=None):
        if not path:
            path = cls.path
        fpath = os.path.join(path, name)
        # print(os.path.exists(fpath))
        with open(fpath, "r") as f:
            data = json.load(f)
         # print(data)
        cvBioPart = cls(**data)
        # print(cv1.Bio_sentence)
        return cvBioPart

    def get_BioInfo_from_user(self):

        print("please provide the following information About your profile")
        
        for word in self.Bio_sentence:
          input_sentence = input(word + " ")
          self.BioInfo_input.append(input_sentence)
        return self.BioInfo_input

    def build_Bio(self):

        self.Bio = self.Bio_template.format(*self.BioInfo_input)
        return (self.Bio)

    def show_Bio(self):
        with open("template.txt",'w') as file:
            file.write(Bio)
            print (Bio)



# ----------- Languaga Part --------------

    @classmethod
    def get_languaga_template(cls,name, path=None):
        if not path:
            path = cls.path
        fpath = os.path.join(path, name)
        with open(fpath, "r") as f:
            data = json.load(f)
            # print(data)
        cvlangPart = cls(**data)
        return cvlangPart

    def get_language_from_user(self):

        print("please provide the following information About the languages you speak")
        
        for l in self.lang_sentence:
          input_lang_sentence = input(l + " ")
          self.language_input.append(input_lang_sentence)
        return self.language_input

    def build_language(self):

        self.language = self.lang_template.format(*self.language_input)
        return (self.language)

    def show_language(self):

        with open("template.txt",'a') as file:
            file.write(language)
            print("\n")
            print (language)

    


temp_name = "basic_template.json"
cvBioPart= CV.getBio_template(temp_name)
sentences = cvBioPart.get_BioInfo_from_user()
Bio = cvBioPart.build_Bio()
cvBioPart.show_Bio()

cvlangPart = CV.get_languaga_template(temp_name)
sentences_lang= cvlangPart.get_language_from_user()
language = cvlangPart.build_language()
cvlangPart.show_language()





# the Sub classes : 
    
class Chronological_Resumes_cv (CV):
    def __init__(self):
        super().__init__()
    
    def about_Chronological():
        print("""this type of resume is ideal for those with a solid, gap-free work history inline with the type of job you are applying for. The Work History or Professional Experience sections of this type of resume are the most pronounced and span between eighta to ten years depending on the number of years at your prior institutions.""")

class Functional_cv (CV):
    def __init__(self):
        super().__init__()

    def about_Functional():
        print("""Functional resumes tend to highlight skills and their application relating to the job description, When building a functional resume, you will list these skills and certifications first and how you have used them in practical situations and highlight how you could use them in a paid position.""")

class Combination_cv (CV):
    def __init__(self ):
         super().__init__(self)

    def about_Combination():
        print("""Combination resume type is a combination of both chronological and functional. Typically this means that both a robust work history and a built-out skills section are listed within the resume. Creating a combination resume is easier with significant work and education experience.""")
