# DEVELOPMENT OF A FACIAL RECOGNITION BASED ATTENDACE SYSTEM (A CASE STUDY OF Afe Babalola University, Ado-Ekiti, Nigeria)

# BY: OKONKWO PASCHAL CHIEMERIE

# MATRIC NUMBER: 20/SCI01/093

# A PROJECT REPORT SUBMITTED TO COMPUTER SCIENCE PROGRAMME, DEPARTMENT OF MATHEMATICAL AND PHYSICAL SCIENCES, COLLEGE OF SCIENCES, AFE BABALOLA UNIVERSITY,
# ADO-EKITI, NIGERIA.

# IN PARTIAL FULFILMENT OF THE REQUIREMENTS FOR THE AWARD OF
# BACHELOR OF SCIENCE (B.Sc.) DEGREE IN COMPUTER SCIENCE
# MAY, 2024


<h2>NOTE: For effective runing processes, This System was ran on Oracle VM VirtualBox runing ubuntu-22.04.4-desktop-amd64</h2>
<h2>To run the system the after all dependencies has been installed run `gui.py`</h2>

<p>Integrate all CCTV cameras with this system to take students' attendace in a classroom setting through facial recognition. This system can also be used to maintain records of students and staff live locations, eliminating the need for biometrics, cards, or manual entry. When linked with a school's student database, the system can track students and register their attendance for lectures.</p>

NOTE: FOLLOWS SHOULD BE INSTALLED
dlib
face_recognition
opencv-python
numpy
pandas  : `pip install pandas`, if not working try `pip --default-timeout=100 install pandas`

Requirements
Python 3.3+ or Python 2.7
macOS or Linux (Windows not officially supported, but might work)
Installation Options:
Installing on Mac or Linux
First, make sure you have dlib already installed with Python bindings:
https://gist.github.com/ageitgey/629d75c1baac34dfa5ca2a1928a7aeaf

Then, make sure you have cmake installed:

brew install cmake

Finally, install this module from pypi using pip3 (or pip2 for Python 2):

pip3 install face_recognition


While Windows isn't officially supported, helpful users have posted instructions on how to install this library:

@masoudr's Windows 10 installation guide (dlib + face_recognition) https://github.com/ageitgey/face_recognition/issues/175#issue-257710508
