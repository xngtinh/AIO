!gdown https: // drive.google.com/uc?id = 1IBScGdW2xlNsc9v5zSAya548kNgiOrko
file_path = "/content/P1_data.txt"


def word_count(file_path):
    dic = {}
    with open(file_path, 'r') as f:
        for line in f:
            for word in line.split():
                word = word.lower().strip()
                if word:
                    if word in dic:
                        dic[word] += 1
                    else:
                        dic[word] = 1
        return dic


word_count(file_path)
