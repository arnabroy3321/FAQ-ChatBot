import re

responses = {
    r"(college.*timing|timing.*college|working hours|college hours)": 
        "College timings are 9:00 AM to 5:10 PM except sunday.",

    r"(admission|apply|enrollment|join college)": 
        "You can apply for admission online through our website.",

    r"(document|required document|certificate|papers needed)": 
        "Required documents are 10th Marksheet, 12th Marksheet, Aadhaar Card, and Passport Photo.",

    r"(course|program|degree|available courses)": 
        "We offer B.Tech, BCA, MCA, MBA, and M.Tech programs.",

    r"(fee|fees|tuition|cost)": 
        "Fee structure varies by course. Please contact the accounts department.",

    r"(hostel|accommodation|stay|residence)": 
        "Yes, hostel facilities are available for both boys and girls.",

    r"(library|book room|reading room)": 
        "Library is open from 9:00 AM to 5:30 PM.",

    r"(contact|phone|email|reach you)": 
        "You can contact us at +91-9876543210.",

    r"(scholarship|financial aid|grant)": 
        "Scholarships are available based on merit and eligibility.",

    r"(class|classes|semester start|session start)": 
        "Classes generally start in August every year.",

    r"(attendance|minimum attendance|attendance requirement)": 
        "Students must maintain at least 75% attendance.",

    r"(result|exam result|marks|grade)": 
        "Results can be accessed through the student portal.",

    r"(transport|bus|college bus|travel facility)": 
        "College buses are available on major routes.",

    r"(exam|examination cell|exam office)": 
        "The Examination Cell is located in first floor.",

    r"(location|address|where is college|college situated)": 
        "The college is located - 81, Nilgunj Rd, Jagarata Pally, Deshpriya Nagar, Agarpara, Kolkata, West Bengal 700109.",

    r"(faculties|teachers|education quality)":
        "The JIS University offers quality education, and the teachers are very friendly. The university is well known for its placement. It provides good quality education.",
    
    r"(placement|job|job opportunity)":
        "decent."
}