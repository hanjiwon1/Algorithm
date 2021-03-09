def solution(skill, skill_trees):
    answer = 0
    idx = 0
    for i in skill_trees:
        for j in i:
            if j not in skill:
                skill_trees[idx] = skill_trees[idx].replace(j, '')

        
        skill_idx_list = []
        tree_idx_list = []
        for j in skill_trees[idx]:
            skill_idx_list.append(skill.index(j))
            tree_idx_list.append(skill_trees[idx].index(j))

        if skill_idx_list == tree_idx_list: answer += 1
        
        idx += 1

    
    return answer

'''
skill = input()
skill_trees = list(map(str, input().split()))
print(solution(skill, skill_trees))
'''
