import pandas as pd
def project_student_grades():
    print("\nPROJECT 1: STUDENT GRADE ANALYZER")
    print("-" * 40)
    student_data = {
        'student id':[4401,4402,4403,4404,4405,4406,],
        'name':['navya','kavya','puji','suji','kavitha','loyal'],
        'grade':['A','B','C','B','C','D'],
        'math_score':['32','54','65','88','92','99'],
        'english_score':['88','90','92','45','56','67'],
        'science_score':['77','90','45','22','87','36'],
        'attendance':['32','86','82','45','42','97']
            
    }
    df = pd.DataFrame(student_data)
    
    df['math_score'] = df['math_score'].astype(int)
    df['english_score'] = df['english_score'].astype(int)
    df['science_score'] = df['science_score'].astype(int)
    df['attendance'] = df['attendance'].astype(int)
    
    print("your tasks")
    
    print("1. calculate the each student total_score")
    df["total_score"] = df['math_score'] + df['english_score'] + df['science_score']
    print(df[['name','total_score']])
    
    print("2. find  average score of  grade")
    avg_of_grade = df.groupby('grade')['total_score'].mean()
    print(avg_of_grade)

    print("3.find students with attendance > 90%")
    high_attendance = df[df['attendance'] > 90]
    print(f"studence with > 90% attendance: {len(high_attendance)}")
    print(high_attendance[['name','attendance']])
    
    print("4.top3 score of students")
    top_score = df.nlargest(3, ['total_score'])
    print(top_score[['name','total_score']])
    
    return df
project_student_grades()