def solution(files):

    processed_files = []
    
    for file in files:
        
        p1, p2 = 0, 0
        while p1 < len(file):
            if file[p1].isdigit():
                p2 = p1
                while p2 < len(file) and file[p2].isdigit():
                    p2 += 1
                break
            else:
                p1 += 1
        
        processed_files.append((file[:p1],file[p1:p2],file[p2:]))

    processed_files.sort(key = lambda x: (x[0].lower(), int(x[1])))

    
    return [''.join(processed_file) for processed_file in processed_files]