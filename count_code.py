def count_code(filename):
    count=0
    for i in range (len(filename)-3):
        if filename[i:i+4] == "code" or filename[i:i+4] == "cope" or filename[i:i+4] == "cooe":
            count+=1
    return count

print(count_code("codepython"))
print(count_code("copepython"))
print(count_code("cooepython"))
print(count_code("cooecode"))
print(count_code("cooecodepython"))