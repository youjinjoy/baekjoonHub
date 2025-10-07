def solution(record):
    result = []
    
    id_nic_map = {}
    
    for message in record:
        
        splitted = message.split(' ')
        
        if splitted[0] == 'Enter':

            uid = splitted[1]
            
            result.append(('Enter', uid))
            id_nic_map[uid] = splitted[2]
                
        elif splitted[0] == 'Change':
            
            uid = splitted[1]
            id_nic_map[uid] = splitted[2]
            
        elif splitted[0] == 'Leave':
            uid = splitted[1]
            result.append(('Leave', uid))
        else:
            raise Exception('입력값 에러: record 내부에 Enter, Change, Leave 중 하나로 실행되지 않는 메세지가 있습니다.')

    answer = []
    for message in result:
        behavior, uid = message
        if behavior == "Enter":
            answer.append(f"{id_nic_map[uid]}님이 들어왔습니다.")
        else:
            answer.append(f"{id_nic_map[uid]}님이 나갔습니다.")
    
    return answer