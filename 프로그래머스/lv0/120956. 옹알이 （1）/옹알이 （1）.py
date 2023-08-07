def solution(babbling):
    word_list = ['aya', 'ye', 'woo', 'ma', 'ayaye', 'ayawoo', 'ayama', 'yeaya', 'yewoo', 'yema', 'wooaya', 'wooye', 'wooma', 'maaya', 'maye', 'mawoo', 'ayayewoo', 'ayayema', 'ayawooye', 'ayawooma', 'ayamaye', 'ayamawoo', 'yeayawoo', 'yeayama', 'yewooaya', 'yewooma', 'yemaaya', 'yemawoo', 'wooayaye', 'wooayama', 'wooyeaya', 'wooyema', 'woomaaya', 'woomaye', 'maayaye', 'maayawoo', 'mayeaya', 'mayewoo', 'mawooaya', 'mawooye', 'ayayewooma', 'ayayemawoo', 'ayawooyema', 'ayawoomaye', 'ayamayewoo', 'ayamawooye', 'yeayawooma', 'yeayamawoo', 'yewooayama', 'yewoomaaya', 'yemaayawoo', 'yemawooaya', 'wooayayema', 'wooayamaye', 'wooyeayama', 'wooyemaaya', 'woomaayaye', 'woomayeaya', 'maayayewoo', 'maayawooye', 'mayeayawoo', 'mayewooaya', 'mawooayaye', 'mawooyeaya']
    cnt = 0
    for i in babbling:
        if i in word_list:
            cnt+=1
    return cnt