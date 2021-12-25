# Creating a search engine

def matchingwords(sentence1,sentence2):
    words1 = sentence1.split()
    words2 = sentence2.split()
    score = 0

    for word1 in words1:
        for word2 in words2:
            if word1.lower() == word2.lower():
                score+=1
    return score


if __name__ == '__main__':
    sentences = ["This is good","Python is good","Tahmid is a bad boy"]
    query = input("Enter the query string:")
    newlist = [matchingwords(query,sentence) for sentence in sentences]
    sortedsentscore = [sentscore for sentscore in sorted(zip(newlist,sentences),reverse=True) if sentscore[0]!=0]

    print(f"{len(sortedsentscore)} results found!")
    for sent,item in sortedsentscore:
        print(f"\"{item}\" with a score of: {sent}")


